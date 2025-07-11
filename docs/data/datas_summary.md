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

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, el tipo de variables, la presencia de valores faltantes y la distribución de las variables.
Como se mencionó anteriormente, el dataset contiene 23481  noticias falsas y 21417 noticias verdaderas. Estas tienen una clasificación de acuerdo a la temática que tratan, como se puede ver en la siguiente gráfica.
https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/8distribucion.JPG

![Temáticas por Tipo de noticia](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/7legibilidad.JPG)

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.
En los datos no se encontraron valores nulos y como se mostró previamente, se encontró que la data tienen un nivel de legibilidad alto.

## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.
La variable objetivo es la variable "label" que indica si la noticia es falsa o verdadera. 

## Variables individuales
A continuación se presenta el histograma de correlaciones de la representación de esta variables
![Histograma de correlaciones](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/4.JPG)

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.
## Variables individuales

## Ranking de variables
Se exploraron las noticias almacenadas en la variable "text" la cual es la única variable que compone el corpus del análisis a realizar. 

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.
A continuación se presenta el mapa de correlaciones para los textos.
![Mapa de correlaciones](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/3.JPG)
Este mapa de correlaciones nos permite ver que los embeddings trabajados para los textos análizados se encuentran por debajo de 0.4 por lo cual se puede concluir que no sufren de redundancia.

## Relación entre variables explicativas y variable objetivo
Como parte de la exploración, se presentan las nubes de palabras de las noticias falsas y verdaderas
![Nube noticias falsas](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/6wc.JPG)

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
![Nube noticias verdaderas](https://github.com/luise90/Proyecto_FakeNews-1/blob/master/imagenes/5wc.JPG)
