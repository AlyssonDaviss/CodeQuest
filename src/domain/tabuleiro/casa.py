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

    def concluir(self, aprovado: bool) -> None:
        """Repassa o resultado do desafio ao gancho correspondente."""
        if aprovado:
            self._tratar_aprovacao()
        else:
            self._tratar_reprovacao()

    def reiniciar(self) -> None:
        """Reinicia a casa."""
        self._concluida = False

    def _tratar_aprovacao(self) -> None:
        """Marca a casa como concluída e dá as recompensas."""
        self._concluida = True
        ...  # recompensas

    @abstractmethod
    def _tratar_reprovacao(self) -> None:
        """A definir."""

