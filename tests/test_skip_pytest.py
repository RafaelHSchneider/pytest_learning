"""
Exemplos de uso de skip no pytest
Execute com:
    pytest -v exemplo_skip.py
"""

import sys
import pytest


# --------------------------------------------------
# 1. Skip incondicional
# --------------------------------------------------
@pytest.mark.skip(reason="Exemplo de teste desabilitado")
def test_skip_simples():
    assert 1 == 1


# --------------------------------------------------
# 2. Skip condicional
# --------------------------------------------------
@pytest.mark.skipif(sys.version_info < (3, 12),
                    reason="Requer Python 3.12 ou superior")
def test_skip_condicional():
    assert True


# --------------------------------------------------
# 3. Skip dentro do teste
# --------------------------------------------------
def test_skip_dinamico():
    ambiente_pronto = False

    if not ambiente_pronto:
        pytest.skip("Ambiente não está pronto para o teste")

    assert True


# --------------------------------------------------
# 4. Skip por sistema operacional
# --------------------------------------------------
@pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="Teste não executa no Windows"
)
def test_apenas_linux():
    assert True


# --------------------------------------------------
# 5. Exemplo normal (não será ignorado)
# --------------------------------------------------
def test_normal():
    assert 2 + 2 == 4
