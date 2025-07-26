
!git clone https://github.com/jhonedine/Proyecto_FakeNews.git

%cd ./Proyecto_FakeNews/scripts/evaluation/models

!pip install -r requirements.txt

%cd ..


import mlflow

# Ruta al directorio donde están los archivos descargados
model_path = "models"

# Cargar el modelo
model = mlflow.pyfunc.load_model(model_path)

noticia = input("Ingresa la noticia a verificar: ")
prediction = model.predict([noticia])
prediction = "Falsa" if prediction else "Verdadera"
print(f"La Noticia Es : {prediction}")

