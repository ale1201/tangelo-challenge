# Tangelo-challenge
Este respositorio fue creado con el fin de responder a los requerimientos presentados en la prueba técnica de Tangelo.

A continuación se muestra un diseño de la solución expuesta.
![Descripción de la imagen](/design/diseño_solucion.png)

La solución se encuentra alojada bajo una función principal 'response_countries()', que se encuentra en el archivo `main.py`. Al ejecutarse, se conecta al API de paises (https://restcountries.com/), se procesa los datos retornados en la respuesta del API, los datos obtenidos son convertidos en dataframes y se calculan estadísticas sobre el tiempo de procesamiento, los dataframes son almacenados en una base de datos SQLite y además se genera en json sobre estos datos.

### Detalles ded implementación
Hay que tener en cuenta que se hace uso de ciertas librerias. Para su correcta ejecución, es necesario installar las librerias que se encuentran en el archivo 'requirements.txt', bajo el comando `pip install -r requirements.txt`
