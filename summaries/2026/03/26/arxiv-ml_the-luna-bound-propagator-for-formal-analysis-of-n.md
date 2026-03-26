---
title: "The Luna Bound Propagator for Formal Analysis of Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23878"
published: "2026-03-26"
summarized: "2026-03-27T07:18:30.498559"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Luna，一种用 C++ 实现的新型神经网络边界传播器，用于形式化验证。Luna 支持区间边界传播（IBP）、CROWN 分析和参数化 CROWN（alpha-CROWN）分析，能够处理通用计算图。实验表明，Luna 在边界紧致性和计算效率方面与最先进的 alpha-CROWN Python 实现具有竞争力，同时解决了 Python 实现难以集成到现有 DNN 验证器和生产级系统的问题。

【方法概述 / Method】
Luna 采用 C++ 从零实现，提供与 Python 实现同等功能的边界传播算法，包括 IBP、CROWN 和 alpha-CROWN。其设计基于通用计算图结构，支持灵活的神经网络架构，便于集成到现有的 C++ 验证框架和长期维护的生产系统中。

【实验结果 / Results】
在 VNN-COMP 2025 基准测试集上的评估显示，Luna 在边界紧致性和计算效率方面与当前最先进的 alpha-CROWN Python 实现表现相当，证明了 C++ 实现并未牺牲性能，同时获得了更好的系统集成能力。

【应用价值 / Applications】
Luna 可直接嵌入现有的 C++ DNN 验证器和工业级安全关键系统，克服了 Python 实现的语言壁垒和依赖复杂性。该工具适用于自动驾驶、航空航天、医疗设备等需要严格神经网络形式化验证的高可靠性场景，有助于推动神经网络验证技术的实际部署和长期维护。
