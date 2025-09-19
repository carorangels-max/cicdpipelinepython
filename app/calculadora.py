# app/calculadora.py
def sumar(a, b):
    return a + b


def restar(a: float, b: float) -> float:
    """ "
    Resta dos numeros y devuelve el resultado.

    Args:
        a (float): El minuendo.
        b (float): El sustraendo.

    Returns:
        float: El resultado de restar `b` entre `a`.
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Divide dos números y devuelve el resultado.

    Args:
        a (float): El numerador.
        b (float): El denominador.

    Returns:
        float: El resultado de dividir `a` entre `b`.

    Raises:
        ZeroDivisionError: Si `b` es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
