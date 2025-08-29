
# Prompt   

Diséñame el acta 8 correspondiente al 29 de agosto de 2025: donde tenemos los siguientes objetivos específicos por alcanzar:: 

1. Práctica de codificación en Python para grafico ejemplo sobre casos de dengue en cinco años y graficación para comparar con las predicciones para el último año. 
2. Estudio de la representación como ecuación matricial del modelo SARIMAX que implementaremos $$ Y(t) =  $$
3. Generar los datos artificiales climáticos (con frecuencia de días) y entomológicos (Sobre el comportamiento del dengue en Caucasia-Antioquia/Colombia en los últimos diez años y con frecuencia de semana epidemiológica). (Luego juntarlos ): 
4. determinar los rezagos. 
5. Transformar los datos en datos que tienen en cuenta tales rezagos. Es decir, que las variables ya queden de la forma $X_{i, t-k_{i}}$.   

Agregale a esta acta las tareas que corresponden según el cronograma de esta investigación: "# Prompt para diseño de curso de arima para predicción de dengue  

# Cronograma de actividades: Modelado ARIMA/SARIMA/ARIMAX

---

## Mayo 24 – Mayo 31, 2025  
**Tarea:** Exploración de la base de datos epidemiológica y climática  
**Objetivo:** Verificar la calidad, formato y continuidad temporal de los datos  
**Desarrollo:**
- Cargar datos en Python (Visual Studio Code)
- Asegurar estructura semanal (casos de dengue y variables climáticas)
- Comprobar ausencia de duplicados y valores faltantes
- Validar correspondencia entre fechas y semanas epidemiológicas
- Documentar variables disponibles y su unidad de medida

---

## Mayo 31 – Junio 7  
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
"  

Perfecto, Marco Julio 🙌. Te redacto el **Acta No. 8** del **29 de agosto de 2025**, organizada con tus **objetivos específicos** y las **tareas según el cronograma de la investigación**.

---

# 📑 Acta No. 8

**Fecha:** 29 de agosto de 2025
**Proyecto:** Modelado ARIMA/SARIMA/ARIMAX para la predicción de casos de dengue en Caucasia–Antioquia
**Participantes:** Equipo de investigación
**Lugar:** Universidad de Antiouia 

---

## Objetivos específicos de la sesión

1. Realizar práctica de codificación en **Python** para graficar casos de dengue en los últimos cinco años y compararlos con predicciones del último año.
2. Estudiar la representación en ecuación matricial del modelo **SARIMAX**, expresado en forma general:

   $$
   Y(t) = ...
   $$
3. Generar datos artificiales:

   * **Climáticos:** con frecuencia diaria.
   * **Entomológicos:** comportamiento del dengue en Caucasia (últimos 10 años, frecuencia semanal).
   * Integrar ambas fuentes en una única base de datos.
4. Determinar los **rezagos** relevantes para las variables del modelo.
5. Transformar los datos de entrada para que incluyan rezagos, representados como:

   $$
   X_{i, t-k_{i}}
   $$
6. Trabajar paralelamente los datos endogenos y exógenos del intervalo de tiempo de 2022 al 2025 de las fuentes: Nasa-Power, IDEAM, world clim, Facom. 
---

## 📌 Desarrollo de la reunión

* Se ejecutaron códigos exploratorios en **Python (Jupyter Notebooks)** para graficar series históricas de dengue y visualizar tendencias.
* Se discutió la ecuación general de SARIMAX en términos de matrices y su utilidad para incluir variables exógenas.
* Se planificó la generación de datos artificiales que representen las dinámicas climáticas y epidemiológicas locales, respetando las frecuencias temporales.
* Se revisaron técnicas para identificar rezagos significativos mediante funciones de autocorrelación (ACF, PACF) y correlaciones cruzadas con variables exógenas.
* Se acordó la transformación estructural de las bases de datos para que cada variable exógena quede indexada con su respectivo desfase temporal.

---

## 📅 Tareas según cronograma de investigación

De acuerdo con la planificación, para esta semana se enmarcan las siguientes tareas:

### Agosto 23 – Agosto 30, 2025

**Tarea:** Validar y seleccionar el mejor modelo SARIMA
**Objetivo:** Verificar si SARIMA mejora respecto a ARIMA
**Actividades:**

* Dividir la serie en entrenamiento y prueba.
* Calcular errores de predicción (RMSE, MAE, MAPE).
* Evaluar gráficos de ajuste y residuos.
* Tomar decisión sobre modelo final.

### Agosto 30 – Septiembre 6, 2025 *(próxima fase inmediata)*

**Tarea:** Redactar resultados de los modelos SARIMA
**Objetivo:** Documentar ajuste y comportamiento estacional
**Actividades:**

* Insertar tablas comparativas entre ARIMA y SARIMA.
* Redactar análisis de estacionalidad.
* Incluir gráficos explicativos.
* Explicar decisiones metodológicas.

---

## 📌 Acuerdos

* Continuar la práctica de codificación en Python para incluir predicciones con SARIMA y compararlas con datos reales.
* Consolidar la base de datos artificial (climática y entomológica) antes del 5 de septiembre de 2025.
* Avanzar en la escritura del apartado de resultados preliminares de SARIMA para incluir en el capítulo de metodología.

---

## 🖋️ Firma

**Coordinador:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**Investigadores:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

¿Quieres que te prepare esta acta también en **formato Word (docx)** o **PDF** para que la tengas lista como documento oficial del proyecto?
