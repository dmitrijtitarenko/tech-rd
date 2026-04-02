---
name: Hardware, IoT, and Robotics Research
description: >
  Embedded systems, RISC-V, edge AI, ROS, sensor fusion, chip design, FPGA, IoT platforms.
  Address "embedded system for", "IoT platform comparison", "robotics framework", "RISC-V advantage", "edge AI", "FPGA vs ASIC" questions.
  Evaluate power consumption, real-time capability, cost per unit, and development ecosystem.
  Critical for IoT products, embedded systems, and robotics projects.
---

# Hardware, IoT, and Robotics Research Domain

## Overview

Hardware, IoT, and robotics research bridges physical systems with digital intelligence. This domain encompasses embedded systems (constrained processors), edge AI (running neural nets on devices), and robotic platforms (integrating sensors, actuators, and control).

Effective research here means understanding: which microcontroller/SoC meets your power and performance budget? How do you choose between custom silicon (ASIC), FPGAs, and commodity hardware? What's the realistic cost and timeline for robotics development?

## Key Research Dimensions

**Embedded Systems & Processors**
- Microcontrollers: ARM Cortex-M (STM32, nRF52), RISC-V, ESP32
- System-on-Chip (SoC): Qualcomm, MediaTek, Apple silicon
- RISC-V: Open-source ISA, low cost, customizable
- Performance tier: Throughput, memory, power consumption
- Real-time capability: Hard real-time (deterministic) vs soft real-time
- Cost: Per-unit pricing at scale (1k, 10k, 100k volumes)

**IoT Platforms & Connectivity**
- Wireless: WiFi, Bluetooth, LoRaWAN, Cellular (4G/5G), NB-IoT, LTE-M
- Range vs power tradeoff: WiFi (close, high power) vs LoRa (long range, low power)
- Cloud platforms: Azure IoT, AWS IoT Core, Google Cloud IoT
- Edge computing: Processing locally vs sending to cloud
- Protocol standards: MQTT, CoAP, AMQP for message passing
- Device management: Provisioning, updates, troubleshooting

**Edge AI & On-Device ML**
- Model optimization: Quantization, pruning, knowledge distillation
- Inference engines: TensorFlow Lite, ONNX Runtime, TVM
- Hardware acceleration: TPU Edge, Neural Engine, Coral
- Latency constraints: Real-time inference on constrained devices
- Power efficiency: Inference per watt metrics
- Model size: Fitting models in device memory (typically MB, not GB)

**Robotics Frameworks & Platforms**
- ROS (Robot Operating System): Distributed messaging, simulation (Gazebo)
- ROS 2: Modern rewrite with DDS, real-time support
- Middleware: Communication between robot components
- Simulation: Testing algorithms without hardware
- Sensor integration: Camera, lidar, IMU fusion
- Motion planning: Collision avoidance, path finding

**Hardware Customization & Design**
- ASIC: Custom silicon, high NRE cost, low unit cost at scale
- FPGA: Flexible, programmable, moderate unit cost, power-efficient
- Custom PCB: Circuit design, manufacturing, assembly
- Prototyping tools: Arduino, Raspberry Pi for early development
- Manufacturing: Sourcing, assembly, testing at scale
- Supply chain: Chip shortages, lead times, cost volatility

**Sensor Technologies**
- Vision: Cameras (RGB, thermal, depth), frame rate, resolution tradeoffs
- Lidar: Range measurement, point clouds, accuracy vs cost
- IMU: Accelerometer, gyroscope, magnetometer fusion
- Environmental: Temperature, humidity, pressure, gas
- Actuators: Motors (DC, stepper, servo), control requirements
- Sensor fusion: Combining multiple sensors for robust perception

## Data Sources & Query Methods

**Processor & Microcontroller Benchmarking**
- TechEmpower for SoC performance
- Microcontroller datasheets: power consumption, performance, cost
- RISC-V International ecosystem and adoption
- EdgeAI benchmarks: MLPerf inference results
- Query pattern: "microcontroller comparison", "RISC-V ecosystem"

**IoT Platform & Connectivity Analysis**
- Gartner IoT platforms Magic Quadrant
- GSMA Intelligence on cellular IoT (NB-IoT, LTE-M) adoption
- LoRa Alliance for LoRaWAN ecosystem
- WiFi/Bluetooth SIG specifications and adoption
- Query pattern: "IoT connectivity comparison", "edge vs cloud"

