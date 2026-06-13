# Containerização com Docker

## Dockerfile
A aplicaçãoo usa build multi-stage:
- Estagio 1 (builder): instala as dependencias
- Estagio 2 (producao): imagem slim enxuta e segura

## Boas praticas aplicadas
- Imagem base: python:3.11-slim
- Usuario não-root (appuser) por segurança
- HEALTHCHECK configurado
- Porta 8000 exposta

## Como executar localmente
docker-compose up --build
Acesse: http://localhost:8000/docs

Documentado por Taina
