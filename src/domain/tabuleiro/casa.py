from abc import ABC, abstractclassmethod

class Casa(ABC):
    """unidade da região, com um desafio de programação."""
    def __ini__(self, numero: int, desafio) -> None:
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
         """Define se a casa foi concluida ou não"""
         if aprovado:
              self._concluida = True
              self._tratar_aprovacao()
         else:
              self._tratar_reprovacao()

    def reiniciar(self) -> None:
        """Reinicia a casa"""
        self._concluida = False

    def _tratar_aprovacao(self):
         """Faz passar de casa e receber as reconpensas"""
         pass

    @abstractclassmethod
    def _tratar_reprovacao(self):
         """A definir"""
         pass

