
# Prompt para el diseño de esta asesoría con DeepSeek  

Dame el diseño de acta de asesoría a la estudiante Janis Zúñiga, para su trabajo de grado adjunto donde trabajaremos hoy en la preparación de la defensa de lo que lleva la estudiante de su trabajo de tesis hasta hoy 25 de julio de 2025. Enfatiza en un grupo de posibles preguntas de los jurados y de cómo prepararse para exponen con seguridad y dominio conceptual. Este diseño de asesoría dámelo el lenguaje markdown. Agregale a las tareas a realizar el de agregar al dataset actual el atributo número de días de lluvia por semana epidemiológica.   



```markdown
# **ACTA DE ASESORÍA - TRABAJO DE GRADO**  
**Fecha:** 25 de julio de 2025  
**Estudiante:** Janis Zuñiga Ortega  
**Título del Proyecto:** *"Análisis de la variabilidad temporal del número de casos de dengue y su relación con variables climáticas en Caucasia, Antioquia"*  
**Asesor:** Guillermo L. Rúa-Uribe  
**Co-Asesor:** Marco Julio Cañas Campillo  

---

## **1. Objetivo de la Sesión**  
1. Preparación para la defensa del trabajo de grado.  
2. Revisión del avance actual (resultados, metodología y discusión).  
3. Simulación de preguntas de los jurados para fortalecer seguridad y dominio conceptual.  
4. Reflexión sobre habilidades blandas y aprendizaje desde los errores.  

---

## **2. Avance Actual (Resumen)**  
- **Metodología:**  
  - Modelos ARIMA/SARIMA/ARIMAX aplicados a series temporales (2008-2024).  
  - Variables climáticas integradas (temperatura, precipitación, humedad).  
  - **Nueva tarea:** Agregar al dataset el atributo *"número de días de lluvia por semana epidemiológica"* (fuente: IDEAM).  
- **Resultados Preliminares:**  
  - Correlación significativa entre temperatura y casos de dengue (rezago de 4-6 semanas).  
  - Patrón estacional identificado (picos en trimestres cálidos-lluviosos).  

---

## **3. Preparación para la Defensa**  

### **3.1. Estructura de la Presentación**  
1. **Introducción (2 min):** Contexto del dengue en Caucasia y justificación.  
2. **Metodología (3 min):** Enfoque ARIMA, fuentes de datos y procesamiento.  
3. **Resultados (3 min):** Gráficos clave (series temporales, residuos).  
4. **Discusión (2 min):** Relación clima-dengue vs. literatura.  
5. **Conclusiones (1 min):** Impacto en salud pública.  

### **3.2. Simulación de Preguntas de Jurados**  
#### **A. Preguntas Técnicas:**  
1. *"¿Cómo validó la estacionariedad de las series?"*  
   - **Respuesta:** "Prueba Dickey-Fuller aumentada (ADF) y diferenciación. Incluiremos días de lluvia para robustecer el modelo."  

2. *"¿Por qué no incluyó redes neuronales?"*  
   - **Respuesta:** "ARIMA es interpretable para variables climáticas (ej: Rúa-Uribe et al., 2013). Redes neuronales son nuestra próxima fase."  

#### **B. Preguntas Conceptuales:**  
3. *"¿Cómo explica el rezago entre lluvias y casos?"*  
   - **Respuesta:** "Ciclo de vida del *Aedes aegypti*: 2-3 semanas para desarrollo larval + incubación del virus."  

#### **C. Preguntas de Impacto:**  
4. *"¿Cómo aporta su modelo al sistema de alerta temprana?"*  
   - **Respuesta:** "Predice brotes con 4-6 semanas de anticipación, útil para fumigación focalizada."  

---

## **4. Habilidades Blandas: Aprendizaje desde los Errores**  
> *"Los errores son recordatorios de nuestra humanidad. Nos obligan a reflexionar, a crecer y a servir con mayor sabiduría. Como profesionales, padres o amigos, cada fallo es una oportunidad para:*  
> - **Aprender:** Un modelo mal ajustado enseña más que uno perfecto.  
> - **Empatizar:** Recordar nuestros tropiezos nos ayuda a guiar a otros.  
> - **Innovar:** Los datos 'ruidosos' a menudo esconden patrones valiosos."*  

**Ejercicio de reflexión (5 min):**  
- Compartir un error académico/personal y cómo transformó su enfoque.  

---

## **5. Tareas Pendientes**  
1. **Dataset:**  
   - Agregar *"días de lluvia/semana epidemiológica"* (IDEAM/NASA POWER).  
   - Validar homogeneidad con datos existentes.  
2. **Presentación:**  
   - Ensayar respuestas con temporizador (max. 12 min).  
   - Preparar slides de respaldo (pruebas ADF, matrices de correlación).  
3. **Reflexión:**  
   - Escribir un párrafo sobre cómo los errores han moldeado su crecimiento profesional.  

--- 

## **6. Compromisos**  
- **Estudiante:**  
  - Enviar dataset actualizado y reflexión antes del 30/07/2025.  
- **Asesor:**  
  - Retroalimentar presentación y ajustar sesión de simulación (05/08/2025).  

**Firma del Asesor:** _________________________  
**Firma del Estudiante:** _________________________  
``` 

### **Notas Clave:**  
- **Lenguaje:** Claro y técnico, pero con espacios para humanizar la ciencia.  
- **Innovación:** Destacar la adición de *días de lluvia* como variable clave.  
- **Profundidad:** Usar anexos para detalles técnicos (ej: parámetros ARIMA óptimos).  
- **Inspiración:** Frases en *cursiva* para conectar con el jurado a nivel emocional.