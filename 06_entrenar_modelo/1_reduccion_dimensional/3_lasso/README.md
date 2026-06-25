Prompt  

Dame el script que implemente todas las recomendaciones aplicables que me acabas de dar, para hacer esta reducción dimensional con la estretegia de regularización Lasso al dataset de la ubicación: "C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\2_datos\1_raw\2_meteo_epi_rezagos_2026_1.xlsx", pero asume que la variable casos_dengue no tiene estacionalidad anual y no escales ni modifiques a la variable casos_dengue ni a sus 12 rezagos. A lo que termines de escalar los atributos meteorológicos, sin escalar los atributos epidemiológicos, guárdame el nuevo dataset en: "C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\2_datos\2_procesados" y en "C:\Users\marco\Documentos\investigacion\arima\08_sat\1_scripts\1_modulo_prediccion_casos_dengue". El dataset final reducido, por favor guárdamelo en las mismas carpeta anteriores. El informe del escalamiento y la reducción dámelo en un archivo excel guardado en "C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\3_resultados". Revisa que después de la reducción dimensional, ningún valor de las variables de casos de dengue y de sus rezagos, hayan sido cambiadas. Tampoco deben ser cambiadas, las variables de año, semana_epi y fecha. Pero no le cambies el nombre a las variables ni en el escalado ni en la reducción. 



Aquí tienes el script definitivo corregido que incorpora de forma estricta la **inmutabilidad absoluta de los nombres de todas las variables**.

En las versiones previas, al aplicar el `RobustScaler` de scikit-learn, el DataFrame resultante volvía a tomar los nombres de las columnas meteorológicas pero el dataset intermedio (`dataset_escalado_completo.csv`) unía los bloques manteniendo intactos los nombres originales del archivo de Excel. En este script se ha blindado y verificado que tanto el dataset intermedio como el dataset final reducido **conserven exactamente el mismo nombre y tipografía de cada variable**, sin agregar prefijos, sufijos ni alterar las mayúsculas/minúsculas.

### Código Completo en Python

