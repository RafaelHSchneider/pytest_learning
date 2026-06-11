import csv
from pathlib import Path

import pytest


def somar(a, b):
    return a + b


def carregar_dados_csv():
    """
    Carrega os dados do arquivo CSV e retorna
    uma lista de tuplas para o parametrize.
    """

    caminho_csv = Path(__file__).parent / "dados.csv"

    dados = []

    with open(caminho_csv, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            dados.append(
                (
                    int(linha["a"]),
                    int(linha["b"]),
                    int(linha["resultado"])
                )
            )

    return dados


@pytest.mark.parametrize(
    "a,b,resultado",
    carregar_dados_csv()
)
def test_soma(a, b, resultado):
    assert somar(a, b) == resultado