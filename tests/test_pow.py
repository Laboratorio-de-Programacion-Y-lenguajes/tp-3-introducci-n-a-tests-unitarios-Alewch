"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize ("base,exponente, resu",  
[ 
# Caso 1: Cualquier número elevado a 0 es 1 [cite: 425]
    (2, 0, 1), 
    (500, 0, 1),
    (-10, 0, 1)                          
])
def test_quart_cero(base,exponente,resu):
    assert pow(base,exponente) == resu



@pytest.mark.parametrize ("base,exponente, resu",
    [
    (7, 1, 7),
    (-3, 1, -3),
    ])
def test_elevado_uno(base,exponente,resu):
    assert pow(base, exponente) == resu
    

 
@pytest.mark.parametrize ("base,exponente, resu",[   
    (-2, 2, 4),
    (-2, 4, 16),
    ])
def test_base_neg(base,exponente,resu):
    assert pow(base, exponente) == resu


@pytest.mark.parametrize ("base,exponente, resu",[ 
    (9, 0.5, pytest.approx(3.0)),
    (2, 0.5, pytest.approx(1.41421356))
    ])
def test_exp_decimal(base, exponente, resu):
    assert pow(base, exponente) == resu