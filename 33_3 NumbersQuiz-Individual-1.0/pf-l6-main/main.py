from flask import Flask, jsonify
import math

app = Flask(__name__)

# Base de datos de trivia de números (puedes expandirla)
trivia_datos = {
    7: "El número 7 es considerado de la suerte en muchas culturas.",
    13: "El número 13 es asociado con la mala suerte en la superstición occidental, conocido como triskaidekafobia.",
    42: "Según la Guía del Autoestopista Galáctico, la respuesta al sentido de la vida, el universo y todo es 42.",
    100: "El número 100 se conoce como un centenar y es la base del sistema de porcentajes.",
}

# --- Rutas de la API ---


@app.route("/")
def inicio():
    """Ruta de bienvenida."""
    return "¡Bienvenido a la API local de Trivia de Números! Prueba con la ruta /trivia/<numero>."


@app.route("/trivia/<int:numero>")
def obtener_trivia(numero):
    """Obtiene un dato de trivia para el número dado."""
    # Buscar el dato en nuestra base de datos
    dato = trivia_datos.get(numero)

    # Si el número no está en nuestra base de datos, buscamos uno matematico
    if dato is None:
        if numero % 2 == 0:
            dato = f"El número {numero} es un número par."
        else:
            dato = f"El número {numero} es un número impar."

        if numero > 1 and all(
            numero % i != 0 for i in range(2, int(math.sqrt(numero)) + 1)
        ):
            dato += f" Además, {numero} es un número primo."

    # Si el dato existe, devolverlo en formato JSON
    if dato:
        return jsonify({"numero": numero, "dato": dato})
    else:
        # Si no se encontró ningún dato, devolver un error 404 (No Encontrado)
        return jsonify({"error": "No hay datos de trivia para este número."}), 404


# --- Ejecutar la aplicación ---

if __name__ == "__main__":
    app.run(debug=True)
