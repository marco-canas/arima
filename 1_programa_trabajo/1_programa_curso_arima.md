# Prompt para diseño de curso de arima para predicción de dengue  

# Cronograma de actividades: Modelado ARIMA/SARIMA/ARIMAX

---

## 🗓️ Mayo 24 – Mayo 31, 2025  
**Tarea:** Exploración de la base de datos epidemiológica y climática  
**Objetivo:** Verificar la calidad, formato y continuidad temporal de los datos  
**Desarrollo:**
- Cargar datos en Python (Visual Studio Code)
- Asegurar estructura semanal (casos de dengue y variables climáticas)
- Comprobar ausencia de duplicados y valores faltantes
- Validar correspondencia entre fechas y semanas epidemiológicas
- Documentar variables disponibles y su unidad de medida

---

## 🗓️ Mayo 31 – Junio 7  
**Tarea:** Generar visualizaciones exploratorias de las series temporales  
**Objetivo:** Identificar tendencias, estacionalidades y valores atípicos  
**Desarrollo:**
- Graficar la serie de casos de dengue y cada variable climática
- Observar patrones visuales (incrementos, caídas, estacionalidad)
- Identificar posibles outliers
- Guardar gráficos para incluir en tesis como análisis exploratorio

---

## 🗓️ Junio 7 – Junio 14  
**Tarea:** Analizar correlaciones entre clima y dengue  
**Objetivo:** Determinar asociaciones preliminares entre variables  
**Desarrollo:**
- Calcular coeficientes de Pearson y Spearman
- Graficar matrices de correlación con mapas de calor
- Analizar rezagos visuales en las series climáticas
- Anotar variables con mayor correlación

---

## 🗓️ Junio 14 – Junio 21  
**Tarea:** Identificar la autocorrelación en la serie de dengue  
**Objetivo:** Comprender la estructura temporal interna de la serie  
**Desarrollo:**
- Calcular y graficar ACF y PACF
- Identificar rezagos significativos
- Estimar valores tentativos para p y q
- Guardar figuras para el capítulo de metodología

---

## 🗓️ Junio 21 – Junio 28  
**Tarea:** Evaluar la estacionariedad de la serie  
**Objetivo:** Diagnosticar si la serie necesita diferenciación  
**Desarrollo:**
- Aplicar la prueba ADF (Dickey-Fuller aumentada)
- Interpretar resultados estadísticos (p-valor, estadístico)
- Diferenciar la serie si es necesario y volver a aplicar ADF
- Conservar versión final de la serie transformada

---

## 🗓️ Junio 28 – Julio 5  
**Tarea:** Determinar parámetros iniciales del modelo ARIMA  
**Objetivo:** Establecer valores (p,d,q) iniciales para los modelos  
**Desarrollo:**
- Definir el orden de diferenciación (d)
- Usar ACF y PACF para determinar p y q
- Probar combinaciones de parámetros iniciales
- Comparar visualmente el ajuste a la serie real

---

## 🗓️ Julio 5 – Julio 12  
**Tarea:** Ajustar los primeros modelos ARIMA  
**Objetivo:** Evaluar el desempeño de modelos candidatos  
**Desarrollo:**
- Ajustar modelos ARIMA con diferentes combinaciones (p,d,q)
- Evaluar AIC, BIC y residuos
- Documentar modelos con mejor desempeño

---

## 🗓️ Julio 12 – Julio 19  
**Tarea:** Refinar los modelos ARIMA  
**Objetivo:** Optimizar el ajuste y reducir error  
**Desarrollo:**
- Ajustar modelos con parámetros alternativos cercanos
- Comparar residuales, validar supuestos del modelo
- Usar gráficos de residuos y prueba de Ljung-Box
- Seleccionar el mejor modelo sin sobreajuste

---

## 🗓️ Julio 19 – Julio 26  
**Tarea:** Validar el modelo ARIMA final  
**Objetivo:** Confirmar su capacidad predictiva  
**Desarrollo:**
- Dividir la serie en entrenamiento y prueba
- Evaluar error de predicción (RMSE, MAE, MAPE)
- Comparar resultados con serie observada
- Confirmar robustez del modelo

---

## 🗓️ Julio 26 – Agosto 2  
**Tarea:** Redactar resultados del modelo ARIMA  
**Objetivo:** Dejar lista la sección preliminar del capítulo de resultados  
**Desarrollo:**
- Documentar parámetros seleccionados
- Insertar tablas de desempeño del modelo
- Incluir gráficos de predicción y residuales
- Redactar interpretación técnica de resultados

---

## 🗓️ Agosto 2 – Agosto 9  
**Tarea:** Evaluar estacionalidad en la serie de dengue  
**Objetivo:** Identificar si hay patrones estacionales claros  
**Desarrollo:**
- Graficar la serie por años superpuestos
- Calcular autocorrelación estacional (rezagos 12, 24, etc.)
- Confirmar necesidad de SARIMA
- Estimar período estacional (s)

---

## 🗓️ Agosto 9 – Agosto 16  
**Tarea:** Determinar parámetros SARIMA iniciales  
**Objetivo:** Estimar (P,D,Q,s) junto con (p,d,q)  
**Desarrollo:**
- Aplicar diferenciación estacional si es necesario
- Usar ACF/PACF para sugerir valores P y Q
- Establecer combinaciones iniciales de SARIMA
- Utilizar auto_arima para comparar

