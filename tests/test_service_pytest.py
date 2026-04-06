import os
import pytest
from app.storage import JsonStorage
from app.disciplina_service import DisciplinaService


@pytest.fixture
def service():
    arquivo = "data/disciplinas_pytest.json"
    if os.path.exists(arquivo):
        os.remove(arquivo)

    storage = JsonStorage(arquivo)
    service = DisciplinaService(storage)

    yield service

    if os.path.exists(arquivo):
        os.remove(arquivo)


def test_criar_disciplina(service):
    disciplina = service.criar_disciplina({
        "titulo": "Engenharia de Software",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 45,
        "disciplina_verao": False
    })

    assert disciplina["id"] == 1
    assert disciplina["titulo"] == "Engenharia de Software"


def test_listar_disciplinas(service):
    service.criar_disciplina({
        "titulo": "Cálculo I",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 50,
        "disciplina_verao": False
    })

    lista = service.listar_disciplinas()

    assert len(lista) == 1
    assert lista[0]["titulo"] == "Cálculo I"


def test_buscar_disciplina_por_id(service):
    criada = service.criar_disciplina({
        "titulo": "Lógica de Programação",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 40,
        "disciplina_verao": False
    })

    encontrada = service.buscar_disciplina_por_id(criada["id"])

    assert encontrada is not None
    assert encontrada["titulo"] == "Lógica de Programação"


def test_buscar_disciplina_inexistente(service):
    encontrada = service.buscar_disciplina_por_id(999)
    assert encontrada is None


def test_atualizar_disciplina(service):
    criada = service.criar_disciplina({
        "titulo": "POO",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 20,
        "disciplina_verao": False
    })

    atualizada = service.atualizar_disciplina(criada["id"], {
        "titulo": "Programação Orientada a Objetos",
        "numero_vagas": 60
    })

    assert atualizada["titulo"] == "Programação Orientada a Objetos"
    assert atualizada["numero_vagas"] == 60


def test_atualizar_disciplina_inexistente(service):
    atualizada = service.atualizar_disciplina(999, {
        "titulo": "Teste"
    })

    assert atualizada is None


def test_remover_disciplina(service):
    criada = service.criar_disciplina({
        "titulo": "Redes de Computadores",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 20,
        "disciplina_verao": True
    })

    removida = service.remover_disciplina(criada["id"])

    assert removida is True
    assert service.buscar_disciplina_por_id(criada["id"]) is None


def test_remover_disciplina_inexistente(service):
    removida = service.remover_disciplina(999)
    assert removida is False


def test_nao_permitir_vagas_invalidas(service):
    with pytest.raises(ValueError, match="Número de vagas deve ser inteiro maior que zero"):
        service.criar_disciplina({
            "titulo": "Inválida",
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-10",
            "numero_vagas": 0,
            "disciplina_verao": False
        })


def test_nao_permitir_titulo_invalido(service):
    with pytest.raises(ValueError, match="Título inválido"):
        service.criar_disciplina({
            "titulo": "",
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-10",
            "numero_vagas": 10,
            "disciplina_verao": False
        })


def test_nao_permitir_disciplina_verao_invalida(service):
    with pytest.raises(ValueError, match="disciplina_verao deve ser booleano"):
        service.criar_disciplina({
            "titulo": "Teste",
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-10",
            "numero_vagas": 10,
            "disciplina_verao": "sim"
        })

def test_listar_disciplinas_vazio(service):
    lista = service.listar_disciplinas()
    assert lista == []
