
# MÉTODOS DA CASA
#   _tratar_aprovacao()   -> chama batalha.resolver_turno(True). Se o inimigo
#                            caiu, a casa fica concluída.
#   _tratar_reprovacao()  -> chama batalha.resolver_turno(False). Não conclui.
#   reiniciar()           -> reinicia a casa e a batalha.
#   regra extra           -> casa já concluída não aceita jogada: lança
#                            CombateEncerradoErro SEM chamar a batalha.
#
# COMO RODAR (uma etapa por vez, na ordem):
#   uv run pytest tests/domain/test_casa_batalha.py -k Etapa1 -v
#   uv run pytest tests/domain/test_casa_batalha.py -k Etapa2 -v
#   ... até a Etapa5 e, por fim, o arquivo inteiro.
#
# Dica: apague os comentários de cada etapa depois que ela passar.
# =============================================================================

from .casa import Casa
from src.domain.nucleo.enums.batalha import ResultadoBatalha


class CasaBatalha(Casa):
    """Casa de combate: aprovar o código do desafio inicia a batalha.

    A casa só chama a Batalha e lê o resultado dela: quem sabe quem ganhou é a
    Batalha. A casa só fica concluída quando a batalha termina em vitória.
    """

    def __init__(self, numero: int, desafio, batalha) -> None:
        super().__init__(numero, desafio)
        self._batalha = batalha

    @property
    def batalha(self):
        return self._batalha

    # Trabalha em cima do resultado do defafio
    def _tratar_aprovacao(self) -> None:
        # Antes de tudo: se a casa já foi concluída, lançar CombateEncerradoErro.
        # O código foi aprovado: começa a batalha.
        # Implementar a Batalha primeiro (ela decide como o "iniciar" se chama).
        # NÃO marcar a casa como concluída aqui: quem conclui é o resultado da batalha.
        ...

    def _tratar_reprovacao(self) -> None:
        # Antes de tudo: se a casa já foi concluída, lançar CombateEncerradoErro.
        # Reprovado antes da batalha: a batalha não começa.
        # Penalidade: a definir (regra atual: refazer o desafio desde o início).
        # Não olhar o resultado da batalha aqui: ela nem começou.
        ...

    # Trabalha em cima do resultado da batalha
    def verificar_resultado(self) -> ResultadoBatalha:
        # Ler o resultado que a BATALHA deu.
        resultado = ...  

        # Se ainda está em andamento: não fazer nada.
        if resultado == ResultadoBatalha.EM_ANDAMENTO:
            return resultado

        # Se o inimigo foi derrotado: marcar a casa como concluída.
        if resultado == ResultadoBatalha.VITORIA:
            self._marcar_concluida()   # ou self._concluida = True, se não adotou a Casa nova

        # Se o jogador perdeu: refazer a casa (reiniciar a casa e a batalha).
        elif resultado == ResultadoBatalha.DERROTA:
            self.reiniciar()

        return resultado

    

