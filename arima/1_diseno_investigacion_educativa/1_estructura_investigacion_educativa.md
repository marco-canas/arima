**Estructura para una Investigación Educativa bajo el Enfoque de Investigación-Acción Educativa (IAE)**  
**Título:** *"Impacto de enfoques pedagógicos innovadores (Aula Invertida, STEAMS y ABPP) en el aprendizaje del modelo ARIMA para predicción de dengue en Caucasia: Un estudio de caso con una candidata a bióloga"*  

---

### **1. Diagnóstico Inicial**  
**Objetivo:** Evaluar las competencias iniciales de la estudiante en:  
- Conocimientos estadísticos (series temporales, ARIMA).  
- Habilidades en Python (Pandas, statsmodels, Jupyter).  
- Comprensión del contexto epidemiológico del dengue en Caucasia.  

**Acciones:**  
- **Prueba diagnóstica:** Ejercicio práctico con datos ficticios para identificar gaps en modelado ARIMA.  
- **Encuesta:** Sobre experiencia previa con Aula Invertida y herramientas computacionales (VS Code/Colab).  
- **Revisión documental:** Análisis del anteproyecto de grado de la estudiante para alinear el curso con sus necesidades.  

---

### **2. Planificación de Ciclos de Acción**  
**Ciclo 1: Módulo 1 (Fundamentos)**  
- **Enfoques pedagógicos:**  
  - **Aula Invertida:** Videos sobre epidemiología del dengue y tutoriales de Pandas.  
  - **STEAMS:** Análisis de datos reales del IDEAM (lluvias) y SIVIGILA (dengue).  
  - **ABPP:** Proyecto inicial: "Relación histórica clima-dengue en Caucasia (2008-2023)".  
- **Herramientas:** Jupyter Notebooks en Colab (colaborativo) y VS Code (profundización).  

**Ciclo 2: Módulo 2-3 (ARIMA y variables meteorológicas)**  
- **Aula Invertida:** Tutoriales interactivos sobre ACF/PACF (usando `ipywidgets`).  
- **STEAMS:** Integración de código Python (statsmodels) y arte (visualizaciones con Plotly).  
- **ABPP:** Modelado SARIMAX con datos reales: "¿Cómo predecir dengue usando lluvias?".  

**Ciclo 3: Módulo 4-5 (Validación y despliegue)**  
- **Aula Invertida:** Simulaciones de validación cruzada temporal.  
- **STEAMS:** Dashboard interactivo en Plotly para autoridades sanitarias.  
- **ABPP:** Proyecto final: "Predicción de brotes 2024 y informe técnico".  

---

### **3. Implementación y Observación**  
**Recolección de datos:**  
- **Cuantitativos:**  
  - Puntajes en quizzes (ej: identificación de órdenes ARIMA).  
  - Métricas de modelos (RMSE, MAPE) en proyectos.  
- **Cualitativos:**  
  - Diario reflexivo de la estudiante (Bitácora en Google Docs).  
  - Grabaciones de sesiones de código en VS Code/Colab.  
  - Autoevaluación de habilidades blandas (trabajo en equipo virtual).  

**Instrumentos:**  
- Rúbricas para evaluar código (calidad, comentarios).  
- Plantilla de informe ABPP (estructura científica: introducción, métodos, resultados).  

---

### **4. Reflexión y Ajustes**  
**Análisis por ciclo:**  
- **Ciclo 1:**  
  - Si la estudiante tiene dificultades con Pandas → añadir tutoría en manipulación de DataFrames.  
- **Ciclo 2:**  
  - Si hay confusión en ACF/PACF → usar animaciones con `matplotlib.animation`.  
- **Ciclo 3:**  
  - Si el dashboard no es claro → incorporar feedback de usuarios ficticios (rol-playing).  

**Indicadores de éxito:**  
- La estudiante implementa un modelo ARIMAX funcional en su tesis.  
- Reduce el RMSE en ≥20% respecto a modelos iniciales.  

---

### **5. Evaluación Final**  
**Validación de hipótesis:**  
- **Triangulación:**  
  - Comparación pre-post en conocimientos estadísticos (prueba t de Student).  
  - Calidad del proyecto final vs. estándares de salud pública.  
  - Autopercepción de la estudiante sobre competencias adquiridas.  

**Resultados esperados:**  
- **Aceptación de hipótesis si:**  
  - La estudiante logra implementar ARIMA en su tesis con rigor metodológico.  
  - Reporta mayor confianza en el uso de Python y enfoques STEAMS.  

---

### **6. Ética y Consideraciones**  
- **Consentimiento informado:** La estudiante acepta uso de sus datos académicos.  
- **Privacidad:** Anonimización de datos epidemiológicos sensibles.  
- **Reconocimiento:** Crédito a colaboradores (ej: IDEAM, SIVIGILA).  

---

### **7. Productos Derivados**  
- **Para la estudiante:**  
  - Modelo ARIMA validado integrado en su tesis.  
  - Portafolio digital (GitHub) con Jupyter Notebooks.  
- **Para la investigación:**  
  - Artículo científico (ej: *Revista de Innovación Educativa en STEAM*).  
  - Plantillas reutilizables para cursos ABPP en salud pública.  

---

### **8. Referentes Teóricos (APA)**  
1. **Duval, R.** (1999). *Registros de representación semiótica y funcionamiento cognitivo*.  
2. **Wing, J. M.** (2006). Computational Thinking. *Communications of the ACM, 49*(3), 33-35.  
3. **Dickey, D. A., & Fuller, W. A.** (1979). Distribution of the Estimators for Autoregressive Time Series With a Unit Root. *Journal of the American Statistical Association, 74*(366), 427-431.  
4. **Box, G. E. P., & Jenkins, G. M.** (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day.  
5. **Freire, P.** (1970). *Pedagogía del Oprimido*. Herder & Herder.  

---

**Nota Final:**  
Este diseño integra los enfoques pedagógicos con herramientas tecnológicas específicas (VS Code, Colab, Jupyter), asegurando que la estudiante no solo aprenda ARIMA, sino que lo aplique directamente en su investigación, validando así la hipótesis desde un enfoque práctico y contextualizado.
