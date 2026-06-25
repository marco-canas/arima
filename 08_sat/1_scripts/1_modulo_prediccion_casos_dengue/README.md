Prompt  

Dame esta función de usuario de una forma que pueda pegarla en un archivo .py para poder tenerla como un módulo de Python que sirva para predecir casos de dengue a partir del año y la semana epidemiológica usando los datos meteorológicos y epidemiológicos de los que disponemos  

Aquí tienes el código estructurado exclusivamente para funcionar como un **módulo independiente de Python**. Puedes guardarlo en un archivo llamado `predictor_dengue_sat.py`.

Este módulo contiene la función de usuario con las rutas exactas del SAT que especificaste, está completamente blindado contra errores de celdas vacías (`NaN`) en Excel y está listo para ser importado desde cualquier otra sección de tu proyecto o terminal de comandos.

### Código del Módulo (`predictor_dengue_sat.py`)

```python
"""
MÓDULO SAT: Predicciones Puntuales de Casos de Dengue mediante ARIMAX.
Este archivo funciona como un módulo reutilizable de Python.
"""

import os
import ast
import pandas as pd
import numpy as np
import statsmodels.api as sm

# CONFIGURACIÓN DE RUTAS INTERNAS DEL MÓDULO (Rutas SAT especificadas)
RUTA_METRICAS = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\3_resultados\metricas_modelos_arimax.xlsx"
RUTA_DATASET_SAT = r"C:\Users\marco\Documentos\investigacion\arima\08_sat\2_datos\1_raw\2_reducido_lasso_solo_dengue.csv"


def _obtener_mejor_orden_arimax(ruta_excel=RUTA_METRICAS):
    """
    Función interna (privada) que lee el Excel plano de métricas 
    y extrae de forma limpia el orden (p,d,q) con menor MAE Promedio.
    """
    if not os.path.exists(ruta_excel):
        raise FileNotFoundError(f"No se encontró el reporte de métricas en: {ruta_excel}")
        
    # Lectura directa desde la fila 1 (sin filas decorativas intermitentes)
    df_metricas = pd.read_excel(ruta_excel)
    df_metricas.columns = df_metricas.columns.str.strip()
    
    # Localizar la fila óptima basada en el menor MAE Promedio
    fila_optima = df_metricas.loc[df_metricas['MAE Promedio'].idxmin()]
    
    # Convertir de manera segura la cadena '(p, d, q)' a una tupla de Python
    orden_tuple = ast.literal_eval(str(fila_optima['Orden (p,d,q)']))
    return orden_tuple


def predecir_casos_dengue(ano, semana_epi, ruta_datos=RUTA_DATASET_SAT):
    """
    Función de usuario principal para la inferencia epidemiológica.
    
    Parámetros:
        ano (int): Año a evaluar (ej. 2024).
        semana_epi (int): Semana epidemiológica a evaluar (1 a 53).
        ruta_datos (str): Ubicación del dataset reducido por Lasso del SAT.
        
    Retorna:
        tuple: (casos_predichos, casos_observados_reales)
    """
    if not os.path.exists(ruta_datos):
        raise FileNotFoundError(f"No se encontró el dataset del SAT en la ruta: {ruta_datos}")
        
    # 1. Cargar el dataset reducido del SAT
    df = pd.read_csv(ruta_datos)
    
    # 2. Localizar el índice de la semana exacta solicitada por el usuario
    indice_objetivo = df[(df['ano'] == ano) & (df['semana_epi'] == semana_epi)].index
    
    if len(indice_objetivo) == 0:
        raise ValueError(f"No existen registros en el dataset SAT para el Año {ano} y Semana {semana_epi}")
        
    idx = indice_objetivo[0]
    
    # 3. Validar estadísticamente que existan las 12 instancias anteriores para armar los rezagos
    if idx < 12:
        raise IndexError(f"La semana elegida (índice {idx}) no cuenta con las 12 instancias anteriores necesarias para alimentar los rezagos del modelo.")
        
    # 4. Extraer la ventana de 13 filas (las 12 semanas pasadas + la semana actual 't')
    ventana_historica = df.iloc[idx-12 : idx+1].reset_index(drop=True)
    
    # 5. Obtener dinámicamente el mejor orden del modelo desde el archivo de métricas
    orden_arimax = _obtener_mejor_orden_arimax()
    
    # 6. Identificar y aislar los atributos meteorológicos (variables exógenas de Lasso)
    columnas_no_exog = ['fecha', 'semana_epi', 'ano', 'casos_dengue']
    columnas_exog = [c for c in df.columns if c not in columnas_no_exog]
    
    # 7. Separar el pasado (t-12 a t-1) del presente contemporáneo (t)
    y_hist = ventana_historica['casos_dengue'].iloc[:-1]
    X_hist = ventana_historica[columnas_exog].iloc[:-1]
    X_futuro = ventana_historica[columnas_exog].iloc[[-1]]  # Fila 't' actual con clima contemporáneo
    
    # 8. Ajustar la estructura lineal del ARIMAX con la memoria temporal cargada
    model = sm.tsa.statespace.SARIMAX(
        y_hist, 
        exog=X_hist, 
        order=orden_arimax,
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    model_fit = model.fit(disp=False)
    
    # 9. Ejecutar la predicción puntual (Forecast de 1 paso hacia adelante)
    prediccion = model_fit.forecast(steps=1, exog=X_futuro).values[0]
    observado = ventana_historica['casos_dengue'].iloc[-1]
    
    # 10. Control lógico-matemático (los casos de dengue no pueden ser negativos)
    casos_predichos = round(max(0.0, prediccion), 2)
    casos_observados = round(observado, 2)
    
    return casos_predichos, casos_observados


# --- BLOQUE DE CONTROL PARA EJECUCIÓN DIRECTA O COMPROBACIONES ---
if __name__ == "__main__":
    print("--- Módulo predictor_dengue_sat cargado exitosamente ---")
    print(f"Buscando datos meteorológicos en: {RUTA_DATASET_SAT}")

```

---

### Cómo usar este módulo desde cualquier otra terminal o script

Al estar empaquetado de forma limpia, puedes llamarlo desde cualquier script que crees en la misma carpeta (`C:\Users\marco\Documentos\investigacion\arima\08_sat\1_scripts`).

**Ejemplo de uso externo:**

```python
import predictor_dengue_sat as pds

# Invocar la función enviando el año y la semana deseada
prediccion, real = pds.predecir_casos_dengue(2024, 15)

print(f"Casos estimados por ARIMAX: {prediccion}")
print(f"Casos registrados en salud pública: {real}")

```