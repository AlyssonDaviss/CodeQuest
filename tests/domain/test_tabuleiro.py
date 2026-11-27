import pytest
from src.domain.tabuleiro.casa import Casa
from src.domain.tabuleiro.casa_comum import CasaComum

# Casas

# Casa comum

def test_casa_e_abstrata():
    with pytest.raises(TypeError):
        Casa(1, None)


def test_nasce_nao_concluida():
    casa = CasaComum(1, None)
    assert casa.numero == 1
    assert casa.concluida is False


def test_aprovado_conclui():
    casa = CasaComum(1, None)
    casa.concluir(True)
    assert casa.concluida is True


def test_reprovado_nao_conclui():
    casa = CasaComum(1, None)
    casa.concluir(False)
    assert casa.concluida is False


def test_reiniciar():
    casa = CasaComum(1, None)
    casa.concluir(True)
    casa.reiniciar()
    assert casa.concluida is False