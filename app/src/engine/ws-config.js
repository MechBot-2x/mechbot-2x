const config = {  
  protocols: ['v3.proto'],  
  binaryType: "arraybuffer",  
  reconnectInterval: 5000,  
  maxRetries: 5  
};  
``` 

## **Flujo de Mensajería**  
```mermaid  
sequenceDiagram  
    participant Vehicle  
    participant Platform  
    participant Services  
    participant App  

    Vehicle->>Platform: Señales CAN (RAW)  
    Platform->>Services: gRPC-stream (Protobuf)  
    Services->>App: WebSocket (JSON)  
    App->>Services: Comandos (Avro)  
    Services->>Platform: ACK (Protobuf)  
    Platform->>Vehicle: Confirmación CAN
