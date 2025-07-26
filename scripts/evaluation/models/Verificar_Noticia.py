
#EJECUTAR MODELO

import mlflow

def cargar_modelo(ruta_modelo="models"):
    """Carga un modelo MLflow desde la ruta especificada."""
    print(f"Cargando modelo desde: {ruta_modelo}")
    model = mlflow.pyfunc.load_model(ruta_modelo)
    return model

def verificar_noticia(model):
    """Solicita al usuario una noticia y predice si es falsa o verdadera."""
    noticia = input("Ingresa la noticia a verificar: ")
    prediction = model.predict([noticia])
    resultado = "Falsa" if prediction[0] else "Verdadera"
    print(f"La Noticia Es: {resultado}")

def main():
    model = cargar_modelo()
    verificar_noticia(model)

if __name__ == "__main__":
    main()

