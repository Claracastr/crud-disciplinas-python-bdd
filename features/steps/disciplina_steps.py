from behave import given, when, then


@given('que o sistema está limpo')
def step_sistema_limpo(context):
    context.storage.write_all([])


@given('existe uma disciplina cadastrada com título "{titulo}", data de início "{data_inicio}", data de término "{data_termino}", vagas {vagas:d} e disciplina de verão "{verao}"')
def step_existe_disciplina(context, titulo, data_inicio, data_termino, vagas, verao):
    disciplina = {
        "titulo": titulo,
        "data_inicio": data_inicio,
        "data_termino": data_termino,
        "numero_vagas": vagas,
        "disciplina_verao": verao.lower() == "true"
    }
    criada = context.service.criar_disciplina(disciplina)
    context.disciplina_id = criada["id"]


@when('eu cadastro uma disciplina com título "{titulo}", data de início "{data_inicio}", data de término "{data_termino}", vagas {vagas:d} e disciplina de verão "{verao}"')
def step_cadastrar_disciplina(context, titulo, data_inicio, data_termino, vagas, verao):
    disciplina = {
        "titulo": titulo,
        "data_inicio": data_inicio,
        "data_termino": data_termino,
        "numero_vagas": vagas,
        "disciplina_verao": verao.lower() == "true"
    }
    context.result = context.service.criar_disciplina(disciplina)


@when('eu listar as disciplinas')
def step_listar_disciplinas(context):
    context.result = context.service.listar_disciplinas()


@when('eu buscar a disciplina pelo id cadastrado')
def step_buscar_disciplina(context):
    context.result = context.service.buscar_disciplina_por_id(context.disciplina_id)


@when('eu atualizar a disciplina cadastrada para título "{titulo}" e vagas {vagas:d}')
def step_atualizar_disciplina(context, titulo, vagas):
    context.result = context.service.atualizar_disciplina(
        context.disciplina_id,
        {
            "titulo": titulo,
            "numero_vagas": vagas
        }
    )


@when('eu remover a disciplina cadastrada')
def step_remover_disciplina(context):
    context.result = context.service.remover_disciplina(context.disciplina_id)


@when('eu tentar cadastrar uma disciplina com vagas {vagas:d}')
def step_cadastrar_disciplina_invalida(context, vagas):
    try:
        context.service.criar_disciplina({
            "titulo": "Disciplina Inválida",
            "data_inicio": "2026-01-01",
            "data_termino": "2026-02-01",
            "numero_vagas": vagas,
            "disciplina_verao": False
        })
    except Exception as error:
        context.error = error


@then('o cadastro deve ser realizado com sucesso')
def step_validar_cadastro(context):
    assert context.result is not None
    assert "id" in context.result


@then('a disciplina deve aparecer na listagem')
def step_validar_listagem(context):
    disciplinas = context.service.listar_disciplinas()
    assert len(disciplinas) == 1


@then('deve existir pelo menos 1 disciplina na listagem')
def step_validar_qtd_listagem(context):
    assert len(context.result) >= 1


@then('a disciplina encontrada deve ter o título "{titulo}"')
def step_validar_titulo(context, titulo):
    assert context.result is not None
    assert context.result["titulo"] == titulo


@then('a disciplina atualizada deve ter o título "{titulo}"')
def step_validar_titulo_atualizado(context, titulo):
    assert context.result["titulo"] == titulo


@then('a disciplina atualizada deve ter {vagas:d} vagas')
def step_validar_vagas_atualizadas(context, vagas):
    assert context.result["numero_vagas"] == vagas


@then('a remoção deve ser realizada com sucesso')
def step_validar_remocao(context):
    assert context.result is True


@then('a disciplina não deve mais existir')
def step_validar_nao_existe(context):
    disciplina = context.service.buscar_disciplina_por_id(context.disciplina_id)
    assert disciplina is None


@then('o sistema deve exibir erro de validação')
def step_validar_erro(context):
    assert context.error is not None