---

## 🗓️ Agosto 16 – Agosto 23  
**Tarea:** Ajustar modelos SARIMA  
**Objetivo:** Evaluar comportamiento de modelos estacionales  
**Desarrollo:**
- Probar al menos 3 combinaciones con SARIMAX
- Registrar métricas AIC, BIC, RMSE, residuos
- Comparar ajuste con ARIMA
- Evaluar reducción de error

---

## 🗓️ Agosto 23 – Agosto 30  
**Tarea:** Validar y seleccionar el mejor modelo SARIMA  
**Objetivo:** Verificar si SARIMA mejora sobre ARIMA  
**Desarrollo:**
- Dividir serie para entrenamiento/prueba
- Calcular errores de predicción
- Evaluar gráficos de ajuste y residuos
- Tomar decisión sobre modelo final

---

## 🗓️ Agosto 30 – Septiembre 6  
**Tarea:** Redactar resultados de modelos SARIMA  
**Objetivo:** Documentar ajuste y comportamiento estacional  
**Desarrollo:**
- Insertar tablas comparativas entre ARIMA y SARIMA
- Redactar análisis de estacionalidad
- Incluir gráficos explicativos
- Explicar decisiones metodológicas

---

## 🗓️ Septiembre 6 – Septiembre 13  
**Tarea:** Preparar datos exógenos para ARIMAX  
**Objetivo:** Seleccionar y transformar variables climáticas  
**Desarrollo:**
- Evaluar correlaciones con rezago
- Seleccionar variables relevantes
- Crear variables climáticas con desfase
- Alinear fechas y escalas

---

## 🗓️ Septiembre 13 – Septiembre 20  
**Tarea:** Ajustar modelos ARIMAX  
**Objetivo:** Integrar variables climáticas como exógenas  
**Desarrollo:**
- Ajustar modelos ARIMA con variables exógenas
- Evaluar significancia de coeficientes
- Verificar supuestos del modelo
- Comparar con modelos sin exógenas

---

## 🗓️ Septiembre 20 – Septiembre 27  
**Tarea:** Validar el modelo ARIMAX  
**Objetivo:** Evaluar capacidad predictiva y explicativa  
**Desarrollo:**
- Calcular errores (RMSE, MAE, MAPE)
- Evaluar contribución de cada variable climática
- Estimar rezago más explicativo
- Decidir si mejora sustancialmente el ajuste

---

## 🗓️ Septiembre 27 – Octubre 4  
**Tarea:** Evaluar desempeño como clasificador binario  
**Objetivo:** Probar modelo para predecir semanas epidémicas  
**Desarrollo:**
- Crear variable binaria de epidemia
- Usar predicción del modelo para clasificar
- Calcular métricas: precisión, recall, F1, AUC
- Evaluar utilidad para alerta temprana

---

## 🗓️ Octubre 4 – Octubre 11  
**Tarea:** Consolidar y comparar modelos  
**Objetivo:** Identificar el modelo más adecuado  
**Desarrollo:**
- Tabla comparativa de métricas
- Interpretación de resultados climáticos
- Discusión metodológica
- Elección del modelo para la tesis

---

## 🗓️ Octubre 11 – Octubre 18  
**Tarea:** Redactar capítulo de resultados (ARIMAX incluido)  
**Objetivo:** Documentar completamente el análisis  
**Desarrollo:**
- Tablas con coeficientes y significancia
- Gráficos de predicción vs observado
- Interpretación climática y epidemiológica
- Redacción clara, académica

---

## 🗓️ Octubre 18 – Octubre 25  
**Tarea:** Preparar material gráfico para presentación  
**Objetivo:** Comunicar visualmente los hallazgos  
**Desarrollo:**
- Selección de gráficos clave
- Preparar presentaciones para asesorías
- Ensayar explicación oral

---

## 🗓️ Octubre 25 – Noviembre 1  
**Tarea:** Elaborar resumen técnico del proceso metodológico  
**Objetivo:** Sintetizar enfoque metodológico para la tesis  
**Desarrollo:**
- Crear diagrama del flujo metodológico
- Redactar texto explicativo
- Anexar decisiones clave
- Incorporar citas actualizadas

---

## 🗓️ Noviembre 1 – Noviembre 8  
**Tarea:** Revisión crítica de resultados y redacción  
**Objetivo:** Afinar análisis estadístico y epidemiológico  
**Desarrollo:**
- Releer y mejorar argumentación
- Revisar coherencia resultados–objetivos
- Integrar retroalimentación del tutor
- Asegurar claridad de figuras y tablas

---

## 🗓️ Noviembre 8 – Noviembre 15  
**Tarea:** Integración con otras partes de la tesis  
**Objetivo:** Preparar transición con discusión y conclusiones  
**Desarrollo:**
- Identificar elementos clave para discusión
- Señalar implicaciones para política pública
- Anotar ideas de limitaciones e investigaciones futuras
- Conectar resultados con contexto regional (Caucasia)

---

## 🗓️ Noviembre 15 – Diciembre 13  
**Tarea:** Paquete final del modelo ajustado  
**Objetivo:** Cerrar completamente la fase de modelado  
**Desarrollo:**
- Guardar código limpio y comentado
- Crear archivo resumen con parámetros finales
- Organizar carpeta de figuras, gráficos y tablas
- Respaldar y enviar información al asesor
