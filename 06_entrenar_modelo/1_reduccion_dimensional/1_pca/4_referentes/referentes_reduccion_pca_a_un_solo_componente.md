Para realizar correctamente la división de datos en entrenamiento y validación (testeo) con datos de series temporales, **no se debe utilizar un muestreo aleatorio**. Dado que las observaciones son dependientes del tiempo, la división debe ser **cronológica**: los primeros datos se usan para entrenar y los últimos datos (los más recientes) se reservan para el testeo.

Además, como solicitas restringir el análisis al intervalo desde el año **2022 hasta el final de los datos**, el algoritmo primero filtrará el dataset por este período histórico y luego calculará los puntos de corte cronológicos para los porcentajes solicitados (80-20, 90-10, 95-5, y 97-3).

A continuación, tienes el script de Python que realiza el filtrado, ejecuta el modelo ARIMAX utilizando el componente `PC_1` en cada una de las particiones temporales, calcula el Error Absoluto Medio (MAE) tanto en el ajuste de entrenamiento como en la predicción de testeo, y genera los gráficos comparativos (líneas y barras) solicitados.

```python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.statespace.sarimax import SARIMAX

# ==========================================
# 1. CONFIGURACIÓN DE RUTAS Y CARGA DE DATOS
# ==========================================
dir_procesados = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\1_pca\2_datos\2_procesados"
dir_resultados = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\1_pca\3_resultados"

ruta_dataset = os.path.join(dir_procesados, "datos_meteorologicos_reducidos_pca.xlsx")

print("Cargando el dataset reducido por PCA...")
df = pd.read_excel(ruta_dataset)

# Asegurar formato de fecha y ordenamiento cronológico
df['fecha'] = pd.to_datetime(df['fecha'])
df = df.sort_values('fecha').reset_index(drop=True)

# ==========================================
# 2. FILTRADO TEMPORAL (DESDE 2022 EN ADELANTE)
# ==========================================
print("Filtrando datos desde el año 2022...")
df_filtrado = df[df['fecha'].dt.year >= 2022].reset_index(drop=True)
total_registros = len(df_filtrado)
print(f"Total de semanas/registros evaluados desde 2022: {total_registros}")

# Definición de variables del modelo
y = df_filtrado['casos_dengue']
X = df_filtrado[['PC_1']]

# ==========================================
# 3. EVALUACIÓN DE PARTICIONES (80-20, 90-10, 95-5, 97-3)
# ==========================================
particiones = {
    "80-20": 0.20,
    "90-10": 0.10,
    "95-5":  0.05,
    "97-3":  0.03
}

# Diccionario para almacenar los resultados de las métricas
resultados_mae = []

# Configuración base del ARIMAX determinada previamente (ej. p=1, d=1, q=1)
order_arimax = (1, 1, 1)

print("\nEvaluando particiones cronológicas...")
for nombre_particion, porc_test in particiones.items():
    # Calcular el índice de división (Split) cronológico
    tamano_test = int(np.floor(total_registros * porc_test))
    indice_corte = total_registros - tamano_test
    
    # División de la variable dependiente (Dengue)
    y_train, y_test = y.iloc[:indice_corte], y.iloc[indice_corte:]
    
    # División de la variable exógena (Clima - PC1)
    X_train, X_test = X.iloc[:indice_corte], X.iloc[indice_corte:]
    
    try:
        # Entrenar el modelo con el set de datos histórico (Train)
        modelo = SARIMAX(y_train, exog=X_train, order=order_arimax,
                         enforce_stationarity=False, enforce_invertibility=False)
        resultado_fit = modelo.fit(disp=False)
        
        # 1. MAE de Entrenamiento (valores ajustados dentro de la muestra)
        pred_train = resultado_fit.fittedvalues
        mae_train = mean_absolute_error(y_train, pred_train)
        
        # 2. MAE de Testeo (Pronóstico fuera de la muestra)
        # Especificamos los pasos a predecir y la variable exógena del futuro
        pred_test = resultado_fit.forecast(steps=tamano_test, exog=X_test)
        mae_test = mean_absolute_error(y_test, pred_test)
        
        resultados_mae.append({
            "Partición": nombre_particion,
            "N_Entrenamiento": len(y_train),
            "N_Testeo": len(y_test),
            "MAE_Entrenamiento": round(mae_train, 4),
            "MAE_Testeo": round(mae_test, 4)
        })
        print(f"-> Partición {nombre_particion} evaluada exitosamente.")
        
    except Exception as e:
        print(f"-> Error al evaluar la partición {nombre_particion}: {str(e)}")

# Convertir resultados a DataFrame
df_mae = pd.DataFrame(resultados_mae)
print("\n--- TABLA COMPARATIVA DE ERRORES (MAE) ---")
print(df_mae.to_string(index=False))

# Guardar los resultados numéricos en Excel
ruta_salida_excel = os.path.join(dir_resultados, "metricas_particiones_mae.xlsx")
df_mae.to_excel(ruta_salida_excel, index=False)

# ==========================================
# 4. GENERACIÓN DE GRÁFICOS
# ==========================================
x_labels = df_mae["Partición"]
x_indices = np.arange(len(x_labels))
width = 0.35

# ---- GRÁFICO 1: DIAGRAMA DE BARRAS COMPARATIVO ----
plt.figure(figsize=(10, 6))
plt.bar(x_indices - width/2, df_mae["MAE_Entrenamiento"], width, label='MAE Entrenamiento', color='#3498db')
plt.bar(x_indices + width/2, df_mae["MAE_Testeo"], width, label='MAE Testeo', color='#e74c3c')

plt.xlabel('Estrategia de División (Train-Test)', fontsize=12)
plt.ylabel('Error Absoluto Medio (MAE)', fontsize=12)
plt.title('Comparativo de MAE por Partición Temporal (Desde 2022)\n[Diagrama de Barras]', fontsize=14, fontweight='bold')
plt.xticks(x_indices, x_labels)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

ruta_barras = os.path.join(dir_resultados, "grafico_barras_mae.png")
plt.savefig(ruta_barras, dpi=300)
print(f"\nGráfico de barras guardado en: {ruta_barras}")
plt.close()

# ---- GRÁFICO 2: GRÁFICO DE LÍNEAS ----
plt.figure(figsize=(10, 6))
plt.plot(x_labels, df_mae["MAE_Entrenamiento"], marker='o', linewidth=2, markersize=8, label='MAE Entrenamiento', color='#2980b9')
plt.plot(x_labels, df_mae["MAE_Testeo"], marker='s', linewidth=2, markersize=8, label='MAE Testeo', color='#c0392b')

plt.xlabel('Estrategia de División (Train-Test)', fontsize=12)
plt.ylabel('Error Absoluto Medio (MAE)', fontsize=12)
plt.title('Tendencia del MAE según Proporción de Datos (Desde 2022)\n[Gráfico de Líneas]', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

ruta_lineas = os.path.join(dir_resultados, "grafico_lineas_mae.png")
plt.savefig(ruta_lineas, dpi=300)
print(f"Gráfico de líneas guardado en: {ruta_lineas}")
plt.close()

print("\n¡Análisis comparativo de particiones finalizado!")

```

### ¿Cómo interpretar las gráficas y resultados que generará este script?

Cuando revises el archivo `metricas_particiones_mae.xlsx` y las imágenes guardadas en la carpeta de resultados, presta atención a la relación entre los dos errores:

1. **Efecto del tamaño del testeo:** Las particiones como la `97-3` evalúan al modelo en un horizonte de tiempo muy corto (apenas las últimas semanas del dataset). Esto suele resultar en un MAE de testeo bajo si la tendencia no cambia drásticamente, pero representa una validación menos exigente.
2. **Evaluación de sobreajuste:** El MAE de entrenamiento medirá qué tan bien se memorizó el pasado el algoritmo. Si el MAE de testeo en la partición `80-20` (que pone a prueba al modelo durante un período largo) se dispara a valores extremadamente altos en comparación con el de entrenamiento, te indicará que el modelo ARIMAX está perdiendo capacidad de generalización ante cambios estacionales climáticos de largo plazo.