"""
Módulo de Predicción de Casos de Dengue mediante Modelado ARIMAX.
Este script automatiza la lectura del mejor modelo guardado y genera predicciones 
basadas en el contexto temporal y meteorológico de 12 rezagos hacia atrás.
"""

import os
import ast
import pandas as pd
import numpy as np
import statsmodels.api as sm

# CONFIGURACIÓN GLOBAL DE RUTAS DE TU INVESTIGACIÓN
RUTA_REDUCIDO = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\2_datos\2_procesados\dataset_reducido_final.csv"
RUTA_METRICAS = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\3_resultados\metricas_modelos_arimax.xlsx"


def obtener_mejor_configuracion_arimax(ruta_excel=RUTA_METRICAS):
    """
    Lee el reporte Excel de resultados buscando dinámicamente la fila de encabezados
    para extraer el orden (p,d,q) del modelo con el menor MAE Promedio.
    """
    if not os.path.exists(ruta_excel):
        raise FileNotFoundError(f"No se encontró el reporte de métricas en: {ruta_excel}")
        
    # 1. Cargamos el Excel completo inicialmente sin asumir ninguna cabecera fija
    df_crudo = pd.read_excel(ruta_excel, header=None)
    
    # 2. Buscamos dinámicamente en qué fila se encuentra la columna 'MAE Promedio'
    fila_cabecera = None
    for idx_fila, fila in df_crudo.iterrows():
        # Convertimos la fila a string y buscamos si contiene la métrica objetivo
        fila_str = fila.astype(str).str.strip().values
        if any('MAE Promedio' in celda or 'MAE Promedio' in celda.replace('ó', 'o') for celda in fila_str):
            fila_cabecera = idx_fila
            break
            
    if fila_cabecera is None:
        raise KeyError("No se pudo localizar de forma automática la fila de encabezados que contiene 'MAE Promedio' en el Excel.")
    
    # 3. Volvemos a leer el Excel usando la fila exacta que encontramos como cabecera
    df_metricas = pd.read_excel(ruta_excel, header=fila_cabecera)
    
    # 4. Limpieza estándar de espacios en las columnas cargadas
    df_metricas.columns = df_metricas.columns.str.strip()
    
    # 5. Localización flexible de los nombres de columnas mapeadas
    nombre_columna_mae = [c for c in df_metricas.columns if 'MAE Promedio' in c or 'MAE Promedio' in c.replace('ó', 'o')][0]
    col_orden = [c for c in df_metricas.columns if 'Orden' in c][0]
    col_particion = [c for c in df_metricas.columns if 'Partici' in c][0]
    col_criterio = [c for c in df_metricas.columns if 'Criterio' in c][0]
    
    # 6. Encontrar la fila con el menor MAE Promedio y extraer los parámetros
    fila_optima = df_metricas.loc[df_metricas[nombre_columna_mae].idxmin()]
    orden_tuple = ast.literal_eval(str(fila_optima[col_orden]))
    
    return {
        'particion': fila_optima[col_particion],
        'criterio': fila_optima[col_criterio],
        'orden': orden_tuple
    }

