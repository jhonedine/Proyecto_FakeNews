# Informe de salida

## Resumen Ejecutivo

Este informe presenta los resultados del proyecto de clasificación de noticias falsas “Fake News” utilizando técnicas de procesamiento de lenguaje natural (NLP) y aprendizaje automático basado en un modelo de TF-IDF y regresión logística.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
  
**Entendimiento del negocio:**
En esta etapa definimos el objetivo del negocio, el cual es desplegar en producción un modelo de NLP que permita clasificar automáticamente noticias como reales o falsas con base en su contenido textual. Plasmando el trasfondo del negocio, describiendo su alcance junto con el cronograma de trabajo para llevarlo a cabo.
**Entendimiento y preparación de los datos:**
Se usa un dataset publico disponible en Kaggle; “Fake and Real News”, el cual contiene noticias clasificadas como verdaderas o falsas. Durante esta etapa se realiza una inspección del conjunto de datos identificando las variables y sus tipos para su posterior limpieza haciendo tokenizacion con Doc2Vec, normalización de textos y limpieza con expresiones regulares. Finalmente se analiza la cantidad de datos, su distribución para cada categoría y su calidad con la ayuda de gráficos como histogramas y nube de palabras.
**Modelamiento:**
Para la construcción del modelo baseline se decidio utilizar Doc2Vec como técnica de representación de texto y como clasificador XGBoost. Como variable de entrada utilizada en el modelo está el texto completo de cada noticia y como variable objetivo esta la variable label, la cual indica si una noticia es verdadera o falsa.
**Despliegue:**
Este modelo fue diseñado para despeglarse en un entorno de Google Colab utilizando MLflow para el seguimiento de experimentos y el registro de modelos. Asi mismo, se uso ngrok para conectar el servidor de MLflow con el libro de colab. Se exportaron los archivos generados por el modelo para que estos sean usados por usuario en diferentes entornos. 
**Evaluacion:**
-Se utilizaron metricas como Precision, Recall, Accuracy, tanto al modelo baseline como al modelo final. El modelo baseline obtuvo una exactitud del 56%, lo que indica que su rendimiento es apenas superior al azar para un problema binario. En cuanto al modelo final; su rendimiento fue superior al 99%, cumpliendo con las expectactivas en cuanto a la precisión necesaria para alertar a las personas sobre noticias falsas que puedan recibir.


- Evaluación del modelo final y comparación con el modelo base.
  
Se abordaron multiples embeddings y clasificadores obteniendo como resultado que el mejor clasificador es regresion Logistica con vectorizador TF-IDF arrojando una precision de 99.07%, un rendimiento muy superior al modelo baseline con el cual se uso Doc2Vec y XGBoost obteniendo un rendimiento modesto con una exactitud del 56% y un f1-score de 46% para la clase de noticias falsas. Esto finalmente, nos muestra que el modelo final mejoro su rendimiento en mas del 40% en comparacion al modelo baseline.

- Descripción de los resultados y su relevancia para el negocio.
  
El modelo implementado cumplió con las expectativas en cuanto a la precisión necesaria para alertar a las personas sobre noticias falsas que puedan recibir. Esto tiene un uso de gran importancia, dado que las noticias falsas son un problema creciente en internet y endiferentes fuentes de informacion, logrando de esta manera evitar problemas de desinformacion y todas las posibles causas que esto pueda resultar en la sociedad.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
  
Uno de los desafíos más relevantes fue el preprocesamiento adecuado de los textos, ya que las noticias contenían ruido como símbolos, errores ortográficos y estructuras gramaticales inconsistentes. Además, la elección del vectorizador y del clasificador impactó fuertemente en el desempeño, lo que requirió múltiples iteraciones para encontrar la mejor combinación. El despliegue en Google Colab con MLflow y ngrok también presentó retos técnicos relacionados con la persistencia del entorno y la conectividad.

- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
  
Se evidenció la importancia de una buena exploración y limpieza de datos antes de aplicar técnicas avanzadas de modelamiento. Aprendimos que las representaciones vectoriales como TF-IDF, aunque simples, pueden ofrecer muy buenos resultados cuando se combinan con modelos robustos como Regresion Logistica. También se reafirmó la necesidad de registrar correctamente los experimentos y modelos, lo cual MLflow facilitó. Por último, aprendimos que un despliegue exitoso requiere planificación, pruebas y herramientas adecuadas que se adapten al entorno.

- Recomendaciones para futuros proyectos de machine learning.
  
Es crucial comenzar con un baseline sencillo y medirlo bien antes de avanzar a modelos más complejos. Además, se recomienda evaluar diferentes técnicas de representación de texto y clasificadores, así como automatizar al máximo el pipeline de entrenamiento y despliegue. Documentar claramente cada etapa y sus resultados facilitará la colaboración y futuras mejoras. También es recomendable explorar opciones de despliegue más estables como servidores dedicados o servicios cloud.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
  
El modelo desarrollado tiene un impacto potencial en el combate contra la desinformación, al permitir detectar de manera automática y eficaz noticias falsas en plataformas digitales. Esto puede ser utilizado por medios de comunicación, plataformas sociales, gobiernos y usuarios en general para tomar decisiones informadas y frenar la propagación de contenido malicioso o engañoso.

- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.
  
Existen oportunidades para mejorar el modelo incorporando datos más actualizados y representativos, incluyendo noticias en otros idiomas o contextos culturales. También se puede explorar el uso de modelos de lenguaje más avanzados como BERT o transformers finetuneados para mejorar aún más el rendimiento. Finalmente, una integración con una API pública permitiría su uso en tiempo real por desarrolladores o usuarios finales.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.

Se logró desarrollar y desplegar un modelo de clasificación de noticias falsas con un rendimiento sobresaliente, alcanzando una precisión superior al 99% al utilizar TF-IDF combinado con Random Forest. Esto representa una mejora significativa frente al modelo base con Doc2Vec. Además, se implementó un entorno reproducible de experimentación y despliegue usando herramientas modernas como MLflow y ngrok.

- Conclusiones finales y recomendaciones para futuros proyectos.

El proyecto demostró la eficacia del enfoque CRISP-DM para abordar problemas de NLP en la vida real. Se recomienda continuar con la mejora iterativa del modelo, incorporar técnicas más recientes como embeddings contextuales y asegurar un entorno de producción más estable. La detección automática de noticias falsas no solo es viable, sino también crítica en el contexto digital actual.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
  
Agradecemos a todos los integrantes del equipo por su dedicación, compromiso y colaboración en cada etapa del proyecto. Su trabajo coordinado permitió superar los desafíos técnicos y alcanzar los objetivos propuestos.

- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
  
Agradecimientos especiales a la Universidad Nacional de Colombia y al cuerpo docente del diplomado por su acompañamiento, asesoría académica y recursos brindados para llevar a cabo este proyecto de manera exitosa.
