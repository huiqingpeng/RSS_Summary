---
title: "RuView project leverages ESP32 nodes for WiFi-based presence detection, pose estimation, and breathing/heart rate monitoring"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/26/ruview-project-leverages-esp32-nodes-for-presence-detection-pose-estimation-and-breathing-heart-rate-monitoring/"
published: "2026-03-26"
summarized: "2026-03-27T07:10:56.530325"
ai_provider: "openai"
---

【是什么 / What it is】

RuView 是一个开源的"WiFi DensePose"实现项目，使用 Rust 或 Python 编写，利用多个 ESP32 节点和 WiFi 路由器，通过分析信道状态信息（CSI）扰动来实现实时人体姿态估计、生命体征监测和存在检测，无需依赖摄像头。该项目基于学术研究中的 WiFi 信号感知技术，可在穿墙条件下工作，但也曾因代码中存在随机数据而陷入造假争议。

RuView is an open-source "WiFi DensePose" implementation written in Rust or Python that leverages multiple ESP32 nodes and a WiFi router to enable real-time human pose estimation, vital sign monitoring, and presence detection by analyzing Channel State Information (CSI) disturbances—without relying on cameras. Based on academic research in WiFi signal sensing, it works through walls but faced controversy over fake data found in early code versions.

---

【为什么重要 / Why it matters】

这项技术代表了隐私友好型感知的重要方向——用无处不在的 WiFi 信号替代摄像头进行人体追踪，消除了视觉监控的隐私顾虑，同时实现了穿墙检测等摄像头无法完成的功能。其低成本硬件方案（约 54 美元）和开源特性使前沿学术研究民主化，尽管部分功能声明（如灾害救援中的伤情分类）可能过于乐观，但核心技术已被 Espressif 等厂商验证，在智能家居、养老监护、安防等领域具有应用潜力。

This technology represents a significant privacy-friendly sensing paradigm—replacing cameras with ubiquitous WiFi signals for human tracking, eliminating privacy concerns of visual surveillance while enabling through-wall detection impossible for cameras. Its low-cost hardware (~$54) and open-source nature democratize cutting-edge academic research; while some claims (e.g., injury severity classification in disaster response) may be overstated, the core technology has been validated by vendors like Espressif, showing potential in smart homes, elder care, and security applications.

---

【我能用什么 / How I can use it】

若具备 ESP32-S3 开发板和 WiFi 路由器，可按照 GitHub 指南搭建 3-6 节点的多静态网格系统，通过 Docker 部署并在本地训练环境特定的姿态估计模型；若暂无硬件，可先使用模拟数据模式或在线演示熟悉界面。建议关注项目 Issue 区和社区反馈以评估实际性能，同时可探索将基础功能（存在检测、呼吸率监测）直接应用于无需神经网络的场景，如无人时的房间状态监控或睡眠呼吸追踪。

With ESP32-S3 boards and a WiFi router, one can build a 3-6 node multistatic mesh following the GitHub guide, deploy via Docker, and train environment-specific pose models locally; without hardware, start with simulated data mode or the live demo to explore the interface. Monitor project issues and community feedback to assess real-world performance, and consider deploying baseline features (presence detection, breathing rate) that work without neural networks—such as room occupancy monitoring or sleep breathing tracking.
