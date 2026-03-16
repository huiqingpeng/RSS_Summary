---
title: "Design, Simulate, and Scale AI Factory Infrastructure with NVIDIA DSX Air"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/design-simulate-and-scale-ai-factory-infrastructure-with-nvidia-dsx-air/"
published: "2026-03-16"
summarized: "2026-03-17T07:08:51.057358"
ai_provider: "openai"
---

【是什么 / What it is】
NVIDIA DSX Air 是一款云端 AI 工厂基础设施模拟平台，允许企业在实际部署硬件之前，对计算、网络、存储和安全系统进行完整的设计、测试与优化。它通过提供保证容量、统一账户管理、模拟检查点和历史记录等功能，帮助用户实现全栈集群的数字化验证。

NVIDIA DSX Air is a cloud-based AI factory infrastructure simulation platform that enables organizations to design, test, and optimize compute, networking, storage, and security systems before physical hardware deployment. It offers features like guaranteed capacity, unified account management, simulation checkpoints, and history tracking to support full-stack cluster validation.

---

【为什么重要 / Why it matters】
AI 工厂建设涉及复杂的多层系统集成，配置错误或集成问题可能导致重大延误和性能损失；DSX Air 通过"数字孪生"方式将部署周期压缩，并降低集成风险。此外，它支持 CI/CD 集成和持续验证，使基础设施运维能够跟上 AI 工作负载的快速迭代节奏，同时减少对专用硬件实验室的依赖。

AI factory construction involves complex multi-layer system integration where misconfigurations or integration issues can cause major delays and performance losses; DSX Air compresses deployment cycles and reduces integration risks through "digital twin" simulation. Furthermore, its CI/CD integration and continuous validation capabilities allow infrastructure operations to keep pace with rapid AI workload iterations while reducing dependency on dedicated hardware labs.

---

【我能用什么 / How I can use it】
技术团队可利用 DSX Air 的 Python SDK 和 REST API 将模拟环境嵌入 CI/CD 流水线，实现配置变更的自动化预验证；企业可通过共享模拟副本建立安全的培训沙箱，降低技能提升成本。对于计划部署 NVIDIA Vera Rubin 等下一代平台的组织，可提前模拟 Spectrum-6 交换机和 NVLink 架构，确保 day-one 的互操作性和平滑迁移。

Technical teams can leverage DSX Air's Python SDK and REST APIs to embed simulation environments into CI/CD pipelines for automated pre-validation of configuration changes; enterprises can establish secure training sandboxes through shared simulation replicas to reduce upskilling costs. For organizations planning to deploy next-generation platforms like NVIDIA Vera Rubin, they can pre-simulate Spectrum-6 switches and NVLink architectures to ensure day-one interoperability and smooth migration.
