from .regiao import Regiao
from .casa import Casa
from nucleo.erros import *

class Trilha:
    def __init__(self, regioes: list[Regiao]) -> None:
        self._regioes = list(regioes)
        self._i_regiao = 0         # Indice da região atual
        self._i_casa = 0           # Indice da casa atual

    # Coleta de informações
    def regiao_atual(self) -> Regiao:
        """Devolve a região em que o jogador está."""
        return self._regioes[self._i_regiao]

    def casa_atual(self) -> Casa:
        """Devolve a casa em que o jogador está, dentro da região atual."""
        return self.regiao_atual().casas[self._i_casa]

    def _esta_na_ultima_casa_da_regiao(self) -> bool:
        """Indica se o jogador está na última casa da região atual."""
        return self._i_casa == len(self.regiao_atual().casas) - 1

    def _ha_mais_regioes(self) -> bool:
        """Indica se existe uma região depois da atual."""
        return self._i_regiao < len(self._regioes) - 1

    def tem_proxima_casa(self) -> bool:
        """Indica se há uma próxima casa; False significa que o jogo acabou."""
        return not self._esta_na_ultima_casa_da_regiao() or self._ha_mais_regioes()

    # Movimentação
    def avancar(self) -> Casa:
        """Move para a próxima casa e a devolve.

        Raises:
            FimDaTrilhaErro: se já está na última casa da última região.
        """
        if not self.tem_proxima_casa():
            raise FimDaTrilhaErro()

        if self._esta_na_ultima_casa_da_regiao():
            self._i_regiao += 1
            self._i_casa = 0
        else:
            self._i_casa += 1
        return self.casa_atual()

    def reiniciar(self) -> None:
        """Volta o jogador ao início e desfaz a conclusão de todas as casas."""
        self._i_regiao = 0
        self._i_casa = 0

        for regiao in self._regioes:
            regiao.reiniciar()