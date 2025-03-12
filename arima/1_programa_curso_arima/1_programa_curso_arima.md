# Prompt para diseño de curso de arima para predicción de dengue  

Dame una estructura para un curso sobre el algoritmo ARIMA y su aplicación a series temporales de datos meteorológicos para construir modelos de predicción de dengue en Caucasia

### Estructura del Curso:
Esta es una estructura detallada para un curso especializado en **ARIMA aplicado a predicción de dengue usando datos meteorológicos** (contexto: Caucasia, Antioquia):

---

### **Curso: Modelado ARIMA para predicción de dengue basada en variables meteorológicas**  
**Duración:** 40 horas (5 módulos, 8 horas cada uno)  
**Nivel:** Intermedio (requisitos: estadística básica, manejo de Python/R)  

---

#### **Módulo 1: Fundamentos de series temporales y dengue en contextos tropicales**  
**Objetivo:** Contextualizar la relación clima-dengue y repasar conceptos estadísticos clave.  
**Contenido:**  
1. **Dengue en Caucasia:**  
   - Epidemiología local (tasas históricas, estacionalidad).  
   - Factores meteorológicos críticos: lluvias, temperatura, humedad (datos del IDEAM Antioquia).  
2. **Series temporales en meteorología:**  
   - Características de datos climáticos: estacionalidad, tendencias, ciclos.  
   - Fuentes de datos abiertos: IDEAM, SIVIGILA (reportes de dengue).  
3. **Introducción a ARIMA:**  
   - ¿Por qué ARIMA para predicción de enfermedades?  
   - Caso de éxito: Modelado de malaria en Urabá (ejemplo regional).  

**Actividad:** Análisis exploratorio de dataset real de Caucasia (2008-2025) con Python/Pandas.  

---

#### **Módulo 2: ARIMA – Teoría y validación de supuestos**  
**Objetivo:** Dominar la estructura matemática de ARIMA y su calibración.  
**Contenido:**  
1. **Descomposición de series temporales:**  
   - Tendencia, estacionalidad, residuales (gráficos ACF/PACF).  
2. **Parámetros (p, d, q):**  
   - Diferenciación para eliminar no estacionariedad (prueba Dickey-Fuller).  
   - Identificación visual de órdenes con correlogramas.  
3. **Metodología Box-Jenkins:**  
   - Identificación → Estimación → Diagnóstico.  
   - Herramientas: `statsmodels` (Python) o `forecast` (R).  

**Actividad:** Modelado ARIMA para temperatura mensual en Caucasia (1990-2023).  

---

#### **Módulo 3: Integración de variables meteorológicas en el modelo**  
**Objetivo:** Incorporar predictores climáticos al modelo ARIMA.  
**Contenido:**  
1. **ARIMAX y SARIMAX:**  
   - Extensión de ARIMA con variables exógenas (ej.: lluvias como predictor de casos de dengue).  
2. **Selección de variables:**  
   - Correlación cruzada entre dengue y clima (desfases temporales óptimos).  
   - Ejemplo: ¿Las lluvias de hace 2 meses impactan los casos actuales?  
3. **Manejo de multivariabilidad:**  
   - Colinealidad entre temperatura y humedad.  

**Actividad:** Construcción de modelo SARIMAX con datos reales:  
- Variable respuesta: Casos semanales de dengue (SIVIGILA).  
- Predictores: Lluvia acumulada (mm), temperatura promedio (°C).  

---

#### **Módulo 4: Validación y ajuste para predicciones robustas**  
**Objetivo:** Evaluar la capacidad predictiva del modelo en escenarios reales.  
**Contenido:**  
1. **Métricas de desempeño:**  
   - MAE, RMSE, MAPE aplicados a salud pública.  
   - Validación cruzada temporal (rolling window).  
2. **Diagnóstico de residuales:**  
   - Prueba Ljung-Box para autocorrelación.  
   - Normalidad de errores (Shapiro-Wilk).  
3. **Ajuste para sobredispersión:**  
   - Cuando los casos de dengue siguen distribución Poisson negativa (common en epidemias).  

**Actividad:** Comparación de modelos ARIMA vs. Prophet en datos 2020-2022.  

---

#### **Módulo 5: Implementación operativa y comunicación de resultados**  
**Objetivo:** Llevar el modelo a un entorno práctico para toma de decisiones.  
**Contenido:**  
1. **Despliegue del modelo:**  
   - Automatización con scripts (Python + Cron).  
   - Alertas tempranas: Umbrales de riesgo para Caucasia.  
2. **Visualización efectiva:**  
   - Mapas de calor con folium (correlación geoespacial).  
   - Dashboards en Power BI/Plotly.  
3. **Ética y limitaciones:**  
   - Sesgos en datos de subregistro.  
   - Comunicación a autoridades sanitarias: informe técnico no técnico.  

**Actividad Final:**  
- Proyecto integrador: Predecir brotes de dengue para 2024 usando datos 2023 como prueba.  
- Presentación simulada a la Secretaría de Salud de Antioquia.  

---

### **Herramientas Tecnológicas:**  
- **Lenguajes:** Python (Jupyter Notebooks) o R (RMarkdown).  
- **Librerías:** Pandas, statsmodels, Prophet, Matplotlib/Seaborn.  
- **Datos:**  
  - Meteorológicos: [IDEAM](https://www.ideam.gov.co/).  
  - Epidemiológicos: [SIVIGILA](https://www.ins.gov.co/).  

---

### **Evaluación:**  
- 40%: Proyecto integrador.  
- 30%: Ejercicios prácticos semanales.  
- 20%: Participación en foros de análisis de datos reales.  
- 10%: Quiz teóricos.  

---

### **Audiencia Ideal:**  
- Funcionarios de salud pública.  
- Estudiantes de estadística/epidemiología.  
- Investigadores en cambio climático y salud.  

--- 

¿Necesitas profundizar en algún módulo, ajustar contenidos, o incluir ejemplos más específicos? 😊
