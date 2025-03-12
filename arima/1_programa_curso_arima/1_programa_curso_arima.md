```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Curso: Modelado de Series Temporales para Dengue en Caucasia</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f0f8ff; }
        h1, h2 { color: #2c3e50; }
        .module { background-color: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 0 10px #bdc3c7; }
        code { background-color: #e8f4f8; padding: 2px 5px; border-radius: 3px; }
        a { color: #3498db; }
    </style>
</head>
<body>
    <h1>🚀 Curso para Biólogos: Modelado Predictivo del Dengue en Caucasia</h1>
    <p><strong>Herramientas:</strong> Python, Jupyter Notebook, Pandas, Statsmodels, Plotly</p>

    <!-- Módulo 1 -->
    <div class="module">
        <h2>📌 Módulo 1: Introducción a Series Temporales y Dengue</h2>
        <h3>Objetivo:</h3>
        <p>Entender la relación clima-dengue usando datos reales de Caucasia.</p>
        <h3>Contenido:</h3>
        <ul>
            <li><strong>Sesión 1:</strong> Introducción a Jupyter y carga de datos (<code>pandas.read_csv</code>)</li>
            <li><strong>Sesión 2:</strong> Visualización interactiva con Plotly:
                <pre><code>import plotly.express as px
fig = px.line(df, x='Fecha', y='Casos_Dengue', color='Zona')
fig.show()</code></pre>
            </li>
        </ul>
    </div>

    <!-- Módulo 2 -->
    <div class="module">
        <h2>📊 Módulo 2: Modelado ARIMA con Variables Entomológicas</h2>
        <h3>Objetivo:</h3>
        <p>Construir modelos ARIMAX que integren:</p>
        <ul>
            <li>Indices pluviométricos</li>
            <li>Densidad de <em>Aedes aegypti</em> (huevos/trampa)</li>
        </ul>
        <h3>Código de Ejemplo:</h3>
        <pre><code>from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(df['Casos'], exog=df[['Lluvia', 'Huevos']], order=(1,1,1))
results = model.fit()
print(results.summary())</code></pre>
    </div>

    <!-- Módulo 3 -->
    <div class="module">
        <h2>🎯 Módulo 3: Validación y Aplicación Práctica</h2>
        <h3>Proyecto Final:</h3>
        <p>Predicción de brotes usando datos 2023 de Caucasia:</p>
        <ol>
            <li>Preprocesar datos meteorológicos y entomológicos</li>
            <li>Implementar modelo ARIMAX con <code>ipywidgets</code> para ajustar parámetros:
                <pre><code>widgets.interact(lambda p,d,q: ARIMA(..., order=(p,d,q)).fit().plot_predict(), 
                p=(0,2), d=(0,1), q=(0,2))</code></pre>
            </li>
        </ol>
    </div>

    <!-- Evaluación -->
    <div class="module">
        <h2>📝 Evaluación</h2>
        <table border="1">
            <tr><th>Tarea</th><th>Herramientas</th></tr>
            <tr><td>Quiz: Interpretación ACF/PACF</td><td>Matplotlib</td></tr>
            <tr><td>Proyecto: Predicción con datos reales</td><td>Statsmodels, Plotly</td></tr>
        </table>
    </div>

    <!-- Recursos -->
    <div class="module">
        <h2>🔗 Recursos</h2>
        <ul>
            <li><a href="https://github.com/min-salud-colombia/datos-dengue">Datos Abiertos Dengue Colombia</a></li>
            <li>Plantilla Jupyter: <a href="#">curso_arima_dengue.ipynb</a></li>
        </ul>
    </div>

    <!-- Footer -->
    <footer>
        <p>© 2024 Curso diseñado para el Instituto de Biología de la Universidad de Antioquia</p>
    </footer>
</body>
</html>
```

### Características del Curso:
1. **Enfoque Práctico**:  
   - Ejercicios con datos reales del municipio de Caucasia (Antioquia).  
   - Integración de variables entomológicas: ovitrampas, índices de Breteau.  

2. **Tecnologías Clave**:  
   - Visualizaciones animadas con `matplotlib.animation`:  
   ```python
   from matplotlib.animation import FuncAnimation
   def animate(i):
       ax.clear()
       ax.plot(df['Casos'][:i], color='red', label='Dengue')
       ax.legend()
   ani = FuncAnimation(fig, animate, frames=len(df))
   from IPython.display import HTML
   HTML(ani.to_jshtml())
   ```

3. **Aprendizaje Colaborativo**:  
   - Uso de GitHub para compartir notebooks y datos.  
   - Foros de discusión sobre modelos alternativos (SARIMA, Prophet).  

4. **Resultados Esperados**:  
   - Modelos predictivos aplicables a políticas públicas de salud.  
   - Publicación de resultados en formato Jupyter Book.  

🌦️ **¡A predecir brotes con ciencia y código!** 🦟📈


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