# Sistema Inteligente de Navegación para Drones de Entrega en Quito

## Descripción del proyecto

Este proyecto presenta el diseño y simulación de un sistema inteligente para la navegación de un vehículo aéreo no tripulado (drone) destinado a la entrega de paquetes entre agencias de una empresa de logística ubicada en la ciudad de Quito, Ecuador.

El sistema utiliza diferentes sensores para monitorear las condiciones del entorno y del propio vehículo, permitiendo tomar decisiones de navegación de forma autónoma. Además, se implementa un modelo de aprendizaje automático que puede apoyar en la toma de decisiones operativas.

El proyecto también incluye una simulación de comunicación entre un operador humano y el drone mediante comandos simples en español utilizando técnicas básicas de procesamiento de lenguaje natural.

---

# Objetivos del proyecto

Diseñar y simular un sistema inteligente que permita a un drone:

- Navegar entre sucursales de una empresa de paquetería
- Detectar condiciones ambientales adversas
- Gestionar su nivel de batería
- Registrar información sobre los paquetes transportados
- Tomar decisiones automáticas ante situaciones de riesgo
- Comunicarse con un operador mediante comandos en lenguaje natural

---

# Sensores utilizados en el sistema

El vehículo aéreo no tripulado considera información proveniente de los siguientes sensores:

- Altitud
- Nivel de batería
- Detección de lluvia
- Velocidad
- Dirección del viento
- Temperatura
- Detección de otros vehículos aéreos
- Detección de obstáculos

Estos sensores permiten evaluar las condiciones del entorno y determinar si el drone puede continuar su trayecto o debe regresar a la sucursal más cercana.

---

# Arquitectura del sistema

El sistema propuesto está compuesto por cuatro componentes principales:

### 1. Generación del dataset

Se genera un dataset simulado que contiene información sobre:

- Condiciones ambientales
- Estado del drone
- Información del paquete
- Decisiones operativas

Este dataset sirve como base para entrenar modelos de aprendizaje supervisado.

---

### 2. Modelos de aprendizaje supervisado

Se evaluaron distintos modelos de clasificación para apoyar en la toma de decisiones del sistema:

- Regresión Logística
- Árboles de decisión
- Máquinas de soporte vectorial (SVM)
- Redes neuronales multicapa (MLP)

Estos modelos permiten analizar diferentes condiciones del entorno y predecir decisiones como continuar el vuelo o regresar a la base.

---

### 3. Máquina de Estados Finitos (FSM)

El comportamiento del drone se modela mediante una máquina de estados finitos que representa los diferentes estados del sistema.

Entre los estados principales se encuentran:

- Encendido
- Verificación de batería
- Listo para despegue
- Navegación
- Entrega de paquete
- Retorno a la base
- Apagado

Este modelo permite estructurar el comportamiento del drone de manera organizada y predecible.

---

### 4. Comunicación mediante Procesamiento de Lenguaje Natural

Se diseñó un pequeño lenguaje de comandos en español que permite al operador consultar el estado del drone mediante una simulación de chat.

Algunos comandos disponibles son:

- **estado**: indica la situación actual del drone
- **bateria**: muestra el nivel de batería
- **sensores**: informa las condiciones del entorno
- **carga**: muestra el peso del paquete transportado
- **cancelar**: cancela la misión actual
- **salir**: finaliza la comunicación

La simulación se ejecuta en Python mediante una interfaz simple de terminal.

---
proyecto_dron_quito_ia
│
├── src
│ ├── 01_generar_dataset.py
│ ├── 02_modelos_supervisados.py
│ ├── 03_pln_chat.py
│ ├── 04_fsm_dron.py
│
├── data
│ └── simulated
│ └── dataset_drone_quito.csv
│
├── figures
│
├── report
│
└── requirements.txt


---

# Instalación

Se recomienda utilizar Python 3.10 o superior.

pip install -r requirements.txt

# Ejecución del proyecto

### Generar dataset

python src/01_generar_dataset.py

Esto creará un archivo CSV con los datos simulados.

---

### Entrenar modelos de aprendizaje automático

python src/02_modelos_supervisados.py

El programa mostrará métricas como:

- Accuracy
- Precision
- Recall
- F1 Score

---

### Simulación de comunicación con el drone


python src/03_pln_chat.py


Permite interactuar con el drone mediante comandos en español.

---

### Simulación de la máquina de estados


python src/04_fsm_dron.py


El sistema mostrará en consola los cambios de estado del drone durante la simulación.

---

# Consideraciones éticas

La implementación de drones autónomos para entregas plantea varios aspectos éticos que deben ser considerados:

1. Seguridad pública  
El uso de drones en zonas urbanas puede representar riesgos para las personas si ocurre un fallo técnico.

2. Privacidad  
Los drones pueden capturar imágenes o video durante su trayecto, por lo que debe protegerse la privacidad de los ciudadanos.

3. Responsabilidad tecnológica  
Es necesario establecer responsabilidades claras en caso de accidentes o fallos del sistema.

4. Impacto laboral  
La automatización de sistemas de entrega podría afectar empleos relacionados con la logística y transporte.

5. Uso responsable de inteligencia artificial  
Los sistemas de IA deben diseñarse de forma transparente, segura y auditables.