def predecir_casos_dengue(ano, semana_epi, ruta_datos=RUTA_REDUCIDO):
    """
    Entrada: año (int) y semana_epi (int).
    Salida: Tupla con (Casos Predichos, Casos Reales Observados) en escala original.
    
    Busca la instancia en el dataset, extrae los 12 rezagos previos requeridos por el modelo 
    para poblar el estado del ARIMAX y calcula la inferencia estadística puntual.
    """
    if not os.path.exists(ruta_datos):
        raise FileNotFoundError(f"No se encontró el dataset reducido en: {ruta_datos}")
        
    # 1. Cargar datos base procesados por Lasso
    df = pd.read_csv(ruta_datos)
    
    # 2. Localizar el índice de la semana epidemiológica solicitada
    indice_objetivo = df[(df['ano'] == ano) & (df['semana_epi'] == semana_epi)].index
    
    if len(indice_objetivo) == 0:
        raise ValueError(f"No existen registros en el dataset para el Año {ano} y Semana Epidemiológica {semana_epi}")
        
    idx = indice_objetivo[0]
    
    # Validar que existan al menos 12 instancias previas para armar el histórico de rezagos
    if idx < 12:
        raise IndexError(f"La semana elegida (índice {idx}) no cuenta con las 12 instancias anteriores necesarias para calcular los rezagos.")
        
    # 3. Obtener automáticamente el mejor modelo ARIMAX entrenado según tu informe
    config_optima = obtener_mejor_configuracion_arimax()
    orden_arimax = config_optima['orden']
    
    # 4. Aislar la ventana histórica de entrenamiento (Instancias 0 hasta la posición actual)
    # Se incluye la instancia actual 'idx' para evaluar los regresores contemporáneos si los hay
    ventana_historica = df.iloc[:idx + 1].reset_index(drop=True)
    
    # 5. Identificar variables de control y aislar regresores exógenos (climatológicos)
    columnas_no_exog = ['fecha', 'semana_epi', 'ano', 'casos_dengue']
    columnas_exog = [c for c in df.columns if c not in columnas_no_exog]
    
    # 6. Preparar vectores endógenos (y) y exógenos (X) para ajustar la memoria del modelo
    # Ajustamos el modelo hasta t-1 para predecir t, o ajustamos hasta t para obtener la predicción puntual de t
    y_historico = ventana_historica['casos_dengue'].iloc[:-1]
    X_historico = ventana_historica[columnas_exog].iloc[:-1]
    
    X_futuro = ventana_historica[columnas_exog].iloc[[-1]]  # Fila t (actual)
    
    # 7. Ajustar el modelo estadístico con los datos pasados inmediatos
    model = sm.tsa.statespace.SARIMAX(
        y_historico,
        exog=X_historico,
        order=orden_arimax,
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    model_fit = model.fit(disp=False)
    
    # 8. Ejecutar el Forecast puntual para el paso t utilizando la información climática actual (t)
    prediccion_diferenciada = model_fit.forecast(steps=1, exog=X_futuro).values[0]
    
    # 9. Recuperar el valor observado real
    valor_real_diferenciado = ventana_historica['casos_dengue'].iloc[-1]
    
    # NOTA ESTADÍSTICA: Si tus datos en este archivo aún están diferenciados (cambio neto), 
    # puedes des-diferenciar sumando el valor real sin diferenciar de la semana anterior (t-1).
    # Si el dataset 'dataset_reducido_final.csv' ya almacena los niveles reales de casos,
    # estas variables representan directamente el recuento epidemiológico.
    casos_predichos = round(prediccion_diferenciada, 2)
    casos_reales = round(valor_real_diferenciado, 2)
    
    # Control para evitar valores matemáticos negativos lógicos en conteos epidemiológicos
    if casos_predichos < 0:
        casos_predichos = 0.0
        
    return casos_predichos, casos_reales


# --- EJEMPLO DE USO LOCAL (Prueba del módulo) ---
if __name__ == "__main__":
    print("--- Probando Módulo de Predicción Epidemiológica ---")
    try:
        # Reemplaza por un año y semana que existan en las filas medias/finales de tu dataset
        ejemplo_ano = 2023
        ejemplo_semana = 25
        
        pred, real = predecir_casos_dengue(ejemplo_ano, ejemplo_semana)
        
        print(f"Año: {ejemplo_ano} | Semana Epidemiológica: {ejemplo_semana}")
        print(f"-> Casos de Dengue Predichos: {pred}")
        print(f"-> Casos de Dengue Observados (Reales): {real}")
        print(f"-> Error Absoluto en esta semana: {round(abs(pred - real), 2)}")
        
    except Exception as e:
        print(f"Error al ejecutar la prueba: {e}")