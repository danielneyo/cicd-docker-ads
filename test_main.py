import pytest
from fastapi.testclient import TestClient
from main import app, tarefas, contador_id
import main

client = TestClient(app)


def setup_function():
    """Limpa o estado antes de cada teste"""
    main.tarefas.clear()
    main.contador_id = 1


# ── 1. Health Check ───────────────────────────────────────
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ── 2. Criar tarefa com sucesso ───────────────────────────
def test_criar_tarefa():
    response = client.post("/tarefas", json={"titulo": "Estudar Docker"})
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Estudar Docker"
    assert data["concluida"] == False
    assert "id" in data


# ── 3. Ler tarefa existente ───────────────────────────────
def test_buscar_tarefa_existente():
    client.post("/tarefas", json={"titulo": "Tarefa de teste"})
    response = client.get("/tarefas/1")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa de teste"


# ── 4. Ler tarefa inexistente (deve retornar 404) ─────────
def test_buscar_tarefa_inexistente():
    response = client.get("/tarefas/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"


# ── 5. Remover tarefa ─────────────────────────────────────
def test_remover_tarefa():
    client.post("/tarefas", json={"titulo": "Tarefa para deletar"})
    response = client.delete("/tarefas/1")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Tarefa removida com sucesso"
    # Confirma que foi removida
    response2 = client.get("/tarefas/1")
    assert response2.status_code == 404


# ── 6. Atualizar tarefa ───────────────────────────────────
def test_atualizar_tarefa():
    client.post("/tarefas", json={"titulo": "Tarefa original"})
    response = client.put("/tarefas/1", json={"titulo": "Tarefa atualizada", "concluida": True})
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa atualizada"
    assert response.json()["concluida"] == True
