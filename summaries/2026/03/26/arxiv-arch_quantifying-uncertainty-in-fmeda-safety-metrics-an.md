---
title: "Quantifying Uncertainty in FMEDA Safety Metrics: An Error Propagation Approach for Enhanced ASIC Verification"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.21770"
published: "2026-03-26"
summarized: "2026-03-27T07:13:41.083464"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对汽车ASIC功能安全验证中的FMEDA（故障模式、影响和诊断分析）指标不确定性问题，提出了一种基于误差传播理论的新方法。该方法通过量化SPFM（单点故障指标）和LFM（潜伏故障指标）的最大偏差并提供置信区间，为分析质量提供直接度量。此外，研究还引入了误差重要性标识符（EII）来精确定位不确定性的主要来源，从而显著增强了FMEDA的透明度和可信度，解决了功能安全领域长期存在的未量化不确定性难题。

【方法概述 / Method】
本研究将误差传播理论引入FMEDA安全指标计算，建立数学模型以量化输入参数（故障模式分布FMD和诊断覆盖率DC）的误差如何传播至最终的SPFM和LFM指标。该方法通过解析推导或数值模拟计算输出指标的置信区间，并设计EII机制对各输入变量的误差贡献度进行排序，识别关键敏感参数。

【实验结果 / Results】
（注：论文摘要未提供具体实验数据，基于方法描述推断）所提方法能够为SPFM和LFM提供量化的置信区间，取代传统单点估计值；EII工具可有效识别导致不确定性的主导输入参数，使验证工程师能够优先改进关键数据来源的精度，从而提升整体分析可靠性。

【应用价值 / Applications】
该方法直接服务于ISO 26262汽车功能安全标准合规性验证，帮助半导体企业和Tier 1供应商在ASIC设计阶段建立更可信的安全分析流程。通过量化不确定性并指导资源优化配置，该技术可降低安全认证风险、减少专家判断依赖，并支持自动驾驶等高安全完整性等级（ASIL）系统的可靠验证。
