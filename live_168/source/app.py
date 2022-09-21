from dataclasses import dataclass


@dataclass
class Tarefa:
    nome: str


class Coluna:
    def __init__(self, nome: str, tarefas=None) -> None:
        self.nome = nome
        self.tarefas: list[Tarefa] = tarefas or []

    def __getitem__(self, item):
        return self.tarefas[item]

    def insere_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)

    def remove_tarefa(self, tarefa: Tarefa):
        self.tarefas.remove(tarefa)

    def __repr__(self):
        return f"Colunas(nome='{self.nome}', tarefas={self.tarefas}"


class Quadro:
    def __init__(self, colunas=None) -> None:
        self.colunas: list[Coluna] = colunas or []

    def inserir_coluna(self, coluna: Coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa: Tarefa):
        self.colunas[0].insere_tarefa(tarefa)

    def mover(self, tarefa: Tarefa):
        if tarefa in self.colunas[0]:
            self.colunas[0].remove_tarefa(tarefa)
            self.colunas[1].insere_tarefa(tarefa)

    def __repr__(self):
        return f"Quadro(colunas={self.colunas}"
