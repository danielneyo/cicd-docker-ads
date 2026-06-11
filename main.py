from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="API de Tarefas", version="1.0.0")

# Banco de dados em memória
tarefas = []
contador_id = 1


class TarefaEntrada(BaseModel):
    titulo: str
    concluida: Optional[bool] = False


class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool


# ── Health Check ──────────────────────────────────────────
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ── Listar todas as tarefas ───────────────────────────────
@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas


# ── Buscar tarefa por ID ──────────────────────────────────
@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int):
    for t in tarefas:
        if t["id"] == tarefa_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


# ── Criar tarefa ──────────────────────────────────────────
@app.post("/tarefas", response_model=Tarefa, status_code=201)
def criar_tarefa(entrada: TarefaEntrada):
    global contador_id
    nova = {"id": contador_id, "titulo": entrada.titulo, "concluida": entrada.concluida}
    tarefas.append(nova)
    contador_id += 1
    return nova


# ── Atualizar tarefa ──────────────────────────────────────
@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, entrada: TarefaEntrada):
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["titulo"] = entrada.titulo
            t["concluida"] = entrada.concluida
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


# ── Remover tarefa ────────────────────────────────────────
@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int):
    for i, t in enumerate(tarefas):
        if t["id"] == tarefa_id:
            tarefas.pop(i)
            return {"mensagem": "Tarefa removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
