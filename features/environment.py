import os
from app.storage import JsonStorage
from app.disciplina_service import DisciplinaService


def before_scenario(context, scenario):
    test_file = "data/disciplinas_test.json"

    if os.path.exists(test_file):
        os.remove(test_file)

    context.storage = JsonStorage(test_file)
    context.service = DisciplinaService(context.storage)
    context.result = None
    context.error = None
    context.disciplina_id = None