"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
def test_resul_decimal():
    assert div(7.0, 2.0) == 3.5

def test_num_negativo():
    assert div (-5.0,-5.0) == 1

def test_division_cero():
    with pytest.raises(ZeroDivisionError) :
        assert div(5.0, 0)