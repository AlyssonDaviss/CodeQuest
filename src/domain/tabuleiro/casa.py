from abc import ABC, abstractmethod


class Casa(ABC):
    """Unidade da região, com um desafio de programação."""

    def __init__(self, numero: int, desafio) -> None:
        self._numero = numero
        self._desafio = desafio
        self._concluida = False

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def desafio(self):
        return self._desafio

    @property
    def concluida(self) -> bool:
        return self._concluida

    def registrar_resultado(self, aprovado: bool) -> None:
        """Repassa o resultado do código do desafio ao gancho correspondente."""
        if aprovado:
            self._tratar_aprovacao()
        else:
            self._tratar_reprovacao()

    def reiniciar(self) -> None:
        """Volta a casa ao estado de não concluída."""
        self._concluida = False

    def _marcar_concluida(self) -> None:
        """Marca a casa como concluída (as filhas chamam quando for a hora)."""
        self._concluida = True

    @abstractmethod
    def _tratar_aprovacao(self) -> None:
        """O que acontece quando o código do desafio é aprovado."""

    @abstractmethod
    def _tratar_reprovacao(self) -> None:
        """O que acontece quando o código do desafio é reprovado."""
