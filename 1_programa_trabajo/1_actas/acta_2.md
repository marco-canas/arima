# **Acta de Asesoría de Trabajo de Grado**  
**Sábado 31 de mayo de 2025**  

📌 **Universidad de Antioquia — Campus Caucasia**  
📘 **Programa:** Biología  
👩‍🎓 **Estudiante:** Janis Zúñiga Ortega  
👨‍🏫 **Asesor:** Marco Julio Cañas Campillo  
📂 **Línea de investigación:** Modelado ARIMA de series temporales climáticas y casos de dengue  

---

### **Objetivo de la sesión**  
Evaluar el avance en la limpieza y transformación de los datos, e iniciar las **visualizaciones exploratorias** de las series temporales (casos de dengue y variables climáticas) según lo planificado para la semana del 31 de mayo al 7 de junio de 2025.  

---

### **Resumen de actividades programadas para la semana actual**  
1. **Completar la limpieza de datos**:  
   - Imputación de valores nulos en humedad relativa (interpolación lineal).  
   - Documentar transformaciones aplicadas.  
2. **Generar visualizaciones exploratorias**:  
   - Gráficos de series temporales para casos de dengue y variables climáticas (temperatura, humedad, precipitación).  
   - Identificación visual de patrones (tendencias, estacionalidad, outliers).  
3. **Organizar resultados**:  
   - Guardar gráficos en formato adecuado para la tesis.  
   - Anotar observaciones relevantes en el cuaderno de trabajo.  

---

### **Desarrollo de la sesión**  
1. **Revisión de avances**:  
   - La estudiante presentó el código de Python para la imputación de datos faltantes (interpolación lineal en humedad relativa).  
   - Se verificó que los datos ahora estén completos y en formato semanal coherente.  
2. **Visualizaciones iniciales**:  
   - Se generaron gráficos preliminares con `matplotlib` y `seaborn`:  
     - Serie temporal de casos de dengue (2015–2025).  
     - Superposición de variables climáticas (ej. temperatura vs. dengue).  
   - **Hallazgos preliminares**:  
     - Posible estacionalidad anual en casos de dengue.  
     - Outliers en precipitación durante 2018 (¿evento climático extremo?).  
3. **Discusión metodológica**:  
   - Se acordó usar gráficos de descomposición (tendencia, estacionalidad, residual) para la próxima semana.  
   - Se recomendó aplicar transformaciones logarítmicas si hay heterocedasticidad.  

---

### **Monitoreo del cumplimiento del cronograma**  
| Actividad                              | Cumplida | Observaciones |  
|----------------------------------------|----------|---------------|  
| Limpieza de datos (imputación)         | Sí       | Interpolación lineal aplicada |  
| Gráficos de series temporales          | Parcial  | Pendiente análisis de outliers |  
| Documentación de patrones visuales     | No       | En progreso |  

---

### **Acuerdos y compromisos**  
1. **Para el 7 de junio**:  
   - Completar gráficos exploratorios (boxplots por año, descomposición de series).  
   - Exportar figuras en alta resolución (formato `.png` o `.svg`).  
   - Redactar un breve informe de hallazgos (máx. 2 páginas).  
2. **Próxima sesión**:  
   - Análisis de correlaciones (Pearson/Spearman) entre clima y dengue.  

---  

**Firma del asesor:**  
__________________________  
*Marco Julio Cañas Campillo*  

**Firma de la estudiante:**  
__________________________  
*Janis Zúñiga Ortega*  

---  
**Nota:** Se adjunta al acta el notebook de Python con los gráficos generados (archivo: `EDA_Dengue_Clima_Mayo2025.ipynb`).