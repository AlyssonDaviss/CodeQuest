from .casa import Casa


class Regiao:
    """Agrupamento de casas, com Boss, início, meio e fim, focado em um conteúdo de Python."""

    def __init__(self, nome: str, conteudo_python: str, casas: list[Casa]) -> None:
        if not casas:
            raise ValueError("É necessário haver casas numa região.")
        self._nome = nome
        self._conteudo_python = conteudo_python
        self._casas = list(casas)

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def conteudo_python(self) -> str:
        return self._conteudo_python

    @property
    def casas(self) -> list[Casa]:
        """Devolve uma cópia, para ninguém alterar a lista interna."""
        return list(self._casas)

    def casa_inicial(self) -> Casa:
        """Primeira casa da região."""
        return self._casas[0]

    def casa_final(self) -> Casa:
        """Última casa da região, onde fica o Boss."""
        return self._casas[-1]

    def esta_concluida(self) -> bool:
        """Verifica se todas as casas da região foram concluídas."""
        for casa in self._casas:
            if not casa.concluida:
                return False
        return True

    def reiniciar(self) -> None:
        """Volta todas as casas ao estado inicial."""
        for casa in self._casas:
            casa.reiniciar()