# **Flujo de Datos 4D - Arquitectura Avanzada**  
**Documento:** `architecture/4D_DATA_FLOW.md`  
**Ubicación Física:** `/mechbot-2x/architecture/4D_DATA_FLOW.md`  
**Responsable:** Equipo de Ingeniería de Plataforma  

## **Diagrama de Flujo Mejorado**  
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ffdfd3', 'edgeLabelBackground':'#fff'}}}%%
flowchart_TD
    subgraph FÍSICA["CAPA FÍSICA (Hardware)"]
        A[<img src='https://cdn-icons-png.flaticon.com/512/1086/1086741.png' width='30'/> Kubernetes Nodes]
        B[<img src='https://cdn-icons-png.flaticon.com/512/3014/3014486.png' width='30'/> NVIDIA Jetson]
        C[<img src='https://cdn-icons-png.flaticon.com/512/2785/2785473.png' width='30'/> RPi Cluster]
    end

    subgraph PLATAFORMA["CAPA PLATAFORMA (Orquestación)"]
        D[<img src='https://cdn-icons-png.flaticon.com/512/3601/3601624.png' width='30'/> Docker]
        E[<img src='https://cdn-icons-png.flaticon.com/512/6134/6134346.png' width='30'/> Helm]
        F[<img src='https://cdn-icons-png.flaticon.com/512/888/888054.png' width='30'/> Istio]
    end

    subgraph SERVICIOS["CAPA SERVICIOS (Backend)"]
        G[<img src='https://cdn-icons-png.flaticon.com/512/2620/2620971.png' width='30'/> API REST]
        H[<img src='https://cdn-icons-png.flaticon.com/512/6134/6134346.png' width='30'/> gRPC]
        I[<img src='https://cdn-icons-png.flaticon.com/512/2777/2777154.png' width='30'/> Kafka]
    end

    subgraph APLICACIÓN["CAPA APLICACIÓN (Frontend)"]
        J[<img src='https://cdn-icons-png.flaticon.com/512/2103/2103633.png' width='30'/> Dashboard 3D]
        K[<img src='https://cdn-icons-png.flaticon.com/512/2328/2328965.png' width='30'/> Diagnóstico IA]
        L[<img src='https://cdn-icons-png.flaticon.com/512/2933/2933245.png' width='30'/> Telemetría]
    end

    FÍSICA -->|Envía métricas| PLATAFORMA
    PLATAFORMA -->|Despliega| SERVICIOS
    SERVICIOS -->|Alimenta| APLICACIÓN
    APLICACIÓN -->|Control| FÍSICA

    style FÍSICA fill:#f9cb9c,stroke:#e69138
    style PLATAFORMA fill:#b6d7a8,stroke:#6aa84f
    style SERVICIOS fill:#a2c4c9,stroke:#3d85c6
    style APLICACIÓN fill:#d5a6bd,stroke:#a64d79
```

## **Archivos de Configuración Clave**  

| Capa | Archivo | Ubicación |  
|------|---------|-----------|  
| **Física** | `hardware/cluster-config.yaml` | `/infra/hardware/` |  
| **Plataforma** | `values-4d.yaml` | `/deploy/helm/` |  
| **Servicios** | `services-pipeline.conf` | `/config/kafka/` |  
| **Aplicación** | `3d-engine-params.json` | `/app/src/engine/` |  

## **Comandos de Monitoreo**  

```bash
# Monitoreo integral (requiere acceso kubectl)
./scripts/monitor-4d.sh \
    --namespace=mechbot-prod \
    --kafka-topic=vehicle_metrics_v3 \
    --grpc-endpoint=mechbot-grpc:50051
```

**Documentación Relacionada:**  
📌 [Protocolo de Comunicación 4D](architecture/4D_COMMS_PROTOCOL.md)  
📌 [Benchmarks de Rendimiento](performance/4D_BENCHMARKS.md)  

**Equipo de Ingeniería MechBot**  
🛠️ **Mantenedores:** @devops-lead @platform-eng  
🔗 **Repositorio:** [github.com/mechmind-dwv/mechbot-2x](https://github.com/mechmind-dwv/mechbot-2x)  
📅 **Última Actualización:** 2025-04-20
