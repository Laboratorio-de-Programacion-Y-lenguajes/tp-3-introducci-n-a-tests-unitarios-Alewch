"""Tests para la función add(a, b) -> float."""

import unittest

import pytest

from src.calculator import add
from src.calculator import suma_numeros_negativos
from src.calculator import sum_negativo_positivo
from src.calculator import sumar_con_cero

# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected

@pytest.mark.parametrize("va, vb, resul", [
 (-1,-1,-2), 
 (0,-1,-1), 
 (1, 1, 2)   
])
def test_suma_numeros_negativos(va,vb,resul):
    assert suma_numeros_negativos(va, vb) == resul
    
@pytest.mark.parametrize("va, vb, resul", [
 (-1,-1,-2), 
 (0,-1,-1), 
 (1, 1, 2)   
])    
def test_sum_negativo_positivo(va, vb, resul):
    assert sum_negativo_positivo(va,vb) == resul

@pytest.mark.parametrize("va, vb, resul", [
 (-1,-1,-2), 
 (0,-1,-1), 
 (1, 1, 2)   
])
def test_sum_negativo_positivo(va, vb, resul):
    assert sum_negativo_positivo(va,vb) == resul


@pytest.mark.parametrize("va, vb, resul", [
 (0,-1,-1), 
 (0,-1,-1), 
 (0, 1, 1)   
])
def test_sumar_con_cero(va, vb, resul):
    assert sumar_con_cero(va,vb) == resul
