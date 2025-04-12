# app/calculadora.py
"""Módulo que proporciona funciones básicas de cálculo: suma, resta, multiplicación y división."""
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

"""Módulo que proporciona funciones básicas de cálculo: suma, resta, multiplicación y división."""
def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b

"""Módulo que proporciona funciones básicas de cálculo: suma, resta, multiplicación y división."""
def multiplicar(a, b):
    """Devuelve la multiplicacion de dos números."""
    return a * b

"""Módulo que proporciona funciones básicas de cálculo: suma, resta, multiplicación y división."""
def dividir(a, b):
    """Devuelve el resultado de dividir 'a' entre 'b'.
    Lanza una excepción ZeroDivisionError si 'b' es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b