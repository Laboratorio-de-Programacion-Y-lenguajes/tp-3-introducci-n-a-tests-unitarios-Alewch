"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_mul_cero():
    assert mul(3,0) == 0 

def test_mul_cero():
    assert mul(-1,-1) == 1 

def test_mul_posneg() :
    assert mul(-1,2) == -2

def test_mul_neutro():
    assert mul(5,1) == 5

def test_mul_cero():
    assert mul(3,0) == 0 

def test_mul_decimales():
    assert mul(3.10,1.10) == pytest.approx(3.41)
