import os
from app.storage import JsonStorage
from app.disciplina_service import DisciplinaService


def criar_service_teste():
    arquivo = "data/disciplinas_pytest.json"
    if os.path.exists(arquivo):
        os.remove(arquivo)
    storage = JsonStorage(arquivo)
    return DisciplinaService(storage)


def test_criar_disciplina():
    service = criar_service_teste()
    disciplina = service.criar_disciplina({
        "titulo": "Engenharia de Software",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 45,
        "disciplina_verao": False
    })
    assert disciplina["id"] == 1
    assert disciplina["titulo"] == "Engenharia de Software"


def test_listar_disciplinas():
    service = criar_service_teste()
    service.criar_disciplina({
        "titulo": "Cálculo I",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 50,
        "disciplina_verao": False
    })
    lista = service.listar_disciplinas()
    assert len(lista) == 1


def test_buscar_disciplina_por_id():
    service = criar_service_teste()
    criada = service.criar_disciplina({
        "titulo": "Lógica de Programação",
        "data_inicio": "2026-08-01",
        "data_termino": "2026-12-10",
        "numero_vagas": 40,
        "disciplina_verao": False
    })
    encontrada = service.buscar_disciplina_por_id(criada["id"])
    assert encontrada["titulo"] == "Lógica de Programação"


def test_atualizar_disciplina():
    service = criar_service_teste()
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


def test_remover_disciplina():
    service = criar_service_teste()
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


def test_nao_permitir_vagas_invalidas():
    service = criar_service_teste()
    try:
        service.criar_disciplina({
            "titulo": "Inválida",
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-10",
            "numero_vagas": 0,
            "disciplina_verao": False
        })
        assert False
    except ValueError as error:
        assert str(error) == "Número de vagas deve ser inteiro maior que zero ou"

