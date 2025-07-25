from argparse import ArgumentParser
import mlflow
mlflow.set_tracking_uri("http://localhost:5000")

def main():
    parser = ArgumentParser(
            description="CLI para modelo de detección de Noticias Falsas"
            )
    parser.add_argument("--text", type=str, required=True, help="Texto de la Noticia")
    args = parser.parse_args()
    model = mlflow.pyfunc.load_model("models:/FakeN/1")
    prediction = model.predict([args.text])[0]
    prediction = "Falsa" if prediction else "Verdadera"
    print(f"La Noticia Es : {prediction}")

if __name__ == "__main__":
    main()
