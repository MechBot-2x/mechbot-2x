# **Documentación de Seguridad - MechBot 2.0x**  
**Ubicación:** `docs/security/GUIDELINES.md`  
**Equipo de Ingeniería - Security Team**  
**Versión:** 2.0.1 | **Última actualización:** 2025-04-03  

---

## **1. Gestión de Secretos y Credenciales**  
**Archivos clave:**  
- `.vault/env.encrypted` (Cifrado con Ansible Vault)  
- `kubernetes/secrets/templates/secret-template.yaml`  

### **Recomendaciones:**  
1. **Nunca almacenar en claro**:  
   ```bash
   # Mal práctica (evitar):
   POSTGRES_PASSWORD=password123  # ❌

   # Buen práctica:
   POSTGRES_PASSWORD=${VAULT:db_prod_password}  # ✅
   ```

2. **Rotación obligatoria**:  
   ```ini
   # En .env.sample
   JWT_SECRET_ROTATION_INTERVAL=30d  # Rotación mensual
   DB_CREDENTIALS_ROTATION=15d       # Rotación quincenal para entornos críticos
   ```

3. **Herramientas recomendadas**:  
   - **HashiCorp Vault** para gestión centralizada  
   - **AWS Secrets Manager** para entornos cloud  
   - **SOPS** para cifrado de archivos (config en `.sops.yaml`)  

---

## **2. Configuración de Red y Comunicaciones**  
**Archivos clave:**  
- `deploy/network/security-groups.prod.yaml`  
- `src/core/security/tls_config.py`  

### **Recomendaciones:**  
| Protocolo | Puertos | Cifrado Requerido |  
|-----------|---------|-------------------|  
| CAN Bus   | -       | TLS 1.3 + MACsec  |  
| gRPC      | 50051   | mTLS con ECDSA    |  
| HTTP/API  | 443     | HSTS + TLS 1.3    |  

**Ejemplo de configuración TLS:**  
```python 
# En tls_config.py
CIPHERS = [
    'TLS_AES_256_GCM_SHA384',
    'TLS_CHACHA20_POLY1305_SHA256'
]
```

---

## **3. Seguridad en Contenedores**  
**Archivos clave:**  
- `dockerfiles/Dockerfile.secure`  
- `kubernetes/policies/pod-security-policy.yaml`  

### **Buenas Prácticas:**  
1. **Usar usuarios no-root**:  
   ```dockerfile
   FROM alpine:3.18
   RUN adduser -D mechbotuser
   USER mechbotuser  # ✅
   ```

2. **Scan de vulnerabilidades**:  
   ```bash
   # En CI/CD (publish.yml)
   - name: Scan image
     uses: aquasecurity/trivy-action@0.9
     with:
       image-ref: ${{ steps.meta.outputs.tags }}
       severity: 'CRITICAL,HIGH'
   ```

3. **Políticas Kubernetes**:  
   ```yaml
   # En pod-security-policy.yaml
   spec:
     readOnlyRootFilesystem: true
     allowPrivilegeEscalation: false
     capabilities:
       drop: ["ALL"]
   ```

---

## **4. Hardening de Bases de Datos**  
**Archivos clave:**  
- `deploy/postgres/postgres-hardening.sql`  
- `config/cassandra/security.yaml`  

### **Configuraciones Críticas:**  
```sql
-- En postgres-hardening.sql
ALTER SYSTEM SET ssl = 'on';
ALTER SYSTEM SET password_encryption = 'scram-sha-256';
CREATE ROLE mechbot_rw WITH LOGIN PASSWORD '${VAULT_DB_PWD}' NOINHERIT;
```

```yaml
# En cassandra/security.yaml
authenticator: PasswordAuthenticator
authorizer: CassandraAuthorizer
role_manager: CassandraRoleManager
```

---

## **5. Monitoreo de Seguridad**  
**Archivos clave:**  
- `monitoring/siem/alerts-rules.yml`  
- `deploy/efk/security-dashboard.ndjson`  

### **Alertas Prioritarias:**  
```yaml
# En alerts-rules.yml
- alert: JWT_Tampering_Attempt
  expr: rate(jwt_failed_attempts[5m]) > 3
  labels:
    severity: critical
  annotations:
    summary: "Posible ataque de fuerza bruta JWT"
```

---

## **6. Auditoría y Cumplimiento**  
**Archivos clave:**  
- `compliance/iso27001-controls.csv`  
- `scripts/security/audit.sh`  

### **Checklist Automatizado:**  
```bash
#!/bin/bash
# En audit.sh
check_ssl() {
  openssl s_client -connect $1:443 | grep "TLSv1.3"
}
check_db_encryption() {
  psql -c "SHOW ssl;" | grep "on"
}
```

---

## **Anexo: Políticas de Emergencia**  
**Ubicación:** `docs/security/INCIDENT_RESPONSE.md`  

| Escenario                | Acción Inmediata                     |  
|--------------------------|--------------------------------------|  
| Fuga de credenciales     | Rotar TODOS los secretos en <1h      |  
| Ataque DDoS              | Activar Cloudflare WAF + Scale Up    |  
| Intrusión DB             | Aislar cluster + Snapshots forenses  |  

**Equipo de Seguridad MechBot 2.0x**  
🔒 `security@mechbot.tech` | 🔗 [Convenciones de Seguridad](https://github.com/mechmind-dwv/mechbot-2x/wiki/Security)  

*Documentación verificada por: @david-security-lead @maria-compliance-officer*
