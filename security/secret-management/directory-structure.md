## **2. Estructura de Directorios Seguros**
**Ubicación:** `security/secret-management/directory-structure.md`

```
mechbot-2x/
├── secrets/                   # Todos los secretos cifrados
│   ├── prod/
│   │   ├── db.enc.yaml        # Cifrado con SOPS/KMS
│   │   └── api-keys.enc.json  
│   └── staging/
│       └── db.enc.yaml
└── templates/
    └── secret-template.yaml   # Helm/K8s secrets
```

**Políticas:**
- Extensiones `.enc.*` para archivos cifrados
- Permisos `chmod 600` para archivos locales
- `.gitignore` que excluya `**/*.enc.*`
