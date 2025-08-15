

Aquí tienes el borrador del **Acta Número 6** (15 de agosto de 2025) tomando en cuenta el formato y estilo de las actas anteriores, así como el programa del curso de ARIMA.
Incluye la **lista de verificación** de actividades programadas en las Actas 1–5 y una proyección de tareas para el ciclo siguiente del curso.

---

# **Acta de Asesoría de Trabajo de Grado**

**Viernes 15 de agosto de 2025**

 **Universidad de Antioquia — Campus Caucasia**
 **Programa:** Biología
 **Estudiante:** Janis Zúñiga Ortega
 **Asesor:** Marco Julio Cañas Campillo
 **Línea de investigación:** Modelado ARIMA/SARIMA/ARIMAX de series temporales climáticas y casos de dengue

---

## **Objetivo de la sesión**

* Revisar el cumplimiento acumulado de actividades de las Actas 1 a 5.
* Evaluar la preparación para iniciar el ajuste de modelos SARIMA (programado para agosto 16–23 según cronograma).
* Consolidar las variables y rezagos seleccionados para la fase estacional del modelado.
* Definir tareas específicas de preprocesamiento para los datos exógenos.

---

## **Lista de verificación de actividades previas (Actas 1–5)**

| Nº Acta | Fecha                                                     | Actividad principal                                                               | Estado        | Observaciones                                                             |
| ------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------- |
| 1       | 24 mayo 2025                                              | Carga y verificación de datos                                                     | ✅ Cumplida    | Nulos imputados, estructura semanal validada                              |
| 2       | 31 mayo 2025                                              | Visualizaciones exploratorias                                                     | ✅ Parcial     | Faltan boxplots y descomposición completa                                 |
| 3       | 25 julio 2025                                             | Preparación para defensa, criterios de epidemia y nueva variable “días de lluvia” | ⏳ En progreso | Variable días de lluvia aún no calculada completamente                    |
| 4       | 6 agosto 2025                                             | Pruebas de normalidad y correlaciones                                             | ✅ Cumplida    | Spearman y Pearson aplicados, variables más correlacionadas identificadas |
| 5       | 9 agosto 2025 *(no adjunta, reconstruida por cronograma)* | Determinación de parámetros SARIMA iniciales                                      | ⏳ En progreso | ACF/PACF estacionales en revisión                                         |

---

## **Desarrollo de la sesión**

1. **Revisión de pendientes:**

   * Confirmado que la imputación de datos y visualizaciones básicas están listas para anexar a la tesis.
   * Se evidenció retraso en la incorporación de la variable “días de lluvia por semana epidemiológica” y en el cálculo completo de ACF/PACF estacionales.
2. **Integración con cronograma ARIMA:**

   * El curso de modelado entra en la fase de determinación de parámetros SARIMA, por lo que es clave finalizar preprocesamientos exógenos antes del 20 de agosto.
3. **Decisiones metodológicas:**

   * Utilizar **auto\_arima** como referencia para valores iniciales (P,D,Q,s).
   * Mantener rezagos identificados en correlación cruzada para modelos SARIMAX posteriores.

---

## **Acuerdos y compromisos**

**Para el 21 de agosto de 2025:**

1. Calcular y documentar variable “días de lluvia por semana epidemiológica” (IDEAM y/o NASA POWER).
2. Finalizar boxplots y descomposición estacional de las series.
3. Estimar parámetros SARIMA iniciales: (P,D,Q,s) junto con (p,d,q).
4. Preparar tabla resumen de variables y rezagos seleccionados para SARIMAX.

---

## **Proyección de próxima fase (según programa del curso)**

* **Agosto 16 – Agosto 23:** Ajuste de modelos SARIMA y comparación inicial con ARIMA.
* **Agosto 23 – Agosto 30:** Validación de modelo SARIMA y selección final.

---

**Firma del asesor:**

---

*Marco Julio Cañas Campillo*

**Firma de la estudiante:**

---

*Janis Zúñiga Ortega*

---

Si quieres, puedo también prepararte este **Acta 6** en un formato Markdown con checklist interactivo (usando `- [ ]` y `- [x]`) para que lo uses directamente en GitHub y puedas marcar avances.
¿Quieres que lo deje así en versión con casillas marcables?
