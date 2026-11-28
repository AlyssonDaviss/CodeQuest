from item import Item

class Equipamento(Item):
    """
    Item que não é consumível pelo usuário, mas pode ser utilizado batalhas por exemplo
    """
    def __init__(self, nome: str, descricao: str, empilhavel: bool, bonus_ataque: int, bonus_defesa: int, tipo_bonus: str, equipado: bool):
        super.__init__(self, nome= nome, descricao= descricao, empilhavel= empilhavel)
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa
        self.tipo_bonus = tipo_bonus
        self.equipado = equipado

    def equipar(self):
        raise NotImplementedError

    def desequipar(self):
        raise NotImplementedError