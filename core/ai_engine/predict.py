import onnxruntime as ort

class MechBotPredictor:
    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(model_path)
        
    async def predict(self, input_data: dict) -> dict:
        inputs = {
            'can_data': input_data['telemetry'],
            'oem_codes': input_data['error_codes']
        }
        outputs = self.session.run(None, inputs)
        return {
            'fault_probability': outputs[0].tolist(),
            'recommended_actions': outputs[1]
        }
