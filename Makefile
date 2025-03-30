# Makefile - MechBot 2.0x
# Equipo Técnico - Automatización de flujos de trabajo

# Variables de entorno
PROJECT_NAME := mechbot-2x
PYTHON := python3.10
PIP := $(PYTHON) -m pip
DOCKER_COMPOSE := docker-compose -f docker-compose.yml

# Configuración de entornos
ENV_FILE := .env
export $(shell grep -v '^#' $(ENV_FILE) | xargs)

# Colores para terminal
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m

## —— Help ——
help:  ## Muestra esta ayuda
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(GREEN)%-25s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

## —— Setup ——
install:  ## Instala dependencias principales
	$(PIP) install -e .[dev,ml,streaming]

install-prod:  ## Instala solo dependencias de producción
	$(PIP) install --no-deps .

env-file:  ## Crea archivo .env de ejemplo
	@cp .env.sample .env
	@echo "$(GREEN)✓ Archivo .env creado$(NC)"

## —— Desarrollo ——
run:  ## Inicia servidor de desarrollo
	uvicorn mechbot.main:app --reload --host 0.0.0.0 --port 8000

test:  ## Ejecuta todos los tests
	$(PYTHON) -m pytest -v --cov=src --cov-report=html

lint:  ## Ejecuta linters (ruff + mypy)
	ruff check src tests
	mypy src

format:  ## Formatea el código (black + isort)
	black src tests
	isort src tests

## —— Docker ——
docker-build:  ## Construye imágenes Docker
	$(DOCKER_COMPOSE) build --no-cache

docker-up:  ## Inicia contenedores
	$(DOCKER_COMPOSE) up -d

docker-down:  ## Detiene contenedores
	$(DOCKER_COMPOSE) down

## —— Kubernetes ——
k8s-deploy:  ## Despliega en cluster Kubernetes
	helm upgrade --install $(PROJECT_NAME) ./charts \
		--namespace $(PROJECT_NAME) \
		--create-namespace \
		--values ./charts/values-prod.yaml

k8s-logs:  ## Muestra logs de los pods
	kubectl logs -l app.kubernetes.io/name=$(PROJECT_NAME) --tail=100 -f

## —— CI/CD ——
ci-validate:  ## Valida configuración CI (pre-commit)
	pre-commit run --all-files

ci-security:  ## Escaneo de seguridad
	trivy fs --security-checks vuln,config .

## —— Utils ——
clean:  ## Limpia archivos temporales
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .coverage htmlcov

.PHONY: help install install-prod env-file run test lint format docker-build docker-up docker-down k8s-deploy k8s-logs ci-validate ci-security clean
