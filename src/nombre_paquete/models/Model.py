
import pandas as pd
import numpy as np
import pandas as pd
import spacy
from unidecode import unidecode
import re
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import os
import pandas as pd
from IPython.display import display


from google.colab import drive
drive.mount('/content/drive')
fake = ('https://drive.google.com/uc?id=111J3U3feYR0ri6_DlP79CGRL-WsmLiF3')
true = ('https://drive.google.com/uc?id=18-_Mg6osJGrLmW3baJTgW_-LWcPCopCE')
df_fake = pd.read_csv(fake, sep=None, engine='python')
df_true = pd.read_csv(true, sep=None, engine='python')

df_fake['type'] = 0

df_true['type'] = 1

df = pd.concat([df_fake, df_true]).reset_index(drop=True)

##Limpieza de los Textos
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

text = df['text'].astype(str)
text = list(text)

corpus = list (map(preprocess, text))
#corpus = list(filter(lambda doc: len(doc), corpus))
display(corpus[:10])

##Entrenamiento del Modelo 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'], test_size=0.15, random_state=42)
X_train, X_tune, y_train, y_tune = train_test_split(X_train, y_train, test_size=0.1765, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer

TFIDF_vectorizer = TfidfVectorizer(max_features=512)
TFIDF_vectorizer.fit(X_train)
TFIDFembedding = TFIDF_vectorizer.transform(X_tune)
TFIDFembedding = pd.DataFrame(TFIDFembedding.toarray())
TFIDFembedding.columns = TFIDF_vectorizer.get_feature_names_out()

##Importar Modelo
# Librerías de apoyo para la visualización de resultados
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Dividir datos
X = df['text']
y = df['type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Entrenar modelo
model.fit(X_train, y_train)

##Pipelin
#Pipeline regresión logistica - TF-IDF
pipeline_lr_TFIDF = Pipeline([('vectorizer', TfidfVectorizer()),
                              ('classifier', LogisticRegression(class_weight="balanced"))])


#Pipeline random forest  - TF-IDF
pipeline_rf_TFIDF = Pipeline([('vectorizer', TfidfVectorizer()),
                        ('classifier', RandomForestClassifier(class_weight="balanced", max_samples= 100))])

lr_param_grid = {'vectorizer__max_features': [128,256,512],
                 'classifier__C': [0.01, 0.1, 1, 10]}

rf_param_grid = {'vectorizer__max_features': [128,256,512],
                 'classifier__criterion': ['gini', 'entropy'],
                 'classifier__n_estimators': [10,50,100]}

!pip install mlflow

import mlflow

command = """
mlflow server         --backend-store-uri sqlite:///tracking.db         --default-artifact-root file:mlruns         -p 5000 &
"""
get_ipython().system_raw(command)

!pip install pyngrok

token = "" # Agregue el token dentro de las comillas
os.environ["NGROK_TOKEN"] = token

!ngrok authtoken $NGROK_TOKEN

from pyngrok import ngrok
ngrok.connect(5000, "http")


mlflow.set_tracking_uri("http://localhost:5000")
experiment = mlflow.get_experiment_by_name("Fake_News")
exp_id = experiment.experiment_id if experiment else None

if exp_id is None:
  # Handle the case where the experiment doesn't exist, e.g., create it
  exp_id = mlflow.create_experiment(name="Fake_News", artifact_location="mlruns/")

#prueba 1

from sklearn.preprocessing import FunctionTransformer

# Wrapper para que sklearn acepte la función
preprocessor = FunctionTransformer(lambda x: list(map(preprocess, x)))

model = Pipeline([
    ('preprocess', preprocessor),
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Entrenar
model.fit(X_train, y_train)


with mlflow.start_run(
        run_name="LogisticRegression", experiment_id=exp_id
        ):
    model = Pipeline([
    ('preprocess', preprocessor),
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(max_iter=1000))
])
    model.fit(X_train, y_train)
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("accuracy", model.score(X_test, y_test))


model_name = 'FakeN'
model_version = 1
model = mlflow.pyfunc.load_model(f"models:/{model_name}/{model_version}")
display(model)

#Noticia Falsa
text1 = "" #Ingresar Texto

prediction = model.predict([text3])
print(prediction)

