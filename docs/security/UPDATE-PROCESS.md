# **Configuración Oficial de Dependabot - MechBot 2.0x**

## **Nombre del Documento**
**Título:** "Política de Gestión de Dependencias Automatizada"  
**Nombre del archivo:** `dependabot.yml`  
**Ubicación en el proyecto:** `.github/dependabot.yml`

## **Estructura del Proyecto**
```
mechbot-2x/
├── .github/
│   ├── workflows/
│   ├── dependabot.yml       # Este archivo (ubicación principal)
│   └── SECURITY.md
├── docs/
│   └── security/
│       └── DEPENDENCY-POLICY.md  # Documentación relacionada
```

## **Características Clave**
1. **Alcance**: Control centralizado de actualizaciones para:
   - Paquetes NPM/Node.js
   - Dependencias Python (pip)
   - Imágenes Docker
   - Acciones de GitHub

2. **Flujo de Trabajo**:
   - Ejecución semanal/mensual programada
   - Notificaciones al equipo core
   - Integración con revisión de seguridad

3. **Documentación Asociada**:
   - `DEPENDENCY-POLICY.md`: Reglas de actualización
   - `UPDATE-PROCESS.md`: Procedimiento de validación

**Equipo de Ingeniería MechBot**  
📍 Este archivo debe mantenerse en la ruta exacta `.github/dependabot.yml` para funcionamiento correcto del sistema de GitHub.  
📅 Última revisión de políticas: Abril 2025 (v2.1.0)
