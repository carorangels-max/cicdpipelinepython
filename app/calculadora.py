# app/calculadora.py
"""
Módulo calculadora.

Este módulo proporciona funciones básicas de operaciones matemáticas:
- sumar(a, b)
- restar(a, b)
- multiplicar(a, b)
- dividir(a, b)
"""


def sumar(a: float, b: float) -> float:
    """
    Suma dos numeros y devuelve el resultado.

    Args:
        a (float): Primer sumando.
        b (float): Segundo sumando.

    Returns:
        float: El resultado de sumar `a` y `b`.
    """
    return a + b


def restar(a: float, b: float) -> float:
    """
    Resta dos numeros y devuelve el resultado.

    Args:
        a (float): El minuendo.
        b (float): El sustraendo.

    Returns:
        float: El resultado de restar `b` entre `a`.
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """
    Multiplica dos números y devuelve el resultado.

    Args:
        a (float): El primer factor.
        b (float): El segundo factor.

    Returns:
        float: El producto de `a` por `b`.
    """
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
