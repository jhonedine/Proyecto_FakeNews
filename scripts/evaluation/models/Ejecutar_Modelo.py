
!git clone https://github.com/jhonedine/Proyecto_FakeNews.git

%cd ./Proyecto_FakeNews/scripts/evaluation/models

!pip install -r requirements.txt

%cd ..


import mlflow

# Ruta al directorio donde están los archivos descargados
model_path = "models"

# Cargar el modelo
model = mlflow.pyfunc.load_model(model_path)

def predict_fake_news(model):
  """
  Takes user input for a news article and uses the provided model to predict
  if it is fake or true.

  Args:
    model: The loaded machine learning model for prediction.
  """
  noticia = input("Ingresa la noticia a verificar: ")
  prediction = model.predict([noticia])
  prediction = "Falsa" if prediction else "Verdadera"
  print(f"La Noticia Es : {prediction}")
