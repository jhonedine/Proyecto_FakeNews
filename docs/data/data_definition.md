# Definición de los datos

## Origen de los datos

- Los textos provienen de un dataset público disponible en Kaggle;
"Fake and Real News", y contiene noticias clasificadas como verdaderas o falsas, específicamente diseñado para detección de noticias falsas.

Se puede usar la API de Kaggle o descargar los datos manualmente desde la página del proyecto.

## Especificación de los scripts para la carga de datos

- Para la carga de estos datos, se empleó el script mostrado a continuación:

```python
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
fake = ('https://drive.google.com/uc?id=111J3U3feYR0ri6_DlP79CGRL-WsmLiF3')
true = ('https://drive.google.com/uc?id=18-_Mg6osJGrLmW3baJTgW_-LWcPCopCE')
df_fake = pd.read_csv(fake, sep=None, engine='python')
df_true = pd.read_csv(true, sep=None, engine='python')
```

## Referencias a rutas o bases de datos origen y destino

- Los datos se encuentran almacenados en google drive.

Estos fueron extraidos de un repositorio de Kaggle y posteriormente almacenados.

Para la base de datos de destino, se plantea el versionamiento de estos datos a través de DVC en Google drive, en un espacio de almacenamiento público.

### Rutas de origen de datos

- A continuacipon se especifica la ubicación de los archivos de origen de los datos.
    'https://drive.google.com/uc?id=111J3U3feYR0ri6_DlP79CGRL-WsmLiF3'
    'https://drive.google.com/uc?id=18-_Mg6osJGrLmW3baJTgW_-LWcPCopCE'

- La estructura de los datos se presenta a continuación:   #Código Usado: df.info()
```python
    Index(['title', 'text', 'subject', 'date', 'type'], dtype='object')


<class 'pandas.core.frame.DataFrame'>
RangeIndex: 44898 entries, 0 to 44897
Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   title    44898 non-null  object
 1   text     44898 non-null  object
 2   subject  44898 non-null  object
 3   date     44898 non-null  object
 4   type     44898 non-null  int64 
dtypes: int64(1), object(4)
memory usage: 1.7+ MB
```
Se encuentra que en este dataset, no existen valores nulos. #Código usado: missing_data = df.isnull().sum() /n print("Datos faltantes:\n", missing_data)
```python
Datos faltantes:
 title      0
text       0
subject    0
date       0
type       0
dtype: int64
```
- Limpieza de los datos:
La selección de las técnicas de preprocesamiento del corpus puede variar en cada conjunto de datos. Recuerde que puede aplicar (no necesariamente todas) las técnicas generales vistas en el curso, tales como:

Tokenizacion: Para el proceso de Tokenizacion se trabajó con 2 tipos de embeddings. El primero fue TFIDF, de tipo frecuentista y Doc2Vec, de tipo semántico.
    Finalmente, por los resultados obtenidos en entrenamiento y prueba, se selección Doc2Vec.

Normalización de textos:

Filtrado de stopwords: Se realizó la remoción de stopwords en ingles de TfidfVectorizer. Esto no se aplicó en Doc2Vec para no afectar el sentido semántico de las noticias.

Limpieza con expresiones regulares: Se realizó la limpieza del texto y su normalización con el siguiente script.

```python
pat = re.compile(r"[^a-z ]")
spaces = re.compile(r"\s{2,}")
def preprocess(text, min_len=1, max_len=23):
    # Normalizamos el texto
    norm_text = unidecode(text).lower()

    # Extraemos tokens
    tokens = norm_text.split()

    # Filtramos palabras por longitud
    filtered_tokens = filter(
            lambda token: (
                len(token) >= min_len and
                len(token) <= max_len
                ),
            tokens
        )
    filtered_text = " ".join(filtered_tokens)
    # Eliminamos caracteres especiales
    clean_text = re.sub(pat, "", filtered_text)
    # Eliminamos espacios duplicados
    spaces_text = re.sub(spaces, " ", clean_text)
    return spaces_text.strip()
```
