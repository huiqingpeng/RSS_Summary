---
title: "LooperRobotics Insight 9 standalone spatial AI camera features D-Robotics RDK X5 SoC, supports ROS 2 (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/25/looperrobotics-insight-9-standalone-spatial-ai-camera-features-d-robotics-rdk-x5-soc-supports-ros-2/"
published: "2026-03-25"
fetched: "2026-03-26T07:01:48.612689"
---

LooperRobotics Insight 9 is an autonomous plug-and-play spatial AI camera designed for embodied intelligence, quadruped robots, and dynamic mobile platforms. Compared to typical USB depth cameras like Intel RealSense D435i or Luxonis OAK-D, which rely on a host PC for processing, the Insight 9 integrates a D-Robotics RDK X5 octa-core Cortex-A55 processor with a 10 TOPS AI accelerator, allowing it to run Visual SLAM (V-SLAM) and depth mapping entirely on-device.
The camera features a “Tri-Eye Perception Matrix,” which includes an 8.4MP Sony Starvis IMX415 RGB sensor with an ultra-wide 188° field of view, and two SmartSens SG0132 global shutter sensors for stereoscopic depth. Encased in a passively cooled CNC aluminum chassis, it is also equipped with an automotive-grade Bosch BMI088 IMU capable of 24g high-G tracking, making it suitable for the heavy vibrations of legged locomotion.
LooperRobotics Insight 9 specifications:
- SoC – D-Robotics RDK X5 octa-core Arm Cortex-A55 processor @ 1.5 GHz; 32 GFLOPS GPU; 10 TOPS BPU 3.0 AI
- System Memory – 4GB LPDDR4
- Storage – 16GB eMMC 5.1 flash
- Camera
- RGB camera (semantic insight)
- Sensor – 8.4MP Sony Starvis IMX415 (3840 × 2160 resolution)
- Field of View – 188° Diagonal / 157° Horizontal
- Low Light Sensitivity – 0.01 Lux
- Stereo depth cameras (spatial awareness)
- Sensors – 2x SmartSens SG0132 global shutter sensors
- Resolution – 1280 × 960 @ 60 fps
- Field of View – 157.2° Diagonal / 115.6° Horizontal
- Baseline – 100 mm
- Focal Length (f) – 304 pixels
- Max Disparity – 163 pixels
- Depth Range – 0.1m to 30m (Optimal engineering range: 0.2m to 8.0m)
- RGB camera (semantic insight)
- USB – 1x USB 3.0 Type-C port for data and power (Ethernet-over-USB not confirmed)
- Mics – Bosch BMI088 6-axis industrial IMU (up to 24g tracking, < 10 μs sync accuracy, ±2000 °/s gyro range)
- Power – 5V/2A DC via USB-C (Ultra-low 5W typical power consumption)
- Dimensions – 129 × 33.8 × 35 mm (aviation-grade CNC aluminum enclosure)
- Weight – 176 grams
- Operating Temperature – -20°C to 85°C
On the software side, the camera runs Linux with a pre-installed ROS 2 Humble environment, so no complex driver setup is needed on the host. Once connected to a network, which in this context refers to a local IP connection between the camera and a robot controller or PC via USB virtual Ethernet, developers can directly access ROS topics for data. This communication is handled by Eclipse Cyclone DDS decentralized real-time middleware. The onboard 10 TOPS NPU performs tasks like AI-based depth mapping, V-SLAM localization, and real-time object detection on the device itself. It also outputs a unified data stream that pixel-for-pixel synchronizes the raw view, rectified view, and neural depth map. You can check out the developer guide to find more details about the SDK, which works on Ubuntu 22.04 (Recommended), Windows 11, and macOS Tahoe.
In terms of depth, accuracy, and performance, the Insight 9 uses stereo vision with a 100mm baseline for better accuracy at longer distances. It maintains an error under 2% at close range and under 8% up to 10 meters. The effective operating range is about 0.2m to 8m for stable and reliable depth measurements, while accuracy decreases at longer distances due to stereo limitations. The company also provides some graphs and visual benchmarks to back up the claims.
This plots the camera’s standalone error rate. As the distance increases (up to 10m), the error naturally goes up, but notice the jagged, up-and-down spikes! This is the “oscillation” or “staircase effect” caused by discrete pixel sampling, a common characteristic of stereo vision. Even with those spikes, it stays below an 8% error rate at the absolute maximum range.
This compares the camera’s depth readings (light blue) against a perfectly accurate laser measurement (dark blue straight line). It shows that the camera’s spatial tracking closely matches real-world results, maintaining a near-perfect 1:1 ratio up to about the 7-meter mark, where it begins to deviate slightly.
The above graph compares the absolute distance accuracy of the three cameras against the ground truth (blue line). The RealSense D435 quickly becomes inaccurate after around 4 meters and underestimates distance, while the RealSense D455 starts to overestimate beyond about 6 meters. In comparison, the Insight 9 stays much closer to the ground truth over a longer range, showing better overall accuracy. More information about depth accuracy and performance details can be found on the hardware doc page.
Previously, we have written about several depth cameras, including the Orbbec Femto Mega 3D depth and 4K RGB camera, the Orbbec Gemini 335Lg depth camera with a GMSL2/FAKRA connector, and the Orbbec Femto Bolt, a 3D depth and RGB USB-C camera developed in collaboration with Microsoft that integrates the same ToF (Time-of-Flight) technology used in the Microsoft Azure Kinect camera module and HoloLens 2 mixed reality headset.
The LooperRobotics Insight 9 is available through Kickstarter, with early bird pricing starting at around $300, offering up to 30% off the $429 MSRP, while later tiers go up to about $365, depending on availability. The product is expected to begin shipping around June 2026, and shipping fees are calculated at checkout, including customs duties and taxes. More information about the camera is available on the products page.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
