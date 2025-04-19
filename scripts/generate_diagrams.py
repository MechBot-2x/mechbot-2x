#!/usr/bin/env python3
"""
Script para generar diagramas de arquitectura del sistema MechBot 2.0
"""

import os
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

# Configuración
OUTPUT_DIR = os.path.join(os.getcwd(), "docs/architecture")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_architecture_diagram():
    """Genera el diagrama principal de arquitectura"""
    with Diagram("MechBot Architecture",
                filename=os.path.join(OUTPUT_DIR, "architecture"),
                show=False,
                direction="TB"):
        
        with Cluster("Vehicle Integration"):
            obd = EC2("OBD-II Interface")
            can = EC2("CAN Bus")
        
        with Cluster("Processing Layer"):
            lb = ELB("Load Balancer")
            processors = [EC2(f"Processor {i}") for i in range(1, 4)]
        
        db = RDS("Database")
        
        obd >> lb >> processors
        can >> lb
        processors >> db

if __name__ == "__main__":
    print("Generating architecture diagrams...")
    generate_architecture_diagram()
    print(f"Diagrams saved to: {OUTPUT_DIR}")
