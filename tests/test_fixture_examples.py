import pytest
from tempfile import NamedTemporaryFile


# ==================================================
# FIXTURE SIMPLES
# ==================================================

@pytest.fixture
def usuario():
    return {
        "nome": "Rafael",
        "idade": 25
    }


def test_nome_usuario(usuario):
    assert usuario["nome"] == "Rafael"


def test_idade_usuario(usuario):
    assert usuario["idade"] == 25


# ==================================================
# FIXTURE COM LISTA
# ==================================================

@pytest.fixture
def numeros():
    return [10, 20, 30, 40]


def test_soma(numeros):
    assert sum(numeros) == 100


def test_maior_valor(numeros):
    assert max(numeros) == 40


# ==================================================
# FIXTURE COM SETUP E TEARDOWN
# ==================================================

@pytest.fixture
def arquivo_temporario():
    arquivo = NamedTemporaryFile(mode="w+", delete=False)

    arquivo.write("Olá pytest!")
    arquivo.seek(0)

    yield arquivo

    arquivo.close()


def test_leitura_arquivo(arquivo_temporario):
    conteudo = arquivo_temporario.read()
    assert "pytest" in conteudo


# ==================================================
# FIXTURE DEPENDENTE
# ==================================================

@pytest.fixture
def produto():
    return {
        "nome": "Notebook",
        "preco": 3500
    }


@pytest.fixture
def produto_com_desconto(produto):
    produto["preco"] *= 0.9
    return produto


def test_desconto(produto_com_desconto):
    assert produto_com_desconto["preco"] == 3150


# ==================================================
# FIXTURE COM PARAMETRIZAÇÃO
# ==================================================

@pytest.fixture(params=[1, 2, 3, 4])
def numero(request):
    return request.param


def test_numero_positivo(numero):
    assert numero > 0


# ==================================================
# FIXTURE AUTOUSE
# ==================================================

@pytest.fixture(autouse=True)
def setup_global():
    print("\nExecutando setup automático")


def test_autouse_1():
    assert True


def test_autouse_2():
    assert 5 > 1


# ==================================================
# FIXTURE COM SCOPE MODULE
# ==================================================

@pytest.fixture(scope="module")
def conexao():
    print("\nCriando conexão...")
    return "Conexão Banco"


def test_conexao_1(conexao):
    assert conexao == "Conexão Banco"


def test_conexao_2(conexao):
    assert "Banco" in conexao


# ==================================================
# FIXTURE COM SCOPE SESSION
# ==================================================

@pytest.fixture(scope="session")
def configuracao():
    return {
        "ambiente": "teste",
        "versao": "1.0"
    }


def test_ambiente(configuracao):
    assert configuracao["ambiente"] == "teste"


def test_versao(configuracao):
    assert configuracao["versao"] == "1.0"


# ==================================================
# FIXTURE RETORNANDO OBJETO
# ==================================================

class Calculadora:
    def somar(self, a, b):
        return a + b

    def multiplicar(self, a, b):
        return a * b


@pytest.fixture
def calculadora():
    return Calculadora()


def test_soma_calculadora(calculadora):
    assert calculadora.somar(2, 3) == 5


def test_multiplicacao_calculadora(calculadora):
    assert calculadora.multiplicar(4, 5) == 20


# ==================================================
# FIXTURE COM DICIONÁRIO DE CONFIGURAÇÃO
# ==================================================

@pytest.fixture
def config_api():
    return {
        "host": "localhost",
        "porta": 8000,
        "debug": True
    }


def test_host(config_api):
    assert config_api["host"] == "localhost"


def test_debug(config_api):
    assert config_api["debug"] is True