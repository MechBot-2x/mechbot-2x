# **Documentación de Monitorización en Tiempo Real - MechBot 2.0x**

## **Archivo Principal**
**Nombre:** `REALTIME_DASHBOARDS.md`  
**Ubicación:** `/monitoring/REALTIME_DASHBOARDS.md`  
**Responsable:** Equipo de Observabilidad - DevOps

## **Arquitectura de Monitorización 4D**

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#fff2cc'}}}%%
flowchart_TD
    A[<img src='https://cdn-icons-png.flaticon.com/512/1086/1086741.png' width='25'/> Sensores Físicos] --> B[<img src='https://cdn-icons-png.flaticon.com/512/3601/3601624.png' width='25'/> Prometheus]
    B --> C[<img src='https://cdn-icons-png.flaticon.com/512/2620/2620971.png' width='25'/> Grafana]
    C --> D[<img src='https://cdn-icons-png.flaticon.com/512/2103/2103633.png' width='25'/> Dashboard 3D]
    
    style A fill:#f9cb9c,stroke:#e69138
    style B fill:#b6d7a8,stroke:#6aa84f
    style C fill:#a2c4c9,stroke:#3d85c6
    style D fill:#d5a6bd,stroke:#a64d79
```

## **Componentes Clave**

### **1. Recolección de Datos**
**Archivos de Configuración:**
- `monitoring/prometheus/prometheus.yml`
- `monitoring/otel-collector/config.yaml`

**Métricas Principales:**
```yaml
# Fragmento de prometheus.yml
scrape_configs:
  - job_name: 'vehicle_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['canbus-exporter:9100', 'ia-inference:9110']
```

### **2. Procesamiento en Tiempo Real**
**Pipeline:**
```bash
# Comando para iniciar el pipeline
./scripts/start-stream-processing.sh \
    --kafka-brokers=kafka1:9092,kafka2:9092 \
    --prometheus-url=http://prometheus:9090
```

### **3. Visualización**
**Dashboards Disponibles:**
1. **Físico**: `dashboards/hardware-3d.json`
2. **Rendimiento IA**: `dashboards/ml-performance.json`
3. **Telemetría**: `dashboards/vehicle-telemetry.json`

## **Configuración de Alertas**

**Archivo:** `monitoring/alert-rules.yml`
```yaml
groups:
- name: vehicle-alerts
  rules:
  - alert: HighCANBusLatency
    expr: rate(canbus_latency_seconds[1m]) > 0.5
    labels:
      severity: 'critical'
    annotations:
      summary: "Alta latencia en bus CAN ({{ $value }}s)"
```

## **Comandos Esenciales**

```bash
# Ver estado del sistema
make monitoring-status

# Acceder a Grafana localmente
kubectl port-forward svc/grafana 3000:3000 -n monitoring

# Probar exportadores
curl http://localhost:9100/metrics | grep canbus
```

## **Documentación Relacionada**
📌 [Política de Retención de Métricas](monitoring/RETENTION_POLICY.md)  
📌 [Guía de Configuración de Alertas](monitoring/ALERTING_GUIDE.md)

**Equipo de Observabilidad MechBot**  
📊 **Contacto:** [observability@mechbot.tech](mailto:observability@mechbot.tech)  
🔧 **Última Actualización:** 2025-04-25  
🌐 **URL Dashboard:** `https://grafana.mechbot.tech/d/4d-realtime`
