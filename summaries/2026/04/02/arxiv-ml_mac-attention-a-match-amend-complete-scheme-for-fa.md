---
title: "MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00235"
published: "2026-04-02"
summarized: "2026-04-03T07:19:08.074294"
ai_provider: "openai"
---

【论文摘要 / Abstract】
MAC-Attention提出了一种保真度和访问权限的注意力加速方案，通过重用语义相似历史查询的注意力计算来解决长上下文解码中的IO瓶颈问题。该方法采用"匹配-修正-补全"三阶段架构，在匹配命中时实现与上下文长度无关的常数级计算和带宽复杂度。实验表明，该方法在128K上下文下可减少99%的KV访问、降低60%以上的token生成延迟，同时保持全注意力质量，实现最高14.3倍的注意力阶段加速和2.6倍的端到端加速。

【方法概述 / Method】
MAC-Attention采用三阶段流水线：匹配阶段在短局部窗口内进行预RoPE的L2距离相似性匹配；修正阶段对匹配边界附近的小范围区域重新计算以校正重用的注意力；补全阶段通过数值稳定的融合操作将修正结果与KV尾部的新计算注意力合并。该方法与模型架构无关，可与IO感知内核、分页KV管理器及MQA/GQA等现有优化技术组合使用。

【实验结果 / Results】
在LongBench v2（120K）、RULER（120K）和LongGenBench（16K连续生成）等基准测试上，相比最新的FlashInfer库，MAC-Attention实现KV访问量减少高达99%，128K上下文下token生成延迟降低超过60%，注意力计算阶段加速达14.3倍以上，端到端加速最高2.6倍，且保持与全注意力计算相当的质量水平。

【应用价值 / Applications】
MAC-Attention适用于需要高效长上下文推理的大规模语言模型部署场景，如长文档理解、多轮对话系统和长文本生成等应用。该方法在显著提升推理速度的同时避免了压缩或选择策略带来的信息损失，为延迟敏感且质量要求高的生产环境提供了实用的加速方案，特别适合128K及以上超长上下文的实时推理服务。
