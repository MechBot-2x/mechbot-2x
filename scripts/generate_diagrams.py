# Documentación Profesional para `generate_diagrams.py`

## Propósito
Script de generación de diagramas de arquitectura para MechBot 2.0 que automatiza la creación de documentación técnica visual mediante programación.

## Estructura del Comando

```bash
python scripts/generate_diagrams.py \
    --output-dir docs/architecture \
    --format png svg pdf \
    --theme dark \
    --diagrams all \
    --validate \
    --log-level INFO
```

## Parámetros de Configuración

| Parámetro        | Valores Permitidos           | Default       | Descripción |
|------------------|-----------------------------|--------------|-------------|
| `--output-dir`   | Cualquier path válido        | `docs/architecture` | Directorio de salida para los diagramas |
| `--format`       | png, svg, pdf, jpg          | png          | Formatos de salida (múltiples permitidos) |
| `--theme`        | light, dark, neutral        | light        | Esquema de colores |
| `--diagrams`     | all, arch, flow, sequence   | all          | Tipos de diagramas a generar |
| `--validate`     | flag (sin valor)             | False        | Valida los recursos antes de generar |
| `--log-level`    | DEBUG, INFO, WARNING, ERROR | INFO         | Nivel de detalle del logging |

## Variables de Entorno Opcionales

```bash
export DIAGRAMS_CACHE_DIR="/tmp/diagrams_cache"  # Custom cache location
export GRAPHVIZ_PATH="/usr/local/bin/graphviz"   # Custom Graphviz path
```

## Ejemplos de Uso Avanzado

1. **Generación para CI/CD**:
```bash
python scripts/generate_diagrams.py \
    --output-dir ${GITHUB_WORKSPACE}/docs \
    --format png \
    --theme neutral \
    --log-level WARNING
```

2. **Generación selectiva con validación**:
```bash
python scripts/generate_diagrams.py \
    --diagrams arch flow \
    --validate \
    --format svg pdf
```

3. **Modo desarrollo con debug**:
```bash
python scripts/generate_diagrams.py \
    --output-dir ./temp_docs \
    --theme dark \
    --log-level DEBUG
```

## Estructura del Script (Resumen)

```python
# Core Components
class DiagramGenerator:
    """Factory para la generación de diagramas"""
    
    def __init__(self, config: DiagramConfig):
        self._validate_environment()
        self._setup_graphviz()
    
    def generate(self):
        """Coordina el proceso de generación"""
        self._load_resources()
        self._create_diagrams()
        self._export_artifacts()

# Technical Implementation Details
- Usa el patrón Factory Method para los diagramas
- Implementa validación de dependencias con Graphviz
- Genera metadata técnica en formato Exif
- Soporta inyección de dependencias para testing
```

## Integración con el Sistema

1. **Dependencias**:
```text
diagrams>=0.23.3
graphviz>=0.20.1
Pillow>=9.0.0 (para manipulación de imágenes)
```

2. **Estructura de Archivos**:
```text
scripts/
├── generate_diagrams.py
└── diagram_templates/
    ├── architecture.py
    └── data_flow.py
resources/
└── icons/
    ├── aws/
    └── custom/
```

3. **Output Esperado**:
```text
docs/architecture/
├── mechbot_architecture.png
├── mechbot_architecture.svg
├── data_flow.png
└── metadata.json
```

## Best Practices Recomendadas

1. **En Entornos CI**:
```yaml
- name: Generate Architecture Diagrams
  run: |
    sudo apt-get install -y graphviz
    pip install diagrams pillow
    python scripts/generate_diagrams.py --format png --theme light
```

2. **Pre-commit Hook**:
```yaml
- repo: local
  hooks:
    - id: generate-diagrams
      name: Update architecture diagrams
      entry: python scripts/generate_diagrams.py --format svg
      language: system
      files: ^(src|config)/.*\.py$
```

## Troubleshooting

| Error | Causa Probable | Solución |
|-------|---------------|----------|
| `GraphvizNotFound` | Graphviz no instalado | `sudo apt-get install graphviz` |
| `MissingIcons` | Ruta incorrecta de íconos | Verificar estructura de `resources/` |
| `ThemeError` | Tema no soportado | Usar `--theme light/dark/neutral` |

¿Necesitas que desarrolle algún aspecto específico con más detalle o que incluya ejemplos de implementación para algún caso de uso particular?