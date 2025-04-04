# =============================================
# Makefile - MechBot 2.0x
# Equipo de Ingeniería - Automatización de CI/CD
# Versión: 2.1.8
# =============================================

# —— Configuración Base ——
PROJECT_NAME := mechbot-2x
PYTHON := python3.10
PIP := $(PYTHON) -m pip
DOCKER := docker
DOCKER_COMPOSE := docker-compose -f deployments/docker-compose.yml
KUBECTL := kubectl
HELM := helm

# —— Variables de Entorno ——
ENV_FILE := .env
include $(ENV_FILE)
export $(shell sed 's/=.*//' $(ENV_FILE))

# —— Configuración de Color ——
GREEN := \033[0;32m
BLUE := \033[0;34m
RED := \033[0;31m
BOLD := \033[1m
NC := \033[0m

# —— Help ——
.PHONY: help
help:  ## Muestra menú de ayuda interactivo
	@echo "\n$(BOLD)MechBot 2.0x - Comandos Disponibles$(NC)\n"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(BLUE)%-25s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
	@echo "\nEjemplo: $(BOLD)make docker-build$(NC)\n"

# —— Entorno de Desarrollo ——
.PHONY: setup
setup: venv env-file install-dev  ## Configura entorno completo (venv + dependencias)

venv:  ## Crea entorno virtual
	@echo "$(GREEN)Creando entorno virtual...$(NC)"
	$(PYTHON) -m venv .venv
	@echo "Ejecuta: $(BOLD)source .venv/bin/activate$(NC)"

env-file:  ## Genera archivo .env de ejemplo
	@cp .env.sample .env
	@echo "$(GREEN)✓ Archivo .env creado$(NC)"
	@echo "Recuerda configurar tus variables en $(BOLD).env$(NC)"

.PHONY: install-dev
install-dev:  ## Instala dependencias de desarrollo
	@echo "$(GREEN)Instalando dependencias...$(NC)"
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev,ml,test]"
	pre-commit install

.PHONY: install-prod
install-prod:  ## Instala solo dependencias de producción
	$(PIP) install --no-deps -e .

# —— Desarrollo ——
.PHONY: run
run:  ## Inicia servidor local con autoreload
	uvicorn src.main:app --reload --host $(API_HOST) --port $(API_PORT)

.PHONY: test
test:  ## Ejecuta tests con cobertura
	$(PYTHON) -m pytest -v \
		--cov=src \
		--cov-report=html \
		--cov-report=xml:coverage.xml \
		--junitxml=test-results.xml

.PHONY: lint
lint:  ## Ejecuta análisis estático de código
	@echo "$(GREEN)Ejecutando linters...$(NC)"
	ruff check src tests
	mypy src
	bandit -r src -c pyproject.toml

.PHONY: format
format:  ## Formatea código automáticamente
	@echo "$(GREEN)Formateando código...$(NC)"
	black src tests
	isort src tests
	ruff --select I --fix src tests

# —— Docker ——
.PHONY: docker-build
docker-build:  ## Construye imágenes Docker
	@echo "$(GREEN)Construyendo imágenes...$(NC)"
	$(DOCKER_COMPOSE) build \
		--build-arg PYTHON_VERSION=$(PYTHON) \
		--no-cache

.PHONY: docker-up
docker-up:  ## Inicia todos los servicios
	@echo "$(GREEN)Iniciando contenedores...$(NC)"
	$(DOCKER_COMPOSE) up -d --remove-orphans

.PHONY: docker-down
docker-down:  ## Detiene y limpia contenedores
	@echo "$(RED)Deteniendo contenedores...$(NC)"
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

# —— Kubernetes ——
.PHONY: k8s-deploy
k8s-deploy:  ## Despliega en cluster Kubernetes
	@echo "$(GREEN)Desplegando en Kubernetes...$(NC)"
	$(HELM) upgrade --install $(PROJECT_NAME) ./deployments/helm \
		--namespace $(PROJECT_NAME) \
		--create-namespace \
		--values ./deployments/helm/values-$(ENV).yaml \
		--atomic \
		--timeout 5m

.PHONY: k8s-logs
k8s-logs:  ## Muestra logs en tiempo real
	$(KUBECTL) logs -l app.kubernetes.io/name=$(PROJECT_NAME) \
		--namespace $(PROJECT_NAME) \
		--tail=100 -f

# —— CI/CD ——
.PHONY: ci-validate
ci-validate: lint test  ## Valida código antes de commit
	@echo "$(GREEN)Validación completada!$(NC)"

.PHONY: ci-security
ci-security:  ## Escaneo de seguridad completo
	trivy fs --security-checks vuln,config,secret .
	grype dir:.

# —— Utilitarios ——
.PHONY: clean
clean:  ## Limpia archivos temporales
	@echo "$(GREEN)Limpieza de archivos...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .coverage coverage.xml htmlcov test-results.xml
	$(DOCKER) system prune -f

.PHONY: generate-diagrams
generate-diagrams:  ## Genera diagramas de arquitectura
	$(PYTHON) tools/generate_diagrams.py \
		--input docs/architecture/specs \
		--format mermaid \
		--output docs/architecture/diagrams

# —— Meta Targets ——
.DEFAULT_GOAL := help
