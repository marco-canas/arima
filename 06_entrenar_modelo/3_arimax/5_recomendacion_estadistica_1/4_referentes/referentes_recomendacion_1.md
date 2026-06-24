Aquí tienes el contenido en formato compatible con un archivo Markdown (`.md`). He incluido los referentes de los pilares estadísticos clásicos (Modelos de Factores Dinámicos y PCA aplicado a series de tiempo), la validación econométrica de los criterios de información, y las librerías oficiales del ecosistema científico de Python que respaldan la ejecución técnica del algoritmo anterior.

Puedes copiar el siguiente bloque de código y guardarlo en un archivo con la extensión `.md` (por ejemplo, `referentes_teoricos.md`):

```markdown
# Referentes Teóricos y Metodológicos: Reducción Dimensional PCA y Modelos ARIMAX

Este documento compila el sustento teórico y los fundamentos computacionales que justifican la metodología híbrida implementada: la separación de la inercia autorregresiva de la enfermedad, la reducción dimensional del bloque climático mediante Análisis de Componentes Principales (PCA) y la selección óptima del modelo ARIMAX bajo múltiples criterios de información.

---

## 1. Fundamentos Estadísticos y de Reducción Dimensional

### El Bloque Climático como Factores Dinámicos
En la modelación de vectores como el *Aedes aegypti*, las variables meteorológicas de alta frecuencia presentan una correlación temporal cruzada e intrínseca (multicolinealidad). El uso de PCA sobre el bloque de regresores rezagados se sustenta en la teoría de **Modelos de Factores Dinámicos (DFM)**. Stock y Watson (2002) demostraron formalmente que una cantidad masiva de predictores temporales correlacionados puede colapsar en unos pocos componentes principales que retienen la variabilidad predictiva, eliminando problemas de sobreajuste y permitiendo estimaciones consistentes por máxima verosimilitud.

### Separación de la Inercia (La Regla de la Endogeneidad Sagrada)
La decisión metodológica de **no aplicar PCA** a la variable objetivo (`casos_dengue`) y sus rezagos se basa en la econometría de series temporales de Box y Jenkins (1970). La estructura autorregresiva modela la dinámica epidemiológica de contagio directo (la inercia endógena), mientras que las variables climáticas actúan estrictamente como perturbaciones exógenas exógenas ($X$). Mezclar ambas dinámicas en un espacio latente de PCA destruiría la autocorrelación parcial de la serie epidémica.

---

## 2. Criterios de Selección de Modelos (AIC, AICc, BIC, HQIC)

La evaluación automática implementada mediante el bucle multi-criterio se fundamenta en las siguientes teorías de penalización paramétrica:
* **AIC y AICc:** Akaike (1974) formuló el criterio basado en la entropía de Kullback-Leibler. Hurvich y Tsai (1989) desarrollaron la corrección para muestras pequeñas ($AICc$), crucial en particiones temporales donde el número de parámetros ajustados ($p, q$ + regresores exógenos) es alto en relación al tamaño de la muestra de entrenamiento.
* **BIC:** Schwarz (1978) diseñó una penalización más estricta basada en el enfoque bayesiano, consistente cuando se busca el modelo "verdadero" a medida que la muestra tiende al infinito.
* **HQIC:** Hannan y Quinn (1979) propusieron una alternativa con una tasa de penalización basada en logaritmos iterados, balanceando el conservadurismo del BIC y la sensibilidad del AIC.

---

## 3. Sustento del Ecosistema de Computación Científica en Python

La implementación en código se apoya firmemente en los estándares de la comunidad científica de Python:
* **`scikit-learn`:** Pedregosa et al. (2011) provee la infraestructura para el escalamiento estándar estricto (crucial para que variables con distintas unidades no sesguen el PCA) y la descomposición matricial mediante SVD truncada.
* **`statsmodels` y `pmdarima`:** Seabold y Perktold (2010), junto al desarrollo derivado de Smith (2017), implementan los algoritmos de estimación de espacio de estados (SARIMAX) que permiten la alimentación directa de matrices exógenas de alta densidad optimizadas mediante el método de optimización Quasi-Newton L-BFGS.

---

## Referencias en Formato APA (7.ª Edición)

Akaike, H. (1974). A new look at the statistical model identification. *IEEE Transactions on Automatic Control*, *19*(6), 716-723. https://doi.org/10.1109/TAC.1974.1100705

Box, G. E., & Jenkins, G. M. (1970). *Time series analysis: Forecasting and control*. Holden-Day.

Hannan, E. J., & Quinn, B. G. (1979). The determination of the order of an autoregression. *Journal of the Royal Statistical Society: Series B (Methodological)*, *41*(2), 190-195. https://doi.org/10.1111/j.2517-6161.1979.tb01072.x

Hurvich, C. M., & Tsai, C. L. (1989). Regression and time series model selection in small samples. *Biometrika*, *76*(2), 297-307. https://doi.org/10.1093/biomet/76.2.297

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825-2830.

Schwarz, G. (1978). Estimating the dimension of a model. *The Annals of Statistics*, *6*(2), 461-464. https://doi.org/10.1214/aos/1176344136

Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and statistical modeling with Python. En *Proceedings of the 9th Python in Science Conference* (pp. 92-96). https://doi.org/10.25080/Majora-92bf1922-011

Smith, T. G. (2017). *Pmdarima: ARIMA time series forecasting for Python* (Versión 2.0.0) [Software de computación]. https://github.com/alkaline-ml/pmdarima

Stock, J. H., & Watson, M. W. (2002). Forecasting using principal components from a large number of predictors. *Journal of the American Statistical Association*, *97*(460), 1167-1179. https://doi.org/10.1198/016214502388618960

```