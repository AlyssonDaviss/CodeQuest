from abc import ABC

class Item(ABC):
    """
    Item que é utilizável pelo Player
    """
    def __init__(self, nome: str, descricao: str, empilhavel: bool):
        self.nome = nome
        self.descricao = descricao
        self.empilhavel = empilhavel

