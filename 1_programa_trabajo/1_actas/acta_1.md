A continuación te presento un diseño de acta en formato Markdown para la sesión del sábado 24 de mayo de 2025, enfocada en el monitoreo del cumplimiento del cronograma del trabajo de grado de la estudiante de Biología, Janis Zúñiga Ortega, en la línea de modelado ARIMA. Puedes usar este diseño como plantilla para futuras actas también.

# Acta de Asesoría de Trabajo de Grado
Sábado 24 de mayo de 2025

📌 Universidad de Antioquia — Campus Caucasia
📘 Programa: Biología
👩‍🎓 Estudiante: Janis Zúñiga Ortega
👨‍🏫 Asesor: Marco Julio Cañas Campillo
📂 Línea de investigación: Modelado ARIMA de series temporales climáticas y casos de dengue

Objetivo de la sesión
Dar inicio a la ejecución del cronograma de trabajo definido para la etapa de modelamiento ARIMA, abordando las actividades de la semana del 24 al 31 de mayo de 2025, según planificación.

Resumen de actividades programadas para la semana actual

* Cargar datos epidemiológicos y climáticos en Python.
* Verificar estructura semanal de los datos.
* Comprobar duplicados y valores nulos.
* Validar correspondencia entre fechas y semanas epidemiológicas.
* Documentar variables y unidades.

Desarrollo de la sesión

* Se revisó la base de datos climática y epidemiológica. Se confirmó que las fechas están estructuradas semanalmente y alineadas entre sí.
* La estudiante realizó carga de datos en Python (archivo .csv).
* Se aplicó código para la identificación de duplicados y valores faltantes. Se encontraron valores nulos en variables de humedad relativa para algunos meses de 2017.
* Se discutieron posibles estrategias de imputación de datos faltantes: media móvil o interpolación lineal.
* Se registraron todas las variables disponibles: temperatura promedio, humedad relativa, precipitación acumulada y número de casos de dengue.
* Se tomaron notas sobre unidades de medida y rangos observados.

Monitoreo del cumplimiento del cronograma

| Actividad                              | Cumplida | Observaciones                               |
| -------------------------------------- | -------- | ------------------------------------------- |
| Carga de datos                         | Sí       | Se utilizó pandas.read\_csv() correctamente |
| Verificación de estructura semanal     | No       | Confirmada alineación de fechas             |
| Revisión de duplicados y valores nulos | No       | Hay nulos en humedad relativa               |
| Validación de fechas epidemiológicas   | No       | Coinciden con semanas ISO                   |
| Documentación de variables y unidades  | No       | Se registró en cuaderno de trabajo          |

Acuerdos y compromisos

* Janis limpiará los datos faltantes utilizando interpolación lineal y documentará el proceso en su cuaderno de trabajo.
* Se preparará un notebook con visualizaciones exploratorias para la sesión del sábado 31 de mayo.
* La estudiante deberá conservar una copia limpia de los datos transformados.

Firma del asesor:

---

Marco Julio Cañas Campillo

Firma de la estudiante:

---

Janis Zúñiga Ortega

