from enum import Enum


class ResultadoBatalha(Enum):
    """Situação de uma batalha, informada pela própria Batalha."""

    EM_ANDAMENTO = "em_andamento"
    VITORIA = "vitoria"
    DERROTA = "derrota"