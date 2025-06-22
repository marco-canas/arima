# **Acta de Asesoría de Trabajo de Grado**  
**Sábado 14 de junio de 2025**  

📌 **Universidad de Antioquia — Campus Caucasia**  
📘 **Programa:** Biología  
👩‍🎓 **Estudiante:** Janis Zúñiga Ortega  
👨‍🏫 **Asesor:** Marco Julio Cañas Campillo  
📂 **Línea de investigación:** Modelado ARIMA de series temporales climáticas y casos de dengue  

---

### **Objetivo de la sesión**  
Evaluar la distribución de los datos, determinar si son normales o no, y aplicar el análisis de correlación entre variables climáticas y casos de dengue.

---

### **Resumen de actividades programadas para la semana actual**  
1. Aplicar la prueba de normalidad de Shapiro-Wilk para cada variable.  
2. Seleccionar el método de correlación adecuado según la distribución.  
3. Calcular coeficientes de Pearson y Spearman.  
4. Visualizar las matrices de correlación con mapas de calor.  
5. Analizar rezagos visuales y anotar variables más correlacionadas.

---

### **Desarrollo de la sesión**

- Se aplicó la **prueba de Shapiro-Wilk** para determinar si las variables seguían una distribución normal.  
- Los resultados mostraron que **ninguna variable presentó distribución normal** (p-valor < 0.05 en todos los casos).  

#### **Resultados de la prueba de normalidad:**

| Variable                      | Estadístico W | p-valor | ¿Distribución Normal? |
|------------------------------|----------------|---------|------------------------|
| Casos                        | 0.8911         | 0.0000  | No                     |
| Temperatura media            | 0.8924         | 0.0000  | No                     |
| Temperatura máxima           | 0.8319         | 0.0000  | No                     |
| Temperatura mínima           | 0.9809         | 0.0274  | No                     |
| Humedad relativa             | 0.7787         | 0.0000  | No                     |
| Precipitación                | 0.9090         | 0.0000  | No                     |
| Velocidad del viento media   | 0.9800         | 0.0218  | No                     |
| Velocidad del viento máxima  | 0.9747         | 0.0053  | No                     |
| Velocidad del viento mínima  | 0.9571         | 0.0001  | No                     |

- Dado que los datos no siguen una distribución normal, se utilizaron **coeficientes de Spearman** (no paramétricos) junto con Pearson para propósitos comparativos.  
- Se generaron **mapas de calor** con las matrices de correlación.  
- Se analizaron **rezagos visuales** entre variables climáticas y casos de dengue.  
- Variables con mayor correlación observada:  
  - **Temperatura media** (Spearman > 0.6)  
  - **Precipitación** con rezago de 1–2 semanas (Pearson > 0.5)

---

### **Monitoreo del cumplimiento del cronograma**

| Actividad                               | Cumplida | Observaciones                                       |
|----------------------------------------|----------|-----------------------------------------------------|
| Prueba de normalidad                   | Sí       | Shapiro-Wilk aplicada correctamente                 |
| Cálculo de correlaciones               | Sí       | Pearson y Spearman aplicados                       |
| Gráficos de mapas de calor             | Sí       | Incluyen todas las variables analizadas             |
| Análisis visual de rezagos             | Sí       | Temperatura y precipitación con correlaciones altas |
| Registro de variables más asociadas    | Sí       | Documentadas en el cuaderno y archivo digital       |

---

### **Acuerdos y compromisos**

1. **Para el 21 de junio**:  
   - Realizar análisis de correlación cruzada con rezagos (cross-correlation).  
   - Determinar rezagos óptimos para modelos ARIMAX.  
   - Preparar una tabla de correlaciones significativas para incluir en la tesis.

2. **Próxima sesión**:  
   - Evaluar rezagos significativos y preseleccionar variables y desfases para modelamiento.

---

**Firma del asesor:**  
__________________________  
*Marco Julio Cañas Campillo*  

**Firma de la estudiante:**  
__________________________  
*Janis Zúñiga Ortega*  

---



