# **Configuración de Dependabot para MechBot 2.0x**  
**Archivo:** `.github/dependabot.yml`  
**Responsable:** Equipo de Ingeniería - DevOps  

## **Configuración Completa**  
```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "08:00"
      timezone: "America/Santiago"
    reviewers:
      - "@mechmind-dwv/team-core"
    commit-message:
      prefix: "chore(deps)"
      prefix-development: "chore(deps-dev)"

  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    allow:
      - dependency-name: "numpy"
        dependency-type: "production"
      - dependency-name: "pytest*"
        dependency-type: "development"

  - package-ecosystem: "docker"
    directory: "/dockerfiles"
    schedule:
      interval: "monthly"
    ignore:
      - dependency-name: "python*"
        versions: ["3.7", "3.8"]

  - package-ecosystem: "github-actions"
    directory: "/.github/workflows"
    schedule:
      interval: "monthly"
    labels:
      - "dependencies"
      - "security"
```

## **Estructura de la Configuración**  

### **1. Ecosistemas Soportados**  
| Ecosistema       | Frecuencia  | Ubicación                |  
|------------------|-------------|--------------------------|  
| npm              | Semanal     | Raíz del proyecto        |  
| pip              | Semanal     | requirements.txt         |  
| Docker           | Mensual     | /dockerfiles             |  
| GitHub Actions   | Mensual     | /.github/workflows       |  

### **2. Reglas Especiales**  
- **Exclusiones**:  
  ```yaml
  ignore:
    - dependency-name: "legacy-package"
      versions: ["1.x"]
  ```
- **Aprobaciones**:  
  ```yaml
  reviewers:
    - "@mechmind-dwv/security-team"
  ```

### **3. Política de Actualizaciones**  
- **Horario**: Lunes 08:00 AM (GMT-4)  
- **Notificaciones**: Slack #dependabot-alerts  
- **Pruebas**:  
  ```yaml
  open-pull-requests-limit: 5
  rebase-strategy: "disabled"
  ```

## **Documentación Relacionada**  
📌 [Política de Dependencias](security/DEPENDENCY-POLICY.md)  
📌 [Proceso de Actualización](docs/development/UPDATE-PROCESS.md)  

**Firma:**  
Equipo de Plataforma - MechBot 2.0x  
🛠️ Última actualización: 2025-04-05  
🔗 [Convención de Commits](https://github.com/mechmind-dwv/mechbot-2x/wiki/Commit-Standards)
