import pytest


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