**Edge AI & Model Optimization**
- TensorFlow Lite documentation and benchmarks
- MLPerf Tiny Inference results (constrained devices)
- Quantization techniques and effectiveness papers
- Query pattern: "edge AI inference", "model quantization"

**Robotics Ecosystem**
- ROS community and project health
- Gazebo simulation capabilities
- Commercial robotics platforms: Boston Dynamics, Tesla Bot, etc.
- Research robotics: ROBOTS dataset, benchmark suites
- Query pattern: "ROS framework", "robot simulation"

**Hardware Manufacturing & Supply Chain**
- Distributor pricing: Digi-Key, Mouser real-time quotes
- Manufacturing partners: Foxconn, Flex, Sanmina capability
- PCB fab leadtimes and capacity
- Supply chain risk: Single-source components
- Query pattern: "chip sourcing", "manufacturing partner"

## Analysis Frameworks

**Processor Selection Matrix** (for embedded system)
- **Performance**: Instructions per second, clock speed, IPC (instructions per cycle)
- **Power budget**: uA in sleep, mA active, thermal dissipation
- **Memory**: RAM and flash availability, memory bus bandwidth
- **I/O**: SPI, I2C, UART, GPIO pins for sensors
- **Cost**: Per-unit price at target production volume
- **Ecosystem**: Development tools, SDK maturity, community support

**IoT Connectivity Decision Tree**
- **Range requirement**: < 100m (Bluetooth) vs 1km (WiFi) vs 10km (LoRa)?
- **Power budget**: Battery-powered or mains power?
- **Bandwidth**: Bytes/sec of data to transmit?
- **Latency**: Real-time response needed or can batch?
- **Infrastructure**: Do you control network (WiFi) or use public (Cellular)?
- **Cost**: Modem cost, subscription fees, gateway cost?

**Edge vs Cloud Computing Decision**
- **Latency**: Can data travel to cloud for processing? (1-3 sec round trip typical)
- **Privacy**: Is edge processing mandatory for sensitive data?
- **Connectivity**: Can device reliably reach cloud? (offline operation needed?)
- **Model complexity**: Can device run inference models? (size constraints)
- **Cost**: Edge compute cost vs cloud storage/compute cost?
- **Power**: Does cloud connectivity drain battery too fast?

**Robotics Platform Assessment**
- **Use case specificity**: Do you need general robotics or specialized platform?
- **ROS maturity**: Is ROS ecosystem sufficient or need custom framework?
- **Simulation**: Can you validate algorithms in simulation before hardware?
- **Integration effort**: How much code to get robot working?
- **Cost**: Hardware + development time to MVP
- **Support**: Community vs commercial support availability?

**Hardware Customization ROI**
- **Volume**: At what production volume does custom hardware pay off?
- **NRE cost**: One-time engineering cost to design custom chip/board
- **Unit cost reduction**: Savings per unit at target volume vs off-shelf
- **Time to market**: Design cycle time vs COTS availability
- **Risk**: Technical risk of custom design vs risk of COTS obsolescence
- **Payback period**: When does per-unit savings exceed NRE?

## Output Format Templates

### Embedded System Architecture
```
Application: [sensor, controller, compute requirement]
Production Volume: [1k units/year, 100k units/year]

Processor Options: [microcontroller/SoC candidates]
Performance Requirement: [MIPS, operations/sec]
Power Budget: [active mA, sleep uA, battery life]
Memory: [RAM and flash sizes needed]

Recommended Solution: [specific processor/board]
Connectivity: [WiFi, Bluetooth, Cellular, other]
Peripheral Support: [available sensors/interfaces]
Development Tools: [SDK, IDE, debugger]
Cost: [per-unit BOM, tooling]
```

### IoT Solution Design
```
Use Case: [monitoring, control, data collection]
Number of Devices: [scale]
Expected Lifetime: [years, battery vs mains]

Connectivity Architecture: [which protocol for which devices]
Cloud Platform: [AWS/Azure/GCP/custom]
Edge Processing: [what computing on device vs cloud]
Data Rate: [bytes/sec, frequency of transmission]

Cost Analysis: [device, connectivity, infrastructure]
Deployment Timeline: [development, manufacturing, rollout]
Scalability: [how to handle 10x growth]
```

