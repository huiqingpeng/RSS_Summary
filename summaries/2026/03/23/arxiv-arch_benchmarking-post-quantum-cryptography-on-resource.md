---
title: "Benchmarking Post-Quantum Cryptography on Resource-Constrained IoT Devices: ML-KEM and ML-DSA on ARM Cortex-M0+"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19340"
published: "2026-03-23"
summarized: "2026-03-24T07:14:20.617667"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本论文首次在ARM Cortex-M0+处理器上对NIST后量子密码标准ML-KEM（FIPS 203）和ML-DSA（FIPS 204）进行了系统性的算法级基准测试。研究发现ML-KEM-512在RP2040平台上完成完整密钥交换仅需36.3毫秒、消耗2.87毫焦能量，比同硬件上的ECDH P-256快17倍且节能94%。ML-DSA签名因拒绝采样机制表现出高延迟方差（变异系数61-71%），而Cortex-M0+相比Cortex-M4仅产生1.8-1.9倍性能下降，显示出后量子密码在极简32位处理器上的可行性。

【方法概述 / Method】
研究采用PQClean参考C语言实现，在133 MHz主频、264 KB SRAM的RP2040（Raspberry Pi Pico）平台上测试了ML-KEM和ML-DSA的全部三个安全等级。测量指标涵盖密钥生成、封装/签名、解封装/验证等核心操作，并通过与ECDH P-256及已发表Cortex-M4结果的对比分析架构差异对性能的影响。

【实验结果 / Results】
ML-KEM在低安全等级表现出优异的能效比，ML-KEM-512的密钥交换延迟和能耗显著优于传统椭圆曲线密码；ML-DSA签名延迟呈现高度不确定性，ML-DSA-87的99th百分位延迟可达1,115毫秒。尽管Cortex-M0+缺乏64位乘法、DSP和SIMD指令，其性能损失相对Cortex-M4控制在2倍以内，证明了参考实现的高效性。

【应用价值 / Applications】
该研究为设计寿命10-20年的物联网设备提供了关键的后量子迁移决策依据，帮助开发者在极端资源受限环境下权衡安全等级与性能开销。开源基准测试套件为社区提供了可复现的评估工具，支撑智能传感器、工业控制等长周期部署场景的密码学升级规划。
