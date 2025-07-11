# Reporte de Datos
El dataset trabajado contiene 44898 noticias clasificadas como verdaderas o falsas.
De estas 23481 son noticias falsas y 21417 son noticias verdaderas.

## Gráfico de Distribución 
![Distribución de Noticias](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/2.JPG)

Esta gráfica muestra la distribución de las noticias en el dataset.


Adicionalmente, se revisó la legibilidad de las noticias presentadas, encontrando que los textos son legibles de acuerdo con el índice flesh Reading easy, equivalente al indice Fernandez-Huerta.
Esto se puede apreciar en la siguiente imagen

![Legibilidad](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/7legibilidad.JPG)

En la gráfica azul encontramos las palabras reconocidas por Spacy y en la gráfica roja, el índice mencionado.


## Resumen general de los datos

Como se mencionó anteriormente, el dataset contiene 23481  noticias falsas y 21417 noticias verdaderas. Estas tienen una clasificación de acuerdo a la temática que tratan, como se puede ver en la siguiente gráfica.
https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/8distribucion.JPG

![Temáticas por Tipo de noticia](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/7legibilidad.JPG)

## Resumen de calidad de los datos

En los datos no se encontraron valores nulos y como se mostró previamente, se encontró que la data tienen un nivel de legibilidad alto.

## Variable objetivo

La variable objetivo es la variable "label" que indica si la noticia es falsa o verdadera. 

A continuación se presenta el histograma de correlaciones de la representación de esta variables
![Histograma de correlaciones](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/4.JPG)

## Variables individuales

Se exploraron las noticias almacenadas en la variable "text" la cual es la única variable que compone el corpus del análisis a realizar. 

A continuación se presenta el mapa de correlaciones para los textos.
![Mapa de correlaciones](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/3.JPG)
Este mapa de correlaciones nos permite ver que los embeddings trabajados para los textos análizados se encuentran por debajo de 0.4 por lo cual se puede concluir que no sufren de redundancia.

Como parte de la exploración, se presentan las nubes de palabras de las noticias falsas y verdaderas
![Nube noticias falsas](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/6wc.JPG)

![Nube noticias verdaderas](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/5wc.JPG)
