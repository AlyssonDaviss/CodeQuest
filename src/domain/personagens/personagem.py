from abc import ABC, abstractmethod

class Personagem(ABC):
    '''Classe abstrata para personagens:

    Attributes:
    nome (str): Representa o nome do personagem
    pontos_vida (int): Representa a quantidade de pontos de vida que o personagem possui
    pontos_vida_max (int): Representa a quantidade máxima de pontos de vida de um personagem
    ataque (int): Representa a quantidade de pontos de vida que o personagem retira do oponente ao atacar
    defesa (int): Representa a quantidade de dano recebido que um personagem pode anular
    status (str): Representa o estado do personagem (morto ou vivo)
    '''
    def __init__(self, nome: str, pontos_vida_max: int, ataque: int, defesa: int, status: str = None) -> None:
        self.nome = nome
        self.pontos_vida_max = pontos_vida_max
        self.pontos_vida = pontos_vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.status = status

    def receber_dano(self, dano: int) -> None:
        """
        Subtrai pontos de vida do personagem conforme o dano recebido
        """
        self.pontos_vida -= dano

    def curar_vida(self, pontos_cura: int) -> None:
        """
        Recupera a vida do personagem conforme os pontos de cura recebidos
        """
        if self.pontos_vida + pontos_cura > self.pontos_vida_max:
            self.pontos_vida = self.pontos_vida_max
        else:
            self.pontos_vida += pontos_cura

    def esta_vivo(self) -> bool:
        return self.status

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defesa(self):
        pass