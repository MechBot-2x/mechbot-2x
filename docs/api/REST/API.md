## **4. API Documentation**
## Vehicle Telemetry API
`POST /api/v2/telemetry`
```json
Request:
{
  "vin": "1HGCM82633A123456",
  "params": {
    "rpm": 3200,
    "temp": 92
  }
}
```
```

📄 `docs/api/GRPC_PROTOCOLS.md`
```protobuf
// proto/diagnosis/v1/service.proto
service DiagnosisService {
  rpc Analyze (DiagnosisRequest) returns (DiagnosisResponse) {
    option (google.api.http) = {
      post: "/v1/diagnosis"
      body: "*"
    };
  }
}
```
