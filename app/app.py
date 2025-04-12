# app/app.py
"""
Importa los módulos de Flask y las funciones de
operaciones básicas definidas en 'calculadora'.
"""
import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Este método gestiona la página principal: procesa formularios
    POST para realizar operaciones aritméticas, maneja errores
    y muestra el resultado.
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
    Endpoint para el health check del ALB.
    Retorna "OK" con estado 200 si la aplicación 
    está viva.
    """
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    # El puerto se puede configurar mediante PORT
    app_port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=app_port, host="0.0.0.0")
