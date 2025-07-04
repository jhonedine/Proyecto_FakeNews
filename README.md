# 🧠 Proyecto Aplicado: Clasificación de Noticias Falsas

Este proyecto tiene como objetivo desarrollar un modelo de aprendizaje automático que permita identificar noticias falsas (fake news) utilizando técnicas de procesamiento de lenguaje natural (NLP). Está orientado a combatir la desinformación digital y apoyar a entidades como medios de comunicación, plataformas sociales, agencias de verificación y gobiernos.

---

## 📌 Objetivo

Construir un clasificador binario (verdadero/falso) de noticias en texto, basado en un dataset público, que automatice la verificación preliminar del contenido textual.

---

## 📊 Dataset

Se utiliza el dataset [Fake and Real News Dataset (Kaggle)](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset), que contiene dos archivos CSV:
- **Fake.csv**: Noticias etiquetadas como falsas
- **True.csv**: Noticias etiquetadas como verdaderas

Se combinan en un único DataFrame con una columna `label`:
- `0`: Noticia falsa
- `1`: Noticia verdadera

---

## 🧱 Estructura del Repositorio

```bash
├── docs/
│   ├── business_understanding/
│   │   ├── business_understanding.md
│   │   └── methodology.md
│   └── data_dictionary/
│       └── data_dictionary.md
├── src/
│   └── data_ingestion/
│       └── load_data.py
├── data/
│   ├── Fake.csv
│   └── True.csv
└── README.md
```

---

## ⚙️ Tecnologías y Herramientas

- Python 3.10+
- Google Colab
- Pandas, scikit-learn
- Kaggle API
- Git y GitHub

---

## 🛠️ Metodología de Trabajo

- Preprocesamiento de texto: limpieza, tokenización, vectorización
- Modelos: Naive Bayes, Regresión Logística, Redes Neuronales
- Validación cruzada y evaluación con métricas de precisión y recall
- Documentación y control de versiones semanal con GitHub

---

## 📅 Cronograma
| Etapa                                           | Duración estimada | Fechas                     |
|------------------------------------------------|-------------------|----------------------------|
| Entendimiento del negocio y carga de datos     | 1 semanas         | 26 de junio - 02 de julio   |
| Preprocesamiento y análisis exploratorio       | 1 semanas         | 03 de julio - 09 de julio |
| Modelamiento y extracción de características   | 1 semanas         | 10 de julio - 16 de julio |
| Despliegue                                     | 1 semanas         | 17 de julio - 20 de julio  |
| Evaluación y entrega final                     | 1 semanas         | 20 de julio - 26 de julio  |
---

## 🤝 Contribuciones y Stakeholders

- **Líder del proyecto**: Edison Molano -- John Mendoza --Luis Cardona
- **Stakeholders**: plataformas sociales, gobiernos, fact-checkers, periodistas

---

## 📢 Licencia

Este proyecto usa datos públicos con fines educativos. No se usa para producción comercial.
