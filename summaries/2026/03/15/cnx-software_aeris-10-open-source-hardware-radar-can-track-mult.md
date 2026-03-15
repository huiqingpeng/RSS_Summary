---
title: "AERIS-10 open-source hardware radar can track multiple objects up to 20km away"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/"
published: "2026-03-15"
summarized: "2026-03-16T07:01:02.858865"
ai_provider: "openai"
---

【是什么 / What it is】

AERIS-10 是一款开源硬件相控阵雷达系统，工作频率为 10.5 GHz，采用脉冲线性调频（LFM）调制技术，基于 AMD Artix-7 FPGA 实现信号处理。该系统提供两个版本：AERIS-10N（探测距离 3km，8×16 贴片天线阵列）和 AERIS-10X（探测距离 20km，32×16 介质填充缝隙波导阵列），所有设计文件和代码均在 GitHub 上以开放许可发布。

AERIS-10 is an open-source hardware phased array radar system operating at 10.5 GHz with Pulse Linear Frequency Modulated (LFM) modulation, built on an AMD Artix-7 FPGA for signal processing. The system comes in two versions: AERIS-10N (3km range with 8×16 patch antenna array) and AERIS-10X (20km range with 32×16 dielectric-filled slotted waveguide array), with all design files and code released on GitHub under open licenses.

【为什么重要 / Why it matters】

该项目将原本售价 25 万美元以上的商用相控阵雷达成本降至 5,000–15,000 美元，使研究人员、无人机开发者和 SDR 爱好者能够以可负担的价格接触先进的雷达技术。作为完全开源的项目，它打破了军事和高端商业领域对相控阵雷达技术的垄断，有望加速民用雷达应用的创新，如无人机探测、自动驾驶和气象监测等领域的发展。

This project reduces the cost of phased array radar from over $250,000 for commercial systems to $5,000–$15,000, making advanced radar technology accessible to researchers, drone developers, and SDR enthusiasts. As a fully open-source initiative, it breaks the monopoly of military and high-end commercial sectors on phased array radar technology, potentially accelerating innovation in civilian applications such as drone detection, autonomous driving, and weather monitoring.

【我能用什么 / How I can use it】

如果你是电子工程师或研究者，可以下载 GitHub 上的 EAGLE 原理图、PCB 布局和 FPGA 代码，自行组装并定制雷达系统用于特定研究项目；无人机开发者可集成该雷达实现避障或目标跟踪功能；SDR 社区成员则能借此深入理解相控阵波束成形、脉冲压缩等核心算法。使用前务必确认当地无线电管理法规（如 FCC 许可），确保合法合规操作。

If you are an electronics engineer or researcher, you can download the EAGLE schematics, PCB layouts, and FPGA code from GitHub to build and customize the radar for specific research projects; drone developers can integrate this radar for obstacle avoidance or target tracking; SDR community members can use it to gain deep understanding of core algorithms like phased array beamforming and pulse compression. Always verify local radio regulations (such as FCC licensing) before operation to ensure legal compliance.
