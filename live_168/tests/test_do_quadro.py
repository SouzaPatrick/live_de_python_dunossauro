from pytest import mark
from source.app import Coluna, Quadro, Tarefa


def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro: Quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0


def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(quadro: Quadro):
    quadro.inserir_coluna(Coluna(nome="A fazer"))
    assert len(quadro.colunas) == 1


def test_quando_inserir_a_coluna_a_fazer_ela_deve_estar_no_quadro(quadro: Quadro):
    quadro.inserir_coluna(Coluna(nome="A fazer"))
    assert quadro.colunas[0].nome == "A fazer"


def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(
    quadro_com_coluna: Quadro,
):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome="Dormir"))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 1


def test_quando_inserir_duas_tarefas_no_quadro_elas_devem_estar_na_primeira_coluna(
    quadro_com_coluna: Quadro,
):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome="Dormir"))
    quadro_com_coluna.inserir_tarefa(Tarefa(nome="Comer"))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 2


def test_quando_mover_cartao_ele_deve_ir_para_coluna_seguinte(
    quadro_com_colunas: Quadro,
):
    tarefa = Tarefa("Usar Mascara!")
    quadro_com_colunas.inserir_tarefa(tarefa=tarefa)

    quadro_com_colunas.mover(tarefa)

    assert tarefa in quadro_com_colunas.colunas[1]


def test_quando_mover_cartao_ele_deve_ser_removido_da_coluna_anterior(
    quadro_com_colunas: Quadro,
):
    tarefa = Tarefa("Usar Mascara!")
    quadro_com_colunas.inserir_tarefa(tarefa=tarefa)

    quadro_com_colunas.mover(tarefa)

    assert tarefa not in quadro_com_colunas.colunas[0]


@mark.exemplo
def test_exemplo_para_brincar(factory_boy_test):
    ...


@mark.parametrizado
@mark.parametrize("quadro_parametrizado", [[1]], indirect=True)  # xpto
def test_passando_parametros_para_fixture(quadro_parametrizado):
    ...
