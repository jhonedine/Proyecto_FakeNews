code = '''
!pip install unidecode
from collections import defaultdict
import chardet
import numpy as np
import pandas as pd
import spacy
from unidecode import unidecode
import re
import seaborn as sns
import matplotlib.pyplot as plt

#Cargamos el Data Set

from google.colab import drive
drive.mount('/content/drive')

# Cargar archivos desde Google Drive
fake = 'https://drive.google.com/uc?id=111J3U3feYR0ri6_DlP79CGRL-WsmLiF3'
true = 'https://drive.google.com/uc?id=18-_Mg6osJGrLmW3baJTgW_-LWcPCopCE'

import pandas as pd

df_fake = pd.read_csv(fake, sep=None, engine='python')
df_true = pd.read_csv(true, sep=None, engine='python')

# Unir datasets y asignar etiquetas
df_fake['label'] = 1
df_true['label'] = 0
df = pd.concat([df_fake, df_true]).sample(frac=1).reset_index(drop=True)
df.head()


#Dividimos el Dataset 

df_fake['type'] = 0
df_true['type'] = 1
df = pd.concat([df_fake, df_true]).reset_index(drop=True)


# Lo Unificamos 


np.unique(df['subject'])


# Detectamos el Lenguaje 


!pip install langdetect
from langdetect import detect

idiomas = df['text'].sample(5).apply(lambda x: detect(str(x)))
print("Idiomas detectados en muestra:", idiomas.tolist())


""El corpus está compuesto por un total de 44.898 documentos, todos ellos redactados en idioma inglés.

En términos de almacenamiento, el tamaño total del conjunto de datos asciende a aproximadamente 178,5 MB.

No hay una relación entre documentos específicos, pero pueden encontrarse similitudes en temas o vocabulario, especialmente si se trata del mismo evento cubierto por distintas fuentes y al agruparlas por fechas o categorias, pueden surgir patrones utiles para el analisis.
"""

from collections import defaultdict
import chardet

def detect_string_encoding(text_sample):
    """Detecta la codificación de una muestra de texto"""
    if not isinstance(text_sample, str) or not text_sample.strip():
        return None
    try:
        result = chardet.detect(text_sample.encode('utf-8', errors='replace'))
        return result['encoding']
    except:
        return None

def check_dataframe_encoding(df):
    """
    Verifica un DataFrame de pandas para detectar problemas de codificación y datos ilegibles.

    Args:
        df (pd.DataFrame): DataFrame a verificar

    Returns:
        dict: Diccionario con los resultados del análisis
    """
    results = {
        'total_columns': len(df.columns),
        'total_rows': len(df),
        'text_columns': [],
        'non_text_columns': [],
        'encoding_problems': defaultdict(list),
        'illegible_data': defaultdict(list),
        'column_encodings': defaultdict(set),
        'encoding_stats': defaultdict(int)
    }

    for column in df.columns:
        # Verificar si la columna contiene texto
        if pd.api.types.is_string_dtype(df[column]):
            results['text_columns'].append(column)

            # Muestra aleatoria para análisis de codificación
            sample_size = min(100, len(df))
            text_sample = ' '.join(df[column].dropna().sample(sample_size, replace=True).astype(str))

            # Detectar codificación
            encoding = detect_string_encoding(text_sample)
            if encoding:
                results['column_encodings'][column].add(encoding)
                results['encoding_stats'][encoding] += 1

            # Verificar filas con posibles problemas
            for idx, value in df[column].items():
                if pd.isna(value):
                    continue

                try:
                    str(value).encode('utf-8').decode('utf-8')
                except UnicodeEncodeError as e:
                    results['encoding_problems'][column].append({
                        'row': idx,
                        'value': str(value)[:100] + '...' if len(str(value)) > 100 else str(value),
                        'error': f'UnicodeEncodeError: {str(e)}'
                    })
                except UnicodeDecodeError as e:
                    results['encoding_problems'][column].append({
                        'row': idx,
                        'value': str(value)[:100] + '...' if len(str(value)) > 100 else str(value),
                        'error': f'UnicodeDecodeError: {str(e)}'
                    })
                except Exception as e:
                    results['illegible_data'][column].append({
                        'row': idx,
                        'value': str(value)[:100] + '...' if len(str(value)) > 100 else str(value),
                        'error': f'Error: {str(e)}'
                    })
        else:
            results['non_text_columns'].append(column)

    return results


check_dataframe_encoding(df)


"""El corpus no contiene datos faltantes, ni tampoco se encuentran documentos vacios. Asi mismo, no se identifican problemas de codificacion, y se verifica que el corpus utiliza una codificacion UTF-8.
Este corpus unicamente contiene texto en ingles, sin presencia de otros idiomas."""

#Verificamos Nulos

df['text'].isna().sum()

# Verificamos Datos Faltantes 

missing_data = df.isnull().sum()
print("Datos faltantes:\n", missing_data)

# Problemas de codificación -> Mostramos texto aleatorio
ejemplo = df['text'].sample(1).values[0]
print("Ejemplo de texto:\n", ejemplo[:500])  # Primeros 500 caracteres



'''
with open("src/data_ingestion/Analisis_Exploratorio.py", "w") as f:
    f.write(code)
