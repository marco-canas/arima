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