```python
import os
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import Font, PatternFill
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LassoCV
from sklearn.model_selection import TimeSeriesSplit

# =====================================================================
# 1. CONFIGURACIÓN DE RUTAS DE ENTRADA Y SALIDA
# =====================================================================
RUTA_RAW_EXCEL = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\2_datos\1_raw\2_meteo_epi_rezagos_2026_1.xlsx"

CARPETA_PROCESADOS = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\2_datos\2_procesados"
CARPETA_SAT = r"C:\Users\marco\Documentos\investigacion\arima\08_sat\1_scripts\1_modulo_prediccion_casos_dengue"
CARPETA_RESULTADOS = r"C:\Users\marco\Documentos\investigacion\arima\06_entrenar_modelo\1_reduccion_dimensional\3_lasso\3_resultados"

for carpeta in [CARPETA_PROCESADOS, CARPETA_SAT, CARPETA_RESULTADOS]:
    os.makedirs(carpeta, exist_ok=True)

# =====================================================================
# 2. CARGA Y DETECCIÓN FLEXIBLE DE COLUMNAS (MANTENIENDO NOMBRES ORIGINALES)
# =====================================================================
print(">>> Leyendo dataset original...")
df_original = pd.read_excel(RUTA_RAW_EXCEL)

# Limpiar espacios en blanco fantasmas en los extremos pero preservar el nombre original textualmente
df_original.columns = df_original.columns.str.strip()

# Guardar una copia exacta del orden y nombres originales de las columnas
columnas_orden_original = list(df_original.columns)

df_original['fecha'] = pd.to_datetime(df_original['fecha'])
df_original = df_original.sort_values('fecha').reset_index(drop=True)

# Detección dinámica de la columna año para evitar errores de codificación (ñ/n)
columna_ano_real = 'año' if 'año' in df_original.columns else 'ano'

# Definir columnas protegidas de control y epidemiológicas (Inmutables)
columnas_control = ['fecha', 'semana_epi', columna_ano_real]
columnas_dengue = ['casos_dengue'] + [c for c in df_original.columns if 'casos_dengue_lag' in c]
columnas_protegidas = columnas_control + columnas_dengue

# Definir atributos meteorológicos a procesar
columnas_meteorologicas = [c for c in df_original.columns if c not in columnas_protegidas]

# =====================================================================
# 3. ESCALAMIENTO EXCLUSIVO (CONSERVANDO LOS NOMBRES ORIGINALES)
# =====================================================================
print(">>> Aplicando RobustScaler solo a variables meteorológicas (sin alterar nombres)...")
scaler = RobustScaler()
scaled_meteo = scaler.fit_transform(df_original[columnas_meteorologicas])

# Creamos el DataFrame intermedio asignando exactamente los mismos nombres originales
df_scaled_meteo = pd.DataFrame(scaled_meteo, columns=columnas_meteorologicas)

# Reconstruir el dataset completo pre-Lasso uniendo los bloques
df_pre_lasso = pd.concat([df_original[columnas_protegidas].reset_index(drop=True), df_scaled_meteo], axis=1)

# Reordenar las columnas del dataset escalado para que mantengan la estructura idéntica del Excel original
df_pre_lasso = df_pre_lasso[columnas_orden_original]

# Guardar dataset escalado completo en ambas ubicaciones
for carpeta in [CARPETA_PROCESADOS, CARPETA_SAT]:
    df_pre_lasso.to_csv(os.path.join(carpeta, "dataset_escalado_completo.csv"), index=False)

# =====================================================================
# 4. REGULARIZACIÓN DIMENSIONAL MEDIANTE LASSO
# =====================================================================
print(">>> Ejecutando optimización Lasso mediante Validación Cruzada Temporal...")

y = df_pre_lasso['casos_dengue']
# El modelo entrena usando la matriz sin las variables estrictas de control temporal
X = df_pre_lasso[[c for c in df_pre_lasso.columns if c not in columnas_control]]

tscv = TimeSeriesSplit(n_splits=5)
lasso_cv = LassoCV(alphas=np.logspace(-4, 1, 100), cv=tscv, max_iter=10000, random_state=42)
lasso_cv.fit(X, y)

coeficientes = lasso_cv.coef_
mejores_atributos = []

# Identificar qué variables meteorológicas sobrevivieron manteniendo su nombre intacto
for col, coef in zip(X.columns, coeficientes):
    if col in columnas_meteorologicas and coef != 0:
        mejores_atributos.append(col)

print(f"-> Lasso finalizado. Atributos climáticos seleccionados: {len(mejores_atributos)} de {len(columnas_meteorologicas)}")

# =====================================================================
# 5. CONSTRUCCIÓN DEL DATASET FINAL REDUCIDO
# =====================================================================
# El orden final de las columnas respetará el orden en el que aparecían en el Excel original
columnas_finales_reducidas = [c for c in columnas_orden_original if c in columnas_protegidas or c in mejores_atributos]
df_reducido_final = df_pre_lasso[columnas_finales_reducidas]

# Exportación del dataset definitivo
for carpeta in [CARPETA_PROCESADOS, CARPETA_SAT]:
    ruta_final_csv = os.path.join(carpeta, "dataset_reducido_final.csv")
    df_reducido_final.to_csv(ruta_final_csv, index=False)
    print(f"   Guardado exitoso en: {ruta_final_csv}")

# =====================================================================
# 6. AUDITORÍA EXIGENTE DE INTEGRIDAD E INMUTABILIDAD DE VALORES
# =====================================================================
print("\n>>> Iniciando auditoría de integridad de datos...")
errores_detectados = 0

for col in columnas_protegidas:
    # Comparación estricta usando Pandas .equals() que valida tanto tipos como NaN de forma exacta
    if not df_original[col].equals(df_reducido_final[col]):
        print(f"   [ALERTA] La columna protegida '{col}' sufrió alteraciones numéricas o de tipo.")
        errores_detectados += 1

if errores_detectados == 0:
    print("   [ÉXITO] Auditoría superada: Casos de dengue, rezagos y variables de control se mantuvieron 100% INMUTABLES.")
else:
    print(f"   [FALLO] Se detectaron {errores_detectados} inconsistencias estructurales.")

# =====================================================================
# 7. INFORME EJECUTIVO EN EXCEL
# =====================================================================
print("\n>>> Generando reporte Excel de la reducción dimensional...")
ruta_informe = os.path.join(CARPETA_RESULTADOS, "informe_escalamiento_y_lasso.xlsx")

wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "Resumen del Proceso"
ws1.views.sheetView[0].showGridLines = True

ws1.append(["Métrica / Parámetro del Proceso", "Valor Evaluado"])
ws1.append(["Mejor Alpha Seleccionado (Lasso)", lasso_cv.alpha_])
ws1.append(["Total Atributos Meteorológicos Iniciales", len(columnas_meteorologicas)])
ws1.append(["Total Atributos Meteorológicos Sobrevivientes", len(mejores_atributos)])
ws1.append(["Total Columnas Protegidas (Dengue e Historial)", len(columnas_protegidas)])
ws1.append(["Estado de Auditoría de Inmutabilidad", "APROBADO" if errores_detectados == 0 else "RECHAZADO"])

ws2 = wb.create_sheet(title="Coeficientes Lasso Climáticos")
ws2.views.sheetView[0].showGridLines = True
ws2.append(["Atributo Meteorológico", "Coeficiente Beta", "Estado de Selección"])

for col, coef in zip(X.columns, coeficientes):
    if col in columnas_meteorologicas:
        estado = "CONSERVADO" if coef != 0 else "ELIMINADO"
        ws2.append([col, round(coef, 6), estado])

# Estilos visuales del Excel
for ws in [ws1, ws2]:
    ws.row_dimensions[1].height = 20
    ws.cell(row=1, column=1).font = Font(bold=True, color="FFFFFF")
    ws.cell(row=1, column=2).font = Font(bold=True, color="FFFFFF")
    ws.cell(row=1, column=1).fill = PatternFill(start_color="1B365D", fill_type="solid")
    ws.cell(row=1, column=2).fill = PatternFill(start_color="1B365D", fill_type="solid")
    if ws == ws2:
        ws.cell(row=1, column=3).font = Font(bold=True, color="FFFFFF")
        ws.cell(row=1, column=3).fill = PatternFill(start_color="1B365D", fill_type="solid")
        
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 15)

wb.save(ruta_informe)
print(f">>> Informe Excel guardado con éxito en: {ruta_informe}")
print("\n--- PROCESO FINALIZADO CORRECTAMENTE ---")

```

### Aspectos clave incorporados:

1. **Preservación Estricta de Nombres:** `pd.DataFrame(scaled_meteo, columns=columnas_meteorologicas)` asegura que los nombres meteorológicos originales se reasignen de inmediato tras el cálculo del `RobustScaler`, previniendo la creación de nombres genéricos como `0, 1, 2...`.
2. **Reordenación de Columnas Original:** Se implementó `df_pre_lasso[columnas_orden_original]` para garantizar que el archivo final mantenga exactamente el mismo orden de izquierda a derecha que poseía el archivo `.xlsx` de origen, evitando desorganizar la estructura de las columnas.
3. **Control Total de Inmutabilidad:** La función `.equals()` de Pandas verifica celda por celda que ningún valor de la serie temporal ni del conteo de casos epidemiológicos haya cambiado un solo decimal durante las etapas matemáticas intermedias.