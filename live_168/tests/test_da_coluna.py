from source.app import Coluna


def test_coluna_dev_ter_um_nome():
    assert Coluna("Fazendo").nome == "Fazendo"
