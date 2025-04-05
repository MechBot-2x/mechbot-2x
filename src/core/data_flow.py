# Importación de módulos y clases necesarios
import os
import sys

from some_module import CANBusReader, GRPCHandler, K8sOrchestrator, ThreeDVisualizer


class DataFlow4D:
    """
    Clase para gestionar el flujo de datos a través de diferentes capas.

    Esta clase define una arquitectura en capas para el procesamiento de señales de vehículos,
    donde cada capa es responsable de una etapa específica de transformación.
    """

    def __init__(self):
        """
        Inicializa las capas del flujo de datos.

        Cada capa se instancia como un atributo del diccionario 'layers',
        mapeando un nombre descriptivo a su respectiva clase.
        """
        self.layers = {
            'physical': CANBusReader(),  # Lector de datos del bus CAN (capa física)
            'platform': K8sOrchestrator(),  # Orquestador de Kubernetes (capa de plataforma)
            'services': GRPCHandler(),  # Manejador de comunicación gRPC (capa de servicios)
            'app': ThreeDVisualizer()  # Visualizador 3D (capa de aplicación)
        }

    def process(self, vehicle_signal):
        """
        Procesa una señal del vehículo a través de todas las capas definidas.

        Args:
            vehicle_signal: La señal del vehículo a procesar.

        Returns:
            Una lista con los resultados de la transformación de la señal en cada capa.
        """
        return [layer.transform(vehicle_signal)
                for layer in self.layers.values()]

# Asegurar que no haya espacios en blanco al final del archivo
