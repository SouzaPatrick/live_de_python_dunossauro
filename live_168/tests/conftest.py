from faker import Faker
from pytest import fixture
from source.app import Coluna, Quadro, Tarefa

fake: Faker = Faker()

import factory


class ColunaFactory(factory.Factory):
    class Meta:
        model = Coluna

    nome = factory.Faker("name")
    tarefas = [Tarefa("A")]


class QuadroFactory(factory.Factory):
    class Meta:
        model = Quadro

    colunas = ColunaFactory.build_batch(5)


@fixture
def factory_boy_test():
    return QuadroFactory.build()


@fixture
def quadro():
    return Quadro()


@fixture
def quadro_parametrizado(request):
    return Quadro()


@fixture
def quadro_com_coluna(quadro: Quadro):
    quadro.inserir_coluna(Coluna(fake.pystr()))
    return quadro


@fixture
def quadro_com_colunas(quadro_com_coluna: Quadro):
    quadro_com_coluna.inserir_coluna(Coluna(fake.pystr()))
    return quadro_com_coluna
