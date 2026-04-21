"""
TP2 (Módulo II) - Calculadora

Funciones puras para practicar testing unitario con pytest.
No debe haber input()/print() en este módulo.
"""

from __future__ import annotations

import math


def add(a: float, b: float) -> float:
    """Retorna a + b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Retorna a - b."""
    return a - b


def mul(a: float, b: float) -> float:
    """Retorna a * b."""
    return a * b


def div(a: float, b: float) -> float:
    """
    Retorna a / b.

    Raises:
        ZeroDivisionError: si b == 0
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def pow_(a: float, b: float) -> float:
    """Retorna a elevado a la potencia b."""
    return a**b


def sqrt(x: float) -> float:
    """
    Retorna la raíz cuadrada de x.

    Raises:
        ValueError: si x < 0
    """
    if x < 0:
        raise ValueError("sqrt() no admite números negativos")
    return math.sqrt(x)


def mean(values: list[float]) -> float:
    """
    Retorna el promedio de una lista de números.

    Raises:
        ValueError: si la lista está vacía
    """
    if not values:
        raise ValueError("mean() requiere una lista no vacía")
    return sum(values) / len(values)

def suma_numeros_negativos(num_one: int, num_two: int ) :    
    return num_one+num_two
    
def sum_negativo_positivo(num_one: int, num_two: int) :
    return num_one+num_two

def sumar_con_cero(num_one: int, num_two: int) :
    return num_one+num_two

def sumar_num_decimales(num_flone: float, num_fltwo: float):
    return num_flone+num_fltwo

    