from .casa import Casa


class CasaComum(Casa):
    """Casa só de ensino, sem batalha: conclui quando o desafio é aprovado."""

    def _tratar_reprovacao(self) -> None:
        """Sem penalidade: o jogador apenas tenta de novo."""

    # Boa parte do funcionamneto dessa classe já é feita pela classe abstrata.