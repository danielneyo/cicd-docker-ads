# 📋 API de Tarefas — CI/CD com Docker

Projeto desenvolvido para a disciplina de **Gerenciamento de Configuração de Software** do curso de Análise e Desenvolvimento de Sistemas.

## 👥 Equipe

| Membro | Responsabilidade |
|--------|-----------------|
| Daniel (Líder) | Repositório, pipeline CI/CD e coordenação |
| Alberto | Endpoints GET e POST da API |
| Ester | Endpoints PUT e DELETE da API |
| Tainá | Dockerfile multi-stage e docker-compose |
| Emerson | Testes automatizados |
| Marjory | Documentação e README |
| Hícaro | QA, Docker Hub e entrega |

---

## 🚀 Sobre o projeto

API REST de lista de tarefas (To-Do) com pipeline CI/CD completo utilizando **GitHub Actions** e **Docker**.

### Endpoints disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Verificação de saúde da API |
| GET | `/tarefas` | Listar todas as tarefas |
| GET | `/tarefas/{id}` | Buscar tarefa por ID |
| POST | `/tarefas` | Criar nova tarefa |
| PUT | `/tarefas/{id}` | Atualizar tarefa |
| DELETE | `/tarefas/{id}` | Remover tarefa |

---

## 🔄 Pipeline CI/CD

```mermaid
flowchart LR
    A[Push / PR] --> B[JOB: CI\nInstala deps\nRoda testes]
    B -->|✅ Testes ok| C[JOB: Build\nBuild Docker\nsem push]
    C -->|✅ Build ok\nApenas na main| D[JOB: CD\nPush Docker Hub\ncom tag de versão]
    B -->|❌ Falha| X[Pipeline\ninterrompido]
```

**Fluxo:**
1. Qualquer `push` ou `pull request` dispara o job de **CI** (testes)
2. Se os testes passam, o job de **Build** valida o Dockerfile
3. Se for um push na branch `main`, o job de **CD** publica a imagem no Docker Hub

---

## 🐳 Executar localmente com Docker

A aplicação foi totalmente conteinerizada utilizando boas práticas de mercado, como **Build Multi-stage** (para manter a imagem leve) e execução com **usuário não-root** (para maior segurança).

**Pré-requisito:** Docker instalado

```bash
# Clonar o repositório
git clone [https://github.com/danielneyo/cicd-docker-ads](https://github.com/danielneyo/cicd-docker-ads)
cd cicd-docker-ads

# Subir a aplicação
docker-compose up --build

# A API estará disponível em:
# http://localhost:8000
# Documentação automática: http://localhost:8000/docs
```

---

## 🧪 Executar os testes

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar os testes
pytest test_main.py -v
```

Saída esperada:
```
test_main.py::test_health_check              PASSED
test_main.py::test_criar_tarefa              PASSED
test_main.py::test_buscar_tarefa_existente   PASSED
test_main.py::test_buscar_tarefa_inexistente PASSED
test_main.py::test_remover_tarefa            PASSED
test_main.py::test_atualizar_tarefa          PASSED
```

---

## 📸 Evidências do Pipeline

Aqui estão as capturas de tela que comprovam a execução bem-sucedida de todo o fluxo automatizado no GitHub Actions (Jobs de Teste, Build e Deploy):
> ![Pipeline CI/CD em verde](img/pipeline-verde.jpg)


![Execução do GitHub Actions](img/github-actions.jpg)


![Pipeline executado com sucesso](img/pipeline-ci-cd.jpg)



> 💡 **Nota:** O pipeline foi executado com sucesso no GitHub Actions, contemplando com êxito as etapas de testes automatizados (CI), geração da imagem Docker (Build) e publicação no Docker Hub (CD).
---
---

## 🐋 Imagem no Docker Hub

![Docker Hub](img/docker-hub.jpg)

```bash
docker pull hicaroluiz/api-tarefas:v1.0.3


```
## 📖 Documentações Complementares

Para informações mais detalhadas sobre cada etapa específica do projeto, consulte os arquivos dedicados criados pela equipe:

* 🐳 **Configuração do Docker e Docker Hub:** Detalhes sobre o Dockerfile multi-stage, boas práticas de segurança e publicação da imagem. Acesse: **[DUCKERHUB.md](./DUCKERHUB.md)**
* 🔌 **Endpoints da API:** Documentação técnica contendo as rotas, métodos (GET, POST, PUT, DELETE) e exemplos de requisição. Acesse: **[ENDPOINTS.md](./ENDPOINTS.md)**
* 🧪 **Relatório de Testes:** Cobertura de testes automatizados e validações de qualidade de software (QA). Acesse: **[relatorio-testes.md](./relatorio-testes.md)**

