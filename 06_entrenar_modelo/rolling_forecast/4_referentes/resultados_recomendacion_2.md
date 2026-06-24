Para sustentar académicamente la metodología aplicada en tu último script (donde la brecha del MAE se redujo drásticamente de $3.5\text{ vs }36.6$ a un equilibrado y realista **$5\text{ vs }7$** gracias a la regularización), necesitas citar los pilares teóricos subyacentes.

Aquí tienes los referentes bibliográficos clave estructurados bajo las normas **APA 7.ª edición**, clasificados por el componente metodológico que justifican en tu investigación:

---

### 1. Sobre la Regularización Lasso y Selección de Variables (Filtrado Previo)

*Justifica matemáticamente por qué redujiste los 144 rezagos climáticos iniciales forzando a los coeficientes irrelevantes a ser exactamente cero para evitar el sobreajuste.*

> **Referencia en la lista de bibliografía:**
> Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical Society: Series B (Methodological)*, *58*(1), 267–288. [https://doi.org/10.1111/j.2517-6161.1996.tb02080.x](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x)
> **Cita textual / paréntica en el texto:**
> (Tibshirani, 1996) o Tibshirani (1996)

> **Referencia en la lista de bibliografía:**
> Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning: Data mining, inference, and prediction* (2.ª ed.). Springer. [https://doi.org/10.1007/978-0-387-84858-7](https://doi.org/10.1007/978-0-387-84858-7)
> **Cita en el texto:**
> (Hastie et al., 2009)

---

### 2. Sobre la Estrategia de Validación Móvil (Rolling Forecast)

*Sustenta el uso de la validación "Walk-Forward" o Rolling Forecast como el método correcto para evaluar series temporales sin caer en filtración de datos históricos (data leakage).*

> **Referencia en la lista de bibliografía:**
> Hyndman, R. J., & Athanasopoulos, G. (2018). *Forecasting: Principles and practice* (2.ª ed.). OTexts. [https://otexts.com/fpp2/](https://otexts.com/fpp2/)
> **Cita en el texto:**
> (Hyndman & Athanasopoulos, 2018)

> **Referencia en la lista de bibliografía:**
> Tashman, L. J. (2000). Out-of-sample tests of forecasting accuracy: An essay and review. *International Journal of Forecasting*, *16*(4), 437–450. [https://doi.org/10.1016/S0169-2070(00)00065-0](https://www.google.com/search?q=https://doi.org/10.1016/S0169-2070(00)00065-0)
> **Cita en el texto:**
> (Tashman, 2000)

---

### 3. Sobre el Modelo ARIMAX (Series de Tiempo con Variables Exógenas)

*Sustenta la integración de los componentes Auto-regresivos (AR) y de Media Móvil (MA) junto a las covariables climáticas externas filtradas por Lasso.*

> **Referencia en la lista de bibliografía:**
> Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: Forecasting and control* (5.ª ed.). John Wiley & Sons.
> **Cita en el texto:**
> (Box et al., 2015)

---

### 4. Sobre la Métrica de Evaluación (MAE)

*Justifica la elección del Error Absoluto Medio (MAE) sobre el RMSE para medir el error en el conteo de casos epidemiológicos, al ser menos sensible a valores atípicos extremos aislados.*

> **Referencia en la lista de bibliografía:**
> Willmott, C. J., & Matsuura, K. (2005). Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance. *Climate Research*, *30*(1), 79–82. [https://doi.org/10.3354/cr030079](https://doi.org/10.3354/cr030079)
> **Cita en el texto:**
> (Willmott & Matsuura, 2005)

---

# Ejemplo de cómo redactar la justificación en tu artículo:

> "Para mitigar la maldición de la dimensionalidad provocada por la inclusión de 12 rezagos para cada variable meteorológica, se implementó un proceso de screening siguiendo los principios de regularización geométrica de **Tibshirani (1996)** mediante el operador Lasso. Este enfoque híbrido de alta dimensionalidad *(Lasso + ARIMAX)* permitió estabilizar los parámetros de la representación de espacio de estados de **Box et al. (2015)**. La evaluación del modelo se rigió bajo una arquitectura de *Rolling Forecast* recomendada por **Hyndman y Athanasopoulos (2018)** para evitar el sesgo de selección temporal. Como resultado, la brecha de error medida a través del MAO **(Willmott & Matsuura, 2005)** se redujo drásticamente, alcanzando un MAE de 5 en el set de entrenamiento y de 7 en testeo, demostrando una alta capacidad de generalización frente a los colapsos matemáticos observados en el modelo saturado inicial."