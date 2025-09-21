"""
Este módulo define la aplicación Flask principal.
Incluye la lógica para recibir datos desde un formulario web,
realizar operaciones matemáticas básicas y renderizar el resultado.
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)
app_port = int(os.environ.get("PORT", 5000))


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Vista principal de la aplicación.

    Muestra un formulario web para ingresar dos números y seleccionar
    una operación matemática. Procesa la solicitud POST, valida los datos,
    ejecuta la operación correspondiente (suma, resta, multiplicación
    o división) y renderiza la plantilla `index.html` con el resultado.
    """

    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]
            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"
    return render_template("index.html", resultado=resultado)
    
@app.route("/health")
def health():
    """
    Endpoint simple de verificación de estado (healthcheck).
    Retorna "OK" con código HTTP 200 si la app está funcionando.
    """
    return "OK", 200

if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True, port=app_port, host="0.0.0.0")  # Quita debug en producción
