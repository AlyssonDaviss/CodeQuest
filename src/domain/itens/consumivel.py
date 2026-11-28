from item import Item

class Consumivel(Item):
    """
    Item que pode ser consumido pelo Player
    """
    def __init__(self, nome: str, descricao: str, empilhavel: bool, efeito: int, quantidade: int):
        super.__init__(nome= nome, descricao= descricao, empilhavel= empilhavel)
        self.efeito = efeito
        self.quantidade = quantidade

    def usar(self):
        raise NotImplementedError

    def esta_esgotado(self):
        raise NotImplementedError