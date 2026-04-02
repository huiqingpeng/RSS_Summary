---
title: "LightGuard: Transparent WiFi Security via Physical-Layer LiFi Key Bootstrapping"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.01092"
published: "2026-04-02"
summarized: "2026-04-03T07:15:25.195824"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出LightGuard，一种利用可见光通信（LiFi）物理层特性增强WiFi安全性的双链路架构。核心洞察在于：WiFi的射频信号易穿透墙壁导致窃听风险，而LiFi受限于视距传播且被不透明表面阻挡，因此可将密钥建立过程从WiFi卸载到物理隔离的LiFi信道，确保加密材料永不经过开放的RF介质。原型系统使用商用WiFi网卡和自研LiFi收发前端验证了该设计。

【方法概述 / Method】
LightGuard采用双链路架构，通过LiFi信道完成会话密钥的生成与协商，随后将密钥安装至WiFi接口用于后续加密通信。该方法利用LiFi的天然物理隔离特性（视线传播、不透光表面阻挡）创建安全的密钥引导通道，实现与现有WiFi基础设施的透明兼容。

【实验结果 / Results】
论文通过原型系统验证了LightGuard的可行性，使用现成WiFi网卡和定制LiFi收发前端完成端到端实现。实验表明该方案能够在保持WiFi通信便利性的同时，消除密钥在RF介质中暴露的风险，实现了物理层安全增强与商用硬件的兼容。

【应用价值 / Applications】
LightGuard适用于对安全性要求高的WiFi部署场景，如企业办公网络、金融机构、政府机构和智能家居等，可有效防御隔墙窃听、中间人攻击等RF侧信道威胁。该方案无需改造现有WiFi协议栈，仅需添加低成本LiFi模块即可实现透明安全升级，具有良好的部署前景。
