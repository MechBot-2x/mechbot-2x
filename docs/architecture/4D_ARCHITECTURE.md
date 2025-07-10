📄 `architecture/4D_ARCHITECTURE.md`
```mermaid
flowchart_TD
    A[Vehicle] -->|CAN FD 2.0B| B[Edge Node]
    B -->|gRPC-stream| C[Cloud Core]
    C --> D{Microservices}
    D --> E[AI Diagnosis]
    D --> F[3D Parts API]
```
