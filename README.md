# Tangelo-challenge
Este respositorio fue creado con el fin de responder a los requerimientos presentados en la prueba técnica de Tangelo.

A continuación se muestra un diseño de la solución expuesta.
![Descripción de la imagen](/design/diseño_solucion.png)

La solución se encuentra alojada bajo una función principal 'response_countries()', que se encuentra en el archivo `main.py`. Al ejecutarse, se conecta al API de paises (https://restcountries.com/), se procesa los datos retornados en la respuesta del API, los datos obtenidos son convertidos en dataframes y se calculan estadísticas sobre el tiempo de procesamiento, los dataframes son almacenados en una base de datos SQLite y además se genera un json sobre estos datos.

### Detalles de implementación
Hay que tener en cuenta que se hace uso de ciertas librerias. Para su correcta ejecución, es necesario installar las librerias que se encuentran en el archivo 'requirements.txt', bajo el comando `pip install -r requirements.txt`

Se hace uso de la libreria 'requests' para realizar una solicitud GET a la API de países (https://restcountries.com/v3.1/all), verificando el código de estado de la respuesta (de ser necesario se lanza excepción).

Para cada tiempo de procesamiento para crear una fila de un país, se usa time.perf_counter(), ya que tiene mayor precisión para tiempos de procesamiento cortos.

Los datos procesados en un dataframe, también son almacenados en una base de datos SQLite que se encuentra en la carpeta /database/, el nombre de la base de datos es 'tangelo-database.db'.
Los datos generados se guardan en un archivo JSON llamado 'data.json', donde se almacena la información extraida de los países  las estadísticas correspondientes a los tiempos de procesamiento de cada fila.

#### Otros

Se implementaron pruebas unitarias haciendo uso de la librería unittest, los cuales verifican el funcionamiento correcto de la función response_countries(), ayudando a garantizar la calidad del código. Para los tests, hay que tener en cuenta que se usaron 'mocks' proporcionados por la libreria unittest; esto es porque como se requiere hacer tests únicamente de la logica de la función, se hacen mocks de la conexión al API y a la base de datos, ya que son funcionalidades que hacen uso de librerias externas oficiales, no es necesario probar su funcionamiento.


Se pueden realizar mejoras en la manejo de excepciones, la optimización del código y la modularización para facilitar el mantenimiento y la escalabilidad.
