# MechBot 2.0x - Makefile

.PHONY: install run test docker-build docker-up docker-down lint format

install:
	@echo "Instalando dependencias..."
	pip install -r requirements.txt

run:
	@echo "Iniciando MechBot API..."
	uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

test:
	@echo "Ejecutando tests..."
	python -m pytest tests/ -v

docker-build:
	@echo "Construyendo imagen Docker..."
	docker build -t mechbot-2x:latest .

docker-up:
	@echo "Iniciando contenedores..."
	docker-compose up -d

docker-down:
	@echo "Deteniendo contenedores..."
	docker-compose down

lint:
	@echo "Ejecutando linter..."
	flake8 api/ --max-line-length=88

format:
	@echo "Formateando código..."
	black api/
	isort api/

clean:
	@echo "Limpiando archivos temporales..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .pytest_cache
