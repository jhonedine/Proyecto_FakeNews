code = '''
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

"""todos los textos deben ser tipo String"""
text = df['text'].astype(str)

"""Listamos Los textos Limpios y los filtramos por el Corpus"""

text = list(text)

corpus = list (map(preprocess, text))
#corpus = list(filter(lambda doc: len(doc), corpus))
display(corpus[:10])
'''
with open("src/data_ingestion/Limpieza_de_Datos.py", "w") as f:
    f.write(code)
