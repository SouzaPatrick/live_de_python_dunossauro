import sys

from pytest import mark
from source.jogo import brincadeira

"""_O teste é formado por 3 etapas (GWT):
- Given - Dado
- When - Quando
- Then - Então
"""


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada: int = 1  # Dado
    esperado: int = 1  # Dado
    resultado: int = brincadeira(entrada)  # Quando

    assert resultado == esperado  # Então


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == "queijo"


@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == "goiabada"


@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == "goiabada"


@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == "goiabada"


@mark.skip(reason="Pq ainda nao implementei")
@mark.goiabada
def test_quando_brincadeira_receber_1_entao_deve_retornar_None():
    assert brincadeira(20) == "goiabada"


@mark.parametrize("entrada", [5, 10, 20, 25, 35])
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == "goiabada"


@mark.parametrize("entrada", [3, 6, 9, 12, 18])
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == "queijo"


@mark.parametrizado
@mark.parametrize(
    "entrada, esperado", [(1, 1), (2, 2), (3, "queijo"), (4, 4), (5, "goiabada")]
)
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado


@mark.xfail(sys.platform == "linux", reason="Deve falhar no linux")
def test_xfail_linux():
    assert 1 == 2


@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)

    resultado = capsys.readouterr()

    assert resultado.out == "Entrei na brincadeira!\n"
