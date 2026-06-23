Aquí tienes los referentes teóricos y metodológicos en formato de lista científica, estructurados bajo las directrices de las normas **APA séptima edición**, organizados por sus respectivos pilares conceptuales (estadística matemática, computación/optimización y ecosistema de Python).

---

### 1. Pilares en Estadística Matemática (Teoría de la Regularización y Contracción)

* **LASSO (L1 Regularization):** Desarrollado por Robert Tibshirani en 1996. Introdujo la penalización de la norma L1 al vector de coeficientes, permitiendo que el estimador realice simultáneamente la selección de variables (fijando coeficientes redundantes exactamente en cero) y la contracción de parámetros para reducir la varianza debida a la alta dimensionalidad y la multicolinealidad.
* **Elastic Net:** Propuesto por Zou y Hastie en 2005 para superar las limitaciones de LASSO en escenarios con multicolinealidad extrema (como los rezagos climáticos). Elastic Net combina de forma convexa la penalización L1 (LASSO) y L2 (Ridge), forzando un "efecto de agrupación" (*grouping effect*) donde las variables altamente correlacionadas entran o salen juntas del modelo, estabilizando los coeficientes.

### 2. Fundamentos de Computación y Optimización Adaptativa

* **Validación Cruzada Integrada (CV):** La optimización de los hiperparámetros críticos ($\alpha$ y la proporción de mezcla L1/L2) se fundamenta en la validación cruzada k-fold (aplicada de manera adaptativa a las ventanas en el script). Este enfoque informático previene el sobreajuste (*overfitting*) al simular el rendimiento del modelo en múltiples subconjuntos de datos no observados, un estándar computacional validado por Stone (1974) y Geisser (1975).

### 3. Ecosistema de Computación Científica en Python

* **`scikit-learn`:** La implementación algorítmica de `LassoCV` y `ElasticNetCV` se basa en la infraestructura de optimización numérica de Scikit-learn (Pedregosa et al., 2011). Internamente, los solucionadores computacionales de esta librería emplean el algoritmo de **Descenso de Coordenadas Cíclicas** (*Coordinate Descent*), ideal por su eficiencia en la resolución de problemas de optimización con restricciones no diferenciables como la norma L1.

---

## Lista de Referencias en Formato APA (7.ª Edición)

Geisser, S. (1975). The predictive sample reuse method with applications. *Journal of the American Statistical Association*, *70*(350), 320-328. [https://doi.org/10.1023/A:1022632616235](https://www.google.com/search?q=https://doi.org/10.1023/A:1022632616235)

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning: Data mining, inference, and prediction* (2.ª ed.). Springer. [https://doi.org/10.1007/978-0-387-84858-7](https://doi.org/10.1007/978-0-387-84858-7)

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825-2830.

Stone, M. (1974). Cross-validatory choice and assessment of statistical predictions. *Journal of the Royal Statistical Society: Series B (Methodological)*, *36*(2), 111-133. [https://doi.org/10.1111/j.2517-6161.1974.tb00994.x](https://doi.org/10.1111/j.2517-6161.1974.tb00994.x)

Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical Society: Series B (Methodological)*, *58*(1), 267-288. [https://doi.org/10.1111/j.2517-6161.1996.tb02080.x](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x)

Zou, H., & Hastie, T. (2005). Regularization and variable selection via the elastic net. *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, *67*(2), 301-320. [https://doi.org/10.1111/j.1467-9868.2005.00503.x](https://doi.org/10.1111/j.1467-9868.2005.00503.x)