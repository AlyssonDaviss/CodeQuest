from item import Item
 
class ItemChave(Item):
    """
    Item usado para acessar novas regiões do jogo
    """
    def __init__(self, nome, descricao, empilhavel, conceito_programacao):
        super().__init__(nome= nome, descricao= descricao, empilhavel= empilhavel)
        self.conceito_programacao = conceito_programacao