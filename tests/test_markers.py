import pytest
import sys

# ----------------------------------------
# Smoke Tests
# ----------------------------------------

@pytest.mark.smoke
def test_login():
    assert True


@pytest.mark.smoke
def test_logout():
    assert True


# ----------------------------------------
# Regression Tests
# ----------------------------------------

@pytest.mark.regression
def test_calculo_desconto():
    assert 100 - 10 == 90


@pytest.mark.regression
def test_calculo_frete():
    assert 20 + 5 == 25


# ----------------------------------------
# API Tests
# ----------------------------------------

@pytest.mark.api
def test_get_users():
    status_code = 200
    assert status_code == 200


@pytest.mark.api
def test_create_user():
    status_code = 201
    assert status_code == 201


# ----------------------------------------
# Database Tests
# ----------------------------------------

@pytest.mark.database
def test_insert_user():
    registros_afetados = 1
    assert registros_afetados == 1


@pytest.mark.database
def test_delete_user():
    registros_afetados = 1
    assert registros_afetados == 1


# ----------------------------------------
# Slow Tests
# ----------------------------------------

@pytest.mark.slow
def test_processamento_longo():
    resultado = sum(range(1000000))
    assert resultado > 0


# ----------------------------------------
# Múltiplos Markers
# ----------------------------------------

@pytest.mark.api
@pytest.mark.smoke
def test_healthcheck():
    status_code = 200
    assert status_code == 200

# ----------------------------------------
# Xfail
# ----------------------------------------

@pytest.mark.xfail(reason="Bug ainda não corrigido")
def test_divisao_por_zero():
    assert 10 / 0 == 0

@pytest.mark.regression
@pytest.mark.xfail(reason="Erro conhecido no cálculo de desconto")
def test_desconto_promocional():
    assert calcular_desconto(100) == 80

@pytest.mark.xfail(
    sys.platform.startswith("win"),
    reason="Funcionalidade ainda não funciona no Windows"
)
def test_recurso_linux():
    assert True

@pytest.mark.xfail(
    raises=ZeroDivisionError,
    reason="Ainda não tratamos divisão por zero"
)
def test_divisao():
    resultado = 10 / 0
    assert resultado == 0