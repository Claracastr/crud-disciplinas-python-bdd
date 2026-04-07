Documentação do Projeto — CRUD de Disciplinas com Python, BDD e GitHub Actions/Clara Castro e Maria Eduarda Alexandre
1. Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de atender à atividade proposta, que consistia na criação de uma aplicação CRUD para gerenciar disciplinas oferecidas por uma instituição de ensino. Além da implementação das operações básicas de cadastro, consulta, atualização e remoção, também foi necessário desenvolver testes funcionais utilizando a metodologia BDD e configurar uma esteira automatizada no GitHub Actions para validar pull requests com cobertura mínima de 75%.

2. Descrição da aplicação

A aplicação foi desenvolvida em Python e utiliza um arquivo JSON como forma de persistência de dados, com o objetivo de simplificar a implementação e facilitar os testes.

Cada disciplina cadastrada possui os seguintes campos obrigatórios:

título
data de início
data de término
número de vagas
indicação se a disciplina é de verão
3. Funcionalidades implementadas

Foram implementadas as quatro operações principais do CRUD:

Create
Permite cadastrar uma nova disciplina no sistema.

Read
Permite listar todas as disciplinas cadastradas e também buscar uma disciplina específica por ID.

Update
Permite atualizar os dados de uma disciplina já existente.

Delete
Permite remover uma disciplina do sistema.

5. Tecnologias utilizadas

As principais tecnologias e ferramentas utilizadas no desenvolvimento foram:

Python
JSON
Behave
Pytest
Pytest-Cov
Git
GitHub
GitHub Actions
6. Persistência de dados

Os dados das disciplinas são armazenados em um arquivo JSON localizado na pasta data. Essa abordagem foi escolhida por ser simples, prática e suficiente para os requisitos da atividade.

A classe responsável pela leitura e escrita no arquivo JSON foi implementada no arquivo storage.py.

7. Lógica da aplicação

A lógica do sistema foi centralizada no arquivo disciplina_service.py, responsável por:

validar os dados recebidos
criar disciplinas com ID automático
listar disciplinas cadastradas
buscar disciplina por ID
atualizar disciplina existente
remover disciplina existente

Também foram implementadas validações para impedir dados inválidos, como:

título vazio
número de vagas menor ou igual a zero
valor inválido para o campo de disciplina de verão
8. Testes BDD

Para atender ao requisito da atividade, foram desenvolvidos testes utilizando a metodologia BDD com a biblioteca Behave.

Os cenários foram escritos em linguagem natural no arquivo disciplina.feature, descrevendo o comportamento esperado do sistema. Entre os cenários testados, estão:

cadastro de disciplina com dados válidos
listagem de disciplinas
busca de disciplina por ID
atualização de disciplina existente
remoção de disciplina
tentativa de cadastro com dados inválidos

Esses testes têm como objetivo validar o comportamento funcional da aplicação sob a perspectiva do usuário.

9. Testes automatizados com Pytest

Além dos testes BDD, também foram implementados testes automatizados com Pytest para garantir melhor cobertura do código e viabilizar a exigência de cobertura mínima na esteira automatizada.

Os testes verificam casos como:

criação de disciplina
listagem vazia e listagem com registros
busca por ID existente e inexistente
atualização de disciplina
remoção de disciplina
tratamento de dados inválidos
cenários de erro

Esses testes complementam os cenários BDD e ajudam a medir a qualidade interna da aplicação.

10. Cobertura de testes

A cobertura de testes foi configurada com a biblioteca pytest-cov. Durante os testes locais, a aplicação atingiu cobertura superior ao mínimo exigido pela atividade, garantindo conformidade com o requisito de pelo menos 75% de cobertura.

11. Esteira automatizada com GitHub Actions

Foi configurada uma esteira de integração contínua por meio do GitHub Actions. O workflow foi definido no arquivo:

.github/workflows/ci.yml

A esteira foi configurada para ser acionada automaticamente em pull requests direcionados à branch main.

Etapas executadas pela esteira

A pipeline realiza as seguintes etapas:

faz checkout do código do repositório
configura a versão do Python
instala as dependências do projeto
executa os testes BDD com Behave
executa os testes com Pytest e verifica a cobertura mínima de 75%

Caso algum teste falhe ou a cobertura fique abaixo do valor mínimo definido, a execução da esteira falha.

12. Fluxo de uso com branches e pull requests

Durante o desenvolvimento, foi utilizado o fluxo com branches para simular um processo mais próximo do ambiente profissional.

O processo seguido foi:

criação de branch para desenvolvimento ou teste
implementação de alterações no código
commit e push para o GitHub
abertura de pull request para a branch main
execução automática da esteira no GitHub Actions
validação do resultado dos testes

Esse fluxo permitiu testar tanto cenários de sucesso quanto cenários de falha na pipeline.

13. Validação da esteira

Durante os testes da pipeline, foram realizados dois tipos de validação:

Cenário de sucesso

Foram adicionados testes válidos e a esteira foi executada com sucesso, demonstrando que o código estava apto para integração.

Cenário de falha

Também foi criado um teste propositalmente incorreto para validar o comportamento da esteira em caso de erro. Nesse cenário, a pipeline falhou, comprovando que a automação estava verificando os testes corretamente.

14. Dificuldades encontradas

Durante o desenvolvimento e configuração da atividade, algumas dificuldades foram encontradas, como:

ajuste do nome correto do arquivo environment.py para o Behave
correção da estrutura do arquivo ci.yml
entendimento do funcionamento da esteira em pull requests
diferença entre a falha da pipeline e o bloqueio real de merge
conflitos entre branches ao testar cenários de falha
identificação do local correto para configuração de proteção de branch no GitHub

Essas dificuldades foram importantes para aprofundar o entendimento sobre versionamento, testes automatizados e integração contínua.

15. Resultado final

Ao final do desenvolvimento, o projeto passou a contar com:

CRUD funcional de disciplinas
persistência em JSON
testes BDD
testes automatizados com cobertura
workflow automatizado no GitHub Actions
validação de pull requests para a branch principal

Dessa forma, a atividade foi atendida com uma solução simples, funcional e organizada, contemplando tanto o desenvolvimento da aplicação quanto a automação de testes.

16. Conclusão

O projeto permitiu aplicar, na prática, conceitos importantes de desenvolvimento de software, como organização de código, testes funcionais, cobertura de testes, versionamento com Git e automação com GitHub Actions. Além de atender aos requisitos da atividade, a implementação também contribuiu para o aprendizado de boas práticas utilizadas em contextos reais de desenvolvimento..