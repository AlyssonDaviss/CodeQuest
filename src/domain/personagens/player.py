from personagem import Personagem

class Player(Personagem):
    """
    Classe do personagem controlado pelo jogador

    Attributes:
    xp (int): Quantidade de xp que o player possui no momento
    nivel (int): Armazena o número do nível atual do player
    prox_nivel_xp (int): Quantidade de xp para subir ao próximo nível --> ADICIONADO
    vidas (int): Quantdade de vidas do player
    inventario (Inventario): Inventario do player
    acoes (list[Acao]): Lista de ações disponíveis ao player
    equipamentos (list[Equipamento]):  Lista com os equipamentos do playe --> OBS: Verificar se é mesmo necessário
    """

# Fazer esqueleto das classes que se relacionarão com Player primerio