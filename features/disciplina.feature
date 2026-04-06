Feature: Gerenciamento de disciplinas

  Scenario: Cadastrar uma disciplina com dados válidos
    Given que o sistema está limpo
    When eu cadastro uma disciplina com título "Algoritmos", data de início "2026-08-01", data de término "2026-12-10", vagas 40 e disciplina de verão "false"
    Then o cadastro deve ser realizado com sucesso
    And a disciplina deve aparecer na listagem

  Scenario: Listar disciplinas cadastradas
    Given que o sistema está limpo
    And existe uma disciplina cadastrada com título "Banco de Dados", data de início "2026-08-05", data de término "2026-12-15", vagas 35 e disciplina de verão "false"
    When eu listar as disciplinas
    Then deve existir pelo menos 1 disciplina na listagem

  Scenario: Buscar disciplina por id
    Given que o sistema está limpo
    And existe uma disciplina cadastrada com título "Estruturas de Dados", data de início "2026-08-10", data de término "2026-12-20", vagas 30 e disciplina de verão "false"
    When eu buscar a disciplina pelo id cadastrado
    Then a disciplina encontrada deve ter o título "Estruturas de Dados"

  Scenario: Atualizar uma disciplina existente
    Given que o sistema está limpo
    And existe uma disciplina cadastrada com título "POO", data de início "2026-08-01", data de término "2026-12-01", vagas 25 e disciplina de verão "false"
    When eu atualizar a disciplina cadastrada para título "Programação Orientada a Objetos" e vagas 50
    Then a disciplina atualizada deve ter o título "Programação Orientada a Objetos"
    And a disciplina atualizada deve ter 50 vagas

  Scenario: Remover uma disciplina existente
    Given que o sistema está limpo
    And existe uma disciplina cadastrada com título "Redes", data de início "2026-08-01", data de término "2026-12-01", vagas 20 e disciplina de verão "true"
    When eu remover a disciplina cadastrada
    Then a remoção deve ser realizada com sucesso
    And a disciplina não deve mais existir

  Scenario: Não permitir cadastro com vagas inválidas
    Given que o sistema está limpo
    When eu tentar cadastrar uma disciplina com vagas 0
    Then o sistema deve exibir erro de validação