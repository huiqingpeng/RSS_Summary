---
title: "Texas Instruments MSPM0G5187 and AM13Ex MCUs integrate TinyEngine NPU for Edge AI applications"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/texas-instruments-mspm0g5187-and-am13ex-mcus-integrate-tinyengine-npu-for-edge-ai-applications/"
published: "2026-03-11"
summarized: "2026-03-12T07:02:19.994153"
ai_provider: "openai"
---

【是什么 / What it is】

德州仪器（TI）推出了两款新型MCU家族——MSPM0G5187和AM13Ex，均内置TinyEngine神经处理单元（NPU），可在芯片上直接实现低延迟、高效率的边缘AI/机器学习推理。MSPM0G5187基于Arm Cortex-M0+，面向通用低功耗应用；AM13Ex基于Arm Cortex-M33，专为实时电机控制设计。

Texas Instruments has launched two new MCU families—the MSPM0G5187 and AM13Ex—both featuring an integrated TinyEngine Neural Processing Unit (NPU) to enable low-latency, high-efficiency Edge AI/Machine Learning inference directly on-chip. The MSPM0G5187 is based on Arm Cortex-M0+ for general-purpose low-power applications, while the AM13Ex uses Arm Cortex-M33 and targets real-time motor control.

---

【为什么重要 / Why it matters】

TinyEngine NPU可将AI模型推理延迟降低90倍、能耗降低120倍以上，使微型MCU具备此前高端处理器才有的AI能力，推动边缘智能向更低成本、更低功耗的设备普及。这标志着边缘AI正从"可选功能"变为"标准配置"，尤其在电池供电设备和工业预测性维护领域具有颠覆性意义。

The TinyEngine NPU delivers up to 90x lower latency and over 120x lower energy per inference, bringing AI capabilities previously reserved for high-end processors to tiny, cost-sensitive MCUs—accelerating the democratization of edge intelligence. This signals a shift where Edge AI is becoming a standard feature rather than a premium add-on, with transformative implications for battery-powered devices and industrial predictive maintenance.

---

【我能用什么 / How I can use it】

开发者可利用CCStudio Edge AI Studio中60+预置模型快速原型开发，结合FreeRTOS/Zephyr构建语音唤醒、异常检测、电机故障预测等应用；对于成本敏感项目，MSPM0G5187的$1以下单价适合大规模部署，而AM13Ex的电机控制专用外设适合机器人/家电智能化升级。建议优先评估LP-MSPM0G5187 LaunchPad开发套件（$22）进行概念验证。

Developers can rapidly prototype using 60+ pre-trained models in CCStudio Edge AI Studio, building voice wake-word, anomaly detection, or motor fault prediction applications with FreeRTOS/Zephyr; for cost-sensitive projects, the sub-$1 MSPM0G5187 suits mass deployment, while AM13Ex's motor-control peripherals fit robotics/appliance intelligence upgrades. Start with the LP-MSPM0G5187 LaunchPad ($22) for proof-of-concept evaluation.
