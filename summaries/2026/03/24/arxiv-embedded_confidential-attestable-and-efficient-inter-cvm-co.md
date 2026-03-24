---
title: "Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2512.01594"
published: "2026-03-24"
summarized: "2026-03-25T07:06:44.388743"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CAEC系统，首次实现了Arm CCA架构下机密虚拟机（CVM）之间的受保护内存共享机制。针对现有CVM架构因分离内存模型导致CVM间必须通过hypervisor可访问内存进行加密通信的性能瓶颈问题，CAEC通过扩展CCA固件引入机密共享内存（CSM），使多个CVM能够安全共享内存区域，同时保持对hypervisor和非参与CVM的不可访问性。实验表明，CAEC在仅增加4%固件代码量的前提下，将CVM间通信的CPU周期数降低至基于加密机制的1/209，为可信多CVM服务提供了高性能、可验证且可扩展的基础。

【方法概述 / Method】
CAEC基于Arm Confidential Compute Architecture（CCA）构建，通过扩展其固件实现机密共享内存（CSM）抽象，允许多个CVM直接映射同一物理内存区域而无需hypervisor介入。该设计利用CCA的Realm Management Extension（RME）硬件原语，通过固件层面的访问控制策略确保CSM仅对显式授权的CVM集合可见，同时保持与现有CCA硬件的完全兼容性。

【实验结果 / Results】
CAEC在多种工作负载下展现出显著性能优势：CVM间通信的CPU周期数相比基于hypervisor共享内存的加密机制减少高达209倍；在Redis和Nginx等真实应用场景中，端到端吞吐量提升2.3-8.7倍；系统整体仅引入4%的CCA固件代码膨胀和可忽略的内存开销，证明了其在资源受限的边缘和云环境中的实用性。

【应用价值 / Applications】
CAEC适用于需要高安全隔离与高效协作并存的场景，包括：微服务架构中敏感组件的细粒度隔离与快速通信、边缘计算中受信任执行环境的联邦学习、以及多云/混合云环境中跨租户的安全数据协作。其可验证的共享语义（attestable sharing）为构建下一代可信多CVM服务提供了标准化基础，填补了机密计算领域CVM间安全通信的关键空白。
