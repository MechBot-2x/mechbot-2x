import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Text } from '@react-three/drei';

/**
 * Componente EngineModel - Visualizador 3D de motor vehicular
 * @param {Object} props - Propiedades del componente
 * @param {string} props.faultCode - Código de falla OBD-II
 * @param {Object} props.telemetry - Datos de telemetría
 */
const EngineModel = ({ faultCode, telemetry = {} }) => {
  // Mapa de colores basado en códigos de falla
  const getColorMap = (code) => {
    const criticalCodes = ['P0300', 'P0172', 'P0420'];
    const warningCodes = ['P0101', 'P0120'];
    
    if (criticalCodes.includes(code)) {
      return { engine: '#ff4444', parts: '#ff0000' }; // Rojo para crítico
    } else if (warningCodes.includes(code)) {
      return { engine: '#ffaa00', parts: '#ff5500' }; // Naranja para advertencia
    }
    return { engine: '#00aaff', parts: '#0088cc' }; // Azul para normal
  };

  const colorMap = getColorMap(faultCode);

  return (
    <div style={{ width: '100%', height: '400px', border: '1px solid #ccc' }}>
      <Canvas camera={{ position: [5, 5, 5], fov: 50 }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[10, 10, 5]} intensity={1} />
        
        {/* Bloque principal del motor */}
        <mesh position={[0, 0, 0]}>
          <boxGeometry args={[3, 2, 2]} />
          <meshStandardMaterial 
            color={colorMap.engine} 
            metalness={0.7}
            roughness={0.3}
          />
        </mesh>

        {/* Cilindros */}
        {[0, 1, 2, 3].map((i) => (
          <mesh key={i} position={[-1 + i * 0.66, 1, 0]}>
            <cylinderGeometry args={[0.3, 0.3, 1, 16]} />
            <meshStandardMaterial 
              color={faultCode === 'P0300' ? '#ff0000' : '#888888'} 
              emissive={faultCode === 'P0300' ? '#ff0000' : '#000000'}
              emissiveIntensity={0.3}
            />
          </mesh>
        ))}

        {/* Texto informativo */}
        <Text
          position={[0, -2, 0]}
          color="white"
          fontSize={0.5}
          anchorX="center"
          anchorY="middle"
        >
          {`Código: ${faultCode || 'N/A'}`}
        </Text>

        {telemetry.rpm && (
          <Text
            position={[0, -2.5, 0]}
            color="#00ff00"
            fontSize={0.3}
            anchorX="center"
            anchorY="middle"
          >
            {`RPM: ${telemetry.rpm}`}
          </Text>
        )}

        <OrbitControls enableZoom={true} enablePan={true} />
      </Canvas>
    </div>
  );
};

export default EngineModel;
