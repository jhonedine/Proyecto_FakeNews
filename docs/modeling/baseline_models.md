
# Reporte del Modelo Baseline

## Descripción del modelo

Para la construcción del modelo baseline en la tarea de clasificación de noticias como verdaderas o falsas, se decidió utilizar Doc2Vec como técnica de representación de texto. Esta elección se debe a la necesidad de capturar el contenido semántico y el contexto global de los documentos, lo cual es clave para distinguir patrones de veracidad o falsedad en el lenguaje utilizado en las noticias.
Doc2Vec permite representar cada documento del corpus como un vector en un espacio continuo, lo que facilita que un modelo de clasificación pueda aprovechar relaciones más complejas entre términos y frases, en comparación con métodos tradicionales como Bag of Words o TF-IDF, que únicamente consideran la frecuencia de las palabras sin atender al significado o la estructura de los textos.
Se estima que este modelo resulte adecuado para nuestro caso de estudio debido al tamaño considerable del corpus disponible (más de 44,000 documentos), lo que puede garantizar suficiente información para que Doc2Vec aprenda representaciones robustas y generalizables


## Variables de entrada

La única variable de entrada utilizada en el modelo es el texto completo de cada noticia, el cual corresponde al cuerpo del documento periodístico. Esta información textual fue transformada utilizando la técnica de embedding Doc2Vec, que convierte cada documento en un vector de características numéricas.
Estos vectores resultantes capturan relaciones semánticas y contextuales entre palabras y frases, permitiendo que el modelo de clasificación identifique patrones de redacción y contenido asociados a noticias verdaderas o falsas. A diferencia de representaciones como Bag of Words o TF-IDF, donde cada palabra es una dimensión, Doc2Vec produce una representación más compacta y significativa a nivel de documento.
En resumen, la entrada al modelo está compuesta por los vectores generados por Doc2Vec a partir del texto, los cuales capturan toda la información relevante del contenido del artículo de noticias.


## Variable objetivo

La variable objetivo utilizada en el modelo es label, la cual indica si una noticia es verdadera o falsa. Esta variable está codificada de forma binaria, donde:
•	1 representa una noticia falsa
•	0 representa una noticia verdadera
El modelo de clasificación fue entrenado para predecir esta variable a partir de la representación vectorial generada por Doc2Vec para cada documento, con el objetivo de detectar patrones de redacción, contenido y contexto que caractericen a las noticias falsas frente a las verdaderas.


## Evaluación del modelo

### Métricas de evaluación

Para evaluar el rendimiento del modelo baseline, se utilizaron las siguientes métricas:
•	Precision: Mide la proporción de predicciones positivas correctas frente al total de predicciones positivas realizadas, lo cual es útil para evaluar cuantos de los elementos clasificados como positivos realmente lo son.
•	Recall: Mide la proporción de verdaderos positivos identificados frente al total real de positivos. Lo cual es crucial cuando los falsos negativos tienen un alto costo, como en este caso para la detección de noticias falsas.
•	Accuracy: Representa el porcentaje de predicciones correctas sobre el total de caso evaluados.
Estas métricas fueron obtenidas a partir del conjunto de prueba, comparando las etiquetas reales con las predichas por el modelo.


### Resultados de evaluación

A continuación, se presentan los resultados obtenidos por el modelo baseline usando Doc2Vec como técnica de representación y clasificador supervisado.


| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.56      | 0.72   | 0.63     | 3508    |
| 1     | 0.56      | 0.39   | 0.46     | 3227    |
| **Accuracy** |        |        | **0.56** | 6735    |
| **Macro avg** | 0.56 | 0.56   | 0.55     | 6735    |
| **Weighted avg** | 0.56 | 0.56 | 0.55     | 6735    |




## Análisis de los resultados

El modelo baseline obtuvo una exactitud del 56%, lo que indica que su rendimiento es apenas superior al azar para un problema binario. 
Aunque logra detectar una parte considerable de las noticias verdaderas dado su resultado de la métrica recall con un 72%, su desempeño en la detección de noticias falsas es limitado con recall del 39%, lo cual es critico considerando que el objetivo es identificar este tipo de noticias.
Si bien la principal fortaleza del modelo esta en su capacidad para representar documentos completos permitiendo capturar algo del contexto y la semántica de las noticias, presenta varias debilidades como su bajo rendimiento en la detección de noticias falsas indicando dificultades para identificas de forma efectiva las diferencias semánticas entre noticias verdaderas y falsas. Asi mismo, se evidencia que el modelo aun no generaliza bien, probablemente por la necesidad de ajustar hiperparametros o utilizar embeddings mas sofisticados.


## Conclusiones

El modelo baseline utilizando Doc2Vec como técnica de representación de texto y un clasificador supervisado obtuvo un rendimiento modesto, con una exactitud del 56% y un F1-Score general de 0.46 para la clase de noticias falsas. Esto sugiere que, aunque el modelo puede distinguir parcialmente entre noticias verdaderas y falsas, su desempeño aún está lejos de ser óptimo.
Principales conclusiones:
•	El modelo baseline sirve como referencia inicial, estableciendo una línea base objetiva para evaluar mejoras posteriores.
•	Tiene mejor capacidad para identificar noticias verdaderas (recall 72%) que falsas (recall 39%), lo cual es una limitación importante dado el objetivo del problema.
•	La representación de texto mediante Doc2Vec, aunque superior al bag-of-words, puede no capturar suficientes relaciones contextuales complejas entre las palabras o frases clave que distinguen una noticia falsa de una real.
Posibles áreas de mejora:
1.	Representación de texto:
o	Usar técnicas más avanzadas como TF-IDF con n-gramas, Word Embeddings preentrenados.
2.	Modelos de clasificación:
o	Probar con modelos más robustos como XGBoost, Random Forest, o redes neuronales profundas.
3.	Optimización de hiperparámetros:
o	Ajustar los parámetros del modelo mediante técnicas como Grid Search o Random Search para encontrar la mejor configuración posible.


## Referencias

Chapman P. et al. (2000). CRISP-DM 1.0 Step-by-step data mining guide. The CRISP-DM consortium.

Mitchell, T. M. (1997). Machine Learning. McGraw-Hill.

Restrepo Calle, F. MLDS4 - U3 - Embeddings [Notebook de clase]. Universidad Nacional de Colombia, Facultad de Ingeniería.

