# Relatório de Validação dos Testes Automatizados

## Responsável

Emerson Ferreira de Sousa

## Data da Execução

11/06/2026

## Horário da Execução

(Preencher com o horário em que o comando foi executado)

## Ambiente Utilizado

| Item                | Valor                 |
| ------------------- | --------------------- |
| Sistema Operacional | Windows 7 SP1 64 bits |
| Python              | 3.8.10                |
| Framework de Testes | pytest 8.2.0          |

## Comando Executado

```bash
py -m pytest -v
```

## Resultados dos Testes

| Teste                          | Endpoint             | Status Esperado          | Resultado  |
| ------------------------------ | -------------------- | ------------------------ | ---------- |
| test_health_check              | GET /health          | 200 OK                   | ✅ Aprovado |
| test_criar_tarefa              | POST /tarefas        | 201 Created              | ✅ Aprovado |
| test_buscar_tarefa_existente   | GET /tarefas/{id}    | 200 OK                   | ✅ Aprovado |
| test_buscar_tarefa_inexistente | GET /tarefas/{id}    | 404 Not Found            | ✅ Aprovado |
| test_remover_tarefa            | DELETE /tarefas/{id} | 200 OK ou 204 No Content | ✅ Aprovado |
| test_atualizar_tarefa          | PUT /tarefas/{id}    | 200 OK                   | ✅ Aprovado |

## Resumo da Execução

| Métrica         | Valor         |
| --------------- | ------------- |
| Total de Testes | 6             |
| Aprovados       | 6             |
| Reprovados      | 0             |
| Tempo Total     | 9.69 segundos |

## Evidência

Resultado apresentado pelo pytest:

* test_health_check PASSED
* test_criar_tarefa PASSED
* test_buscar_tarefa_existente PASSED
* test_buscar_tarefa_inexistente PASSED
* test_remover_tarefa PASSED
* test_atualizar_tarefa PASSED

Resultado Final:

6 passed in 9.69s

## Conclusão

Todos os testes automatizados da API foram executados com sucesso. Os endpoints apresentaram comportamento compatível com os requisitos definidos para o projeto, validando as operações de criação, consulta, atualização, remoção e verificação de saúde da aplicação.
