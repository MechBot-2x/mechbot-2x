# Ejemplo en src/core/data_flow.py
class DataFlow4D:
    def __init__(self):
        self.layers = {
            'physical': CANBusReader(),
            'platform': K8sOrchestrator(),
            'services': GRPCHandler(),
            'app': ThreeDVisualizer()
        }
    
    def process(self, vehicle_signal):
        return [layer.transform(signal) 
                for layer in self.layers.values()]
