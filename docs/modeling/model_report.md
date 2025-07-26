
# Reporte del Modelo Final

## Resumen Ejecutivo

Se presenta el problema de clasificación de noticias falsas. Este se aborda desde múltiples embeddings y clasificadores, siendo el mejor clasificador Regresión Logística con vectorizador TF-IDF. Con este se obtiene una precisión del 99.07%..

## Descripción del Problema

El proyecto busca abordar el creciente problema de la difusión masiva de noticias falsas a través de medios digitales, un fenómeno que ha generado desinformación, polarización social, y pérdida de confianza en las fuentes de información. En la actualidad, millones de usuarios consumen contenido en línea sin filtros ni verificación, lo que permite que noticias engañosas se propaguen rápidamente y tengan un impacto significativo en la opinión pública, procesos electorales, decisiones de salud, y otros aspectos críticos de la sociedad.

Desde la perspectiva del negocio y del dominio, se pretende desarrollar una solución automatizada basada en técnicas de procesamiento de lenguaje natural (NLP) que permita clasificar de forma eficiente noticias como verdaderas o falsas. Esto contribuiría a reducir el tiempo y los recursos dedicados a la verificación manual de información, facilitando la implementación de herramientas preventivas contra la desinformación en plataformas digitales y medios de comunicación.

## Descripción del Modelo

Este proyecto está fundamentado en la metodología CRISP-DM (Cross Industry Standard Process for Data Mining), la cual brinda un marco de trabajo bastante usado en los proyectos de ciencia de datos y machine learning. Este marco se plantea como un proceso iterativo que atraviesa diferentes etapas desde la comprensión del problema hasta el despliegue de la solución. Como lo menciona (CHAPMAN, 2000), este enfoque cíclico permite una retroalimentación constante y la adaptación a los desafíos que se encuentran a lo largo del desarrollo del proyecto.

## Evaluación del Modelo

Con las métricas seleccionadas, a continuación se presentan los resultados obtenidos:


| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 0.99   | 0.99     | 4710    |
| 1     | 0.99      | 0.99   | 0.99     | 4270    |
| **Accuracy**     |         |         | **0.99** | 8980    |
| **Macro avg**    | 0.99    | 0.99    | 0.99     | 8980    |
| **Weighted avg** | 0.99    | 0.99    | 0.99     | 8980    |

Este modelo presenta muy buenas métricas por lo que se considera una solución óptima que puede ser implementada.

## Conclusiones y Recomendaciones

El modelo implementado cumplió con las expectativas en cuanto a la precisión necesaria para alertar a las personas sobre noticias falsas que puedan recibir.
Las noticias falsas son un problema creciente en internet, por lo que a continuación se dan unas recomendaciones de aproximaciones futuras con los que puede robustecerse este modelo para ayudar a generar alertas al respecto:
- Implementación de modelos multimodales que permitan la transformación y análisis de imagenes y audios en redes sociales
- Identificación de enlaces sospechosos que pudieran incluir noticias falsas
- Incluir imagenes generadas por IA en las noticias falsas.

## Referencias

Chapman P. et al. (2000). CRISP-DM 1.0 Step-by-step data mining guide. The CRISP-DM consortium.

Mitchell, T. M. (1997). Machine Learning. McGraw-Hill.

Restrepo Calle, F. MLDS4 - U3 - Embeddings [Notebook de clase]. Universidad Nacional de Colombia, Facultad de Ingeniería.
