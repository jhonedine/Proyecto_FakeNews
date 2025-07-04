# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto
Proyecto_FakeNews

## Objetivo
Desplegar en producción un modelo de NLP que permita clasificar automáticamente noticias como reales o falsas con base en su contenido textual.

## Trasfondo del Negocio
El presente proyecto está dirigido principalmente a entidades que enfrentan los desafíos de la desinformación digital, como lo son las plataformas de redes sociales, medios de comunicación, agencias de noticias, organizaciones de verificación de datos (fact-checking), y gobiernos. Estas entidades son los principales beneficiarios de una solución automatizada que permita identificar y clasificar contenido informativo como verdadero o falso.

El dominio del proyecto se ubica en el ámbito del periodismo digital, la tecnología de la información y la seguridad informativa, con un enfoque particular en el análisis de contenido textual. Dado el impacto social y político que puede tener la difusión de noticias falsas, este proyecto también puede ser de utilidad para organizaciones que promuevan la alfabetización mediática y la protección de la información veraz en entornos digitales.

El proyecto busca abordar el creciente problema de la difusión masiva de noticias falsas a través de medios digitales, un fenómeno que ha generado desinformación, polarización social, y pérdida de confianza en las fuentes de información. En la actualidad, millones de usuarios consumen contenido en línea sin filtros ni verificación, lo que permite que noticias engañosas se propaguen rápidamente y tengan un impacto significativo en la opinión pública, procesos electorales, decisiones de salud, y otros aspectos críticos de la sociedad.

Desde la perspectiva del negocio y del dominio, se pretende desplegar una solución basada en técnicas de procesamiento de lenguaje natural (NLP) probada que permite clasificar de forma eficiente noticias como verdaderas o falsas. Este proyecto contempla el despliegue en una interfaz de uso fácil un identificador de noticias falsas a través de su url.

## Dominio del Proyecto
Periodismo digital, seguridad informativa, alfabetización mediática y tecnología de la información.



## Metodología
Enfoque TDSP(Team Data Science Process):  El algoritmo seleccionado previamente fue Regresión logística posterior al uso de un embedding frecuentista TF-IDF, sin embargo, se realizará una nueva extracción de características, un modelamiento enfocado en los ajustes de parámetros de modelos como xgboost, randomfores y regresión logística y el tamaño de los vectores del embedding. Una vez actualizado el modelo, se procederá con el despliegue empleando herramientas como github para el control de versiones, DVC para gestión de datos y modelos, MLflow para el seguimiento de experimentos, y ngrok para exponer servicios localmente durante pruebas. Esto conducirá a la generación de un pipeline reproducible y escalable.


## Cronograma

| Etapa                                           | Duración estimada | Fechas                     |
|------------------------------------------------|-------------------|----------------------------|
| Entendimiento del negocio y carga de datos     | 1 semanas         | 26 de junio - 02 de julio   |
| Preprocesamiento y análisis exploratorio       | 1 semanas         | 03 de julio - 09 de julio |
| Modelamiento y extracción de características   | 1 semanas         | 10 de julio - 16 de julio |
| Despliegue                                     | 1 semanas         | 17 de julio - 20 de julio  |
| Evaluación y entrega final                     | 1 semanas         | 20 de julio - 26 de julio  |


## Equipo del Proyecto
- John Mendoza – Analista de datos y líder del proyecto
- Edison Molano – Analista de datos y líder del proyecto
- Luis Cardona – Analista de datos y líder del proyecto

## Presupuesto
Sin costo. Herramientas de código abierto y Google Colab

## Partes interesadas
- Plataformas sociales, fact-checkers, gobiernos, medios y ONGs

## Aprobaciones
- John Mendoza – Responsable del proyecto
- Fecha: 3 de julio de 2025
