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
