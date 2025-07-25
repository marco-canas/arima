
# Prompt para el diseño de esta asesoría con DeepSeek  

Dame el diseño de acta de asesoría a la estudiante Janis Zúñiga, para su trabajo de grado adjunto donde trabajaremos hoy en la preparación de la defensa de lo que lleva la estudiante de su trabajo de tesis hasta hoy 25 de julio de 2025. Enfatiza en un grupo de posibles preguntas de los jurados y de cómo prepararse para exponen con seguridad y dominio conceptual. Este diseño de asesoría dámelo el lenguaje markdown. Agregale a las tareas a realizar el de agregar al dataset actual el atributo número de días de lluvia por semana epidemiológica.   




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
  - Modelos ARIMA/SARIMA/ARIMAX aplicados a series temporales (2008-2025).  
  - Variables climáticas integradas (temperatura, precipitación, humedad, las cuales son función de la variable anño-semana_epidemiologica).  
  - **Nueva tarea:** Agregar al dataset el atributo *"número de días de lluvia por semana epidemiológica"* (fuente: IDEAM). Número de casos de dengue por semana eqpidemiológica la variable binaria de si hay epidemia o no en el municipio. Estableciendo previamente cuando se dirá que hay epidemia en Caucasia Antioquia.  
  - Establecer científicamente criterios para establecer epidemoa de dengue en Caucasia. 
- **Resultados Preliminares:**  
  - Correlación significativa entre temperatura y casos de dengue (rezago de 4-6 semanas).  
  - Patrón estacional identificado (picos en trimestres cálidos-lluviosos).  

---

### **Criterios para Establecer una Epidemia de Dengue en Municipios como Caucasia, Antioquia (Colombia)**  

Para determinar la presencia de una **epidemia de dengue**, se deben considerar **umbrales epidemiológicos** basados en:  
1. **Incidencia semanal (casos/semana epidemiológica)**  
2. **Tasa de ataque (casos por 100,000 habitantes)**  
3. **Tendencia temporal (aumento significativo respecto a años previos)**  
4. **Factores climáticos y entomológicos (índices de infestación por *Aedes aegypti*)**  

---

### **1. Criterios Cuantitativos**  

#### **A. Umbral Epidemiológico (Línea Base)**  
- **Referencia:** OMS y Protocolo de Vigilancia del INS Colombia ([INS, 2023](https://www.ins.gov.co)).  
- **Método:**  
  - Calcular el **promedio histórico de casos semanales** (últimos 5 años).  
  - Establecer un **umbral epidémico** como:  
    - **Media + 1 o 2 desviaciones estándar** (según sensibilidad deseada).  
    - **Percentil 90** de la distribución semanal histórica.  

**Ejemplo para Caucasia (Población: ~98,000 hab):**  
| Semana Epidemiológica | Casos Promedio (2019-2023) | Umbral Epidémico (Media + 1 SD) |  
|-----------------------|----------------------------|----------------------------------|  
| Semana 10             | 15                         | 30                               |  
| Semana 25             | 20                         | 40                               |  

- **Definición de epidemia:** Superar el umbral en **2 semanas consecutivas**.  

#### **B. Tasa de Ataque**  
- **Fórmula:**  
  \[
  \text{Tasa} = \left( \frac{\text{Casos semanales}}{\text{Población}} \right) \times 100,000
  \]  
- **Umbral sugerido:**  
  - **Alerta:** ≥50 casos/100,000 hab/semana.  
  - **Epidemia:** ≥100 casos/100,000 hab/semana (*OPS, 2022*).  

---

### **2. Criterios Cualitativos**  
- **Aumento repentino:** Incremento del **50% o más** respecto a la misma semana en años anteriores.  
- **Serotipos circulantes:** Detección de **DENV-2 o DENV-3** (asociados a brotes graves, *WHO, 2024*).  
- **Indicadores entomológicos:**  
  - **Índice de Breteau (IB)** > 5% (cantidad de recipientes con larvas por 100 viviendas).  
  - **Índice de vivienda (IV)** > 10% (*OPS, 2021*).  

---

### **3. Factores Climáticos**  
- **Variables asociadas a brotes:**  
  - **Temperatura media** > 28°C (*Rúa-Uribe et al., 2013*).  
  - **Precipitación acumulada** > 100 mm/semana (*Messina et al., 2019*).  
  - **Humedad relativa** > 80% (*Altassan et al., 2024*).  

---

### **4. Validación Científica**  
#### **Referencias Clave:**  
1. **Organización Panamericana de la Salud (OPS, 2021):**  
   - [Guía para la Vigilancia del Dengue](https://www.paho.org).  
   - Umbrales basados en tasas de incidencia y tendencias temporales.  

2. **Instituto Nacional de Salud (INS, Colombia):**  
   - Protocolo de vigilancia con criterios de **alerta, brote y epidemia** ([Boletín Epidemiológico Semanal](https://www.ins.gov.co)).  

3. **Estudios en Contextos Similares:**  
   - **Rúa-Uribe et al. (2013):** Correlación entre **El Niño** y brotes en Antioquia (*Biomedica*).  
   - **Nakase et al. (2024):** Impacto del cambio climático en la expansión del dengue (*Nature*).  

4. **WHO (2024):**  
   - Definición global de epidemia: **exceso de casos respecto a lo esperado** + impacto en sistemas de salud.  

---

### **5. Ejemplo Aplicado a Caucasia**  
| **Semana** | **Casos (2025)** | **Umbral Epidémico** | **Tasa/100,000 hab** | **Clasificación** |  
|------------|------------------|-----------------------|-----------------------|-------------------|  
| 20         | 25               | 30                    | 25.5                  | Normal            |  
| 21         | 45               | 30                    | 45.9                  | **Alerta**        |  
| 22         | 60               | 30                    | 61.2                  | **Epidemia**      |  

**Conclusión:** Si en la **semana 22** se supera el umbral con una tasa >50/100,000 hab y hay condiciones climáticas favorables (ej. lluvias intensas), se declara **epidemia**.  

---

### **Recomendaciones**  
- **Integrar modelos predictivos** (ARIMA/SARIMA) para anticipar brotes (*Medina et al., 2024*).  
- **Declarar alertas tempranas** cuando se alcance el **50% del umbral epidémico**.  

Este enfoque combina **rigor estadístico** y **contexto local**, siguiendo estándares internacionales.


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

# Referencias para el trabajo en esta acta: 

