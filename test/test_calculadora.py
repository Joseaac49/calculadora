import pytest
from calculadora.operaciones import sumar, dividir, restar, multiplicar


# ------------------------
# SUMA
# ------------------------
def test_sumar_positivos(numeros):
    assert sumar(*numeros) == 12


def test_sumar_negativos():
    assert sumar(-2, -6) == -8


@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 5, 5),
])
def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado


# ------------------------
# RESTA
# ------------------------
@pytest.mark.parametrize("a,b,resultado", [
    (5, 3, 2),
    (3, 5, -2),
])
def test_restar(a, b, resultado):
    assert restar(a, b) == resultado


# ------------------------
# MULTIPLICACIÓN
# ------------------------
@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 6),
    (5, 0, 0),
])
def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b) == resultado


# ------------------------
# DIVISIÓN
# ------------------------
@pytest.mark.parametrize("a,b,resultado", [
    (6, 2, 3),
    (10, 5, 2),
])
def test_dividir(a, b, resultado):
    assert dividir(a, b) == resultado


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)