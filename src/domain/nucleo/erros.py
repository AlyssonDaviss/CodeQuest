from __future__ import annotations

# No Notion tem modelos para os erros que podemos lançar

class CodeQuestErro(Exception):
    """Erro base de todo o jogo.

    Capturar ``CodeQuestErro`` pega qualquer erro previsto pelo domínio,
    sem esconder erros inesperados (``TypeError``, ``KeyError`` etc.).
    """

    mensagem_padrao = "Ocorreu um erro no CodeQuest."

    def __init__(self, mensagem: str | None = None) -> None:
        self._mensagem = mensagem or self.mensagem_padrao
        super().__init__(self._mensagem)

    @property
    def mensagem(self) -> str:
        """Texto pronto para ser exibido ao jogador."""
        return self._mensagem


# Tabuleiro

class ErroTabuleiro(CodeQuestErro):
    """Erro ao navegar ou montar o tabuleiro."""

    mensagem_padrao = "Erro no tabuleiro."

class FimDaTrilhaErro(ErroTabuleiro):
    """Tentativa de avançar quando não existe próxima casa."""

    mensagem_padrao = "Não há próxima casa: você chegou ao fim da trilha."

