import pytest

def test_type():
    assert type(1) == int

def test_strs():
    assert 'pytest'.capitalize() == 'Pytest'

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