### Edge AI Implementation
```
ML Model: [trained model, original size]
Target Device: [processor, memory constraints]

Optimization Strategy: [quantization, pruning, distillation]
Model Size: [original vs optimized, in MB]
Inference Latency: [target, achievable]
Accuracy Impact: [if quantization causes degradation]

Framework: [TensorFlow Lite, ONNX Runtime, etc.]
Hardware Acceleration: [CPU, GPU, NPU, Coral TPU]
Testing: [validation on target device]
Update Mechanism: [how to push new models]
```

### Robotics Development Plan
```
Robot Type: [autonomous vehicle, manipulator, humanoid]
Target Application: [research, commercial, consumer]

Hardware Platform: [commercially available vs custom]
Simulation Environment: [Gazebo, V-REP, custom]
Perception Pipeline: [sensors, fusion, algorithms]
Motion Planning: [path planning, obstacle avoidance]

ROS Version: [ROS 1 or ROS 2]
Development Timeline: [milestone schedule]
Testing Strategy: [simulation then hardware]
Team Expertise: [required skills, training]
```

## Key Metrics to Always Collect

For hardware/IoT decisions, track:
1. **Performance**: Throughput (ops/sec), latency, responsiveness
2. **Power**: Active power (mA), sleep power (uA), battery life (days/months)
3. **Cost**: BOM cost, development cost, NRE, per-unit cost at scale
4. **Reliability**: Uptime, MTBF, failure modes
5. **Scalability**: Number of devices supportable, network capacity
6. **Development speed**: Time to prototype, iteration cycle
7. **Ecosystem**: Available libraries, tutorials, community support

## Computational Workflows

**Pre-built Analysis Scripts**
- `power_budget_calculator.py` — Model power consumption across processor/connectivity/sensors using pandas
- `bom_cost_projector.py` — Estimate per-unit manufacturing cost at different production volumes with numpy
- `edge_ai_performance_analyzer.py` — Compute inference latency and accuracy degradation from quantization using benchmarks
- `iot_connectivity_simulator.py` — Model message frequency, bandwidth, battery life across WiFi/BLE/LoRa scenarios

**Dynamic Computation Examples**
- When selecting processor, compute power efficiency (operations per milliwatt) across candidates with statistical comparison
- When planning manufacturing, run cost curves (NRE amortization vs unit cost) across volume tiers
- When optimizing edge AI, simulate accuracy vs latency tradeoff from model quantization

**Output Artifacts**
- Power budget breakdown pie chart (processor/memory/connectivity/sensors percentages)
- Cost scaling curve (line: unit cost vs production volume with break-even analysis)
- Inference latency vs accuracy scatter plot (quantization levels, color: model size)
- Mermaid state diagram showing IoT device lifecycle (provisioning, operation, maintenance)
- LaTeX formula: Power_Budget (mA-hours) = (Active_mA * Duty_Cycle + Sleep_uA * (1-Duty_Cycle)) / 1000 * Battery_mAh

## References

Load from `references/` directory:
- `microcontroller-selection-guide.md` — processor comparison and tradeoffs
- `edge-ai-optimization-techniques.md` — quantization, pruning, inference
- `iot-connectivity-comparison.md` — WiFi vs Bluetooth vs LoRa vs Cellular
- `ros-getting-started.md` — ROS setup and basic tutorials
- `hardware-custom-vs-cots.md` — decision framework for custom electronics
- `sensor-fusion-algorithms.md` — integrating multiple sensors
- `embedded-power-optimization.md` — reducing power consumption

## Common Pitfalls to Avoid

- **Processor overkill**: Using expensive SoC when cheap microcontroller sufficient
- **Power underestimation**: Connectivity (WiFi, Cellular) drains battery faster than expected
- **Connectivity assumptions**: "Just use WiFi" without considering range/power constraints
- **Supply chain surprise**: Chosen component becomes unavailable mid-production
- **ROS complexity**: Using ROS when simple state machine sufficient adds overhead
- **Simulation gap**: Algorithm works in Gazebo but fails on real hardware (sensor noise, latency)
- **Edge AI limitations**: Quantized model accuracy loss unacceptable for deployment
- **Manufacturing shock**: Labor cost vs design cost shifts in different production volumes
