# Bienvenido a MechBot 2.0x

```mermaid
flowchart TD
    A[Documentación] --> B[Arquitectura]
    A --> C[Seguridad]
    A --> D[Monitorización]
    A --> E[AI]

Acceso Rápido

    Resumen Técnico

    Índice Completo

    Estructura del Proyecto

Equipo

    DevOps: infra@mechbot.tech

    Seguridad: security@mechbot.tech

    Soporte: support@mechbot.tech
    EOF

## 5. Reconstruir y verificar

```bash
# Limpiar y reconstruir
rm -rf site/
mkdocs build --strict

# Iniciar servidor
mkdocs serve -a 0.0.0.0:8000

6. Verificación final

    Accede a http://localhost:8000

    Verifica que:
        Todos los elementos del menú funcionen

        Los diagramas Mermaid se rendericen correctamente

        No haya errores 404 en la consola del servidor

Solución para problemas persistentes:

Si algún enlace no funciona:
bash

# Buscar el archivo problemático
grep -r "texto-del-enlace" docs/

# Corregir manualmente el enlace
nano docs/ruta/al/archivo.md

Ahora deberías poder ver y navegar por toda la documentación sin problemas.```
