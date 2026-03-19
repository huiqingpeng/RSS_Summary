---
title: "Stable Forgetting: Bounded Parameter-Efficient Unlearning in Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.24166"
published: "2026-03-19"
summarized: "2026-03-19T14:07:24.276797"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对基础模型（如语言和视觉Transformer）中的机器遗忘问题，揭示了现有梯度差分方法在结合交叉熵损失时会导致权重和梯度无界增长的缺陷。作者从理论上分析了梯度上升如何破坏Transformer前馈MLP层的优化稳定性，并提出了有界参数高效遗忘方法（Bounded Parameter-Efficient Unlearning），通过在MLP适配器上应用有界函数来稳定LoRA微调过程。实验表明，该方法在CIFAR-100视觉任务和多个语言模型基准（TOFU、TDEC、MUSE）上均实现了高质量的遗忘效果，同时保持了模型效用。

【方法概述 / Method】
论文采用理论分析与算法设计相结合的方法：首先建立数学框架证明梯度上升在MLP层中的不稳定性机制，然后设计基于LoRA的参数高效微调方案，将标准梯度上升替换为有界函数（如Sine函数）作用于MLP适配器的权重更新，从而约束优化动态并确保可靠收敛。

【实验结果 / Results】
在CIFAR-100的ViT类别删除任务中，GD+Sine方法在ViT-B/16、ViT-L/14和DeiT-S三种架构上均唯一实现了高遗忘质量与模型效用的平衡；在语言模型基准上，该方法在22M至8B参数规模的模型中均展现出改进的遗忘性能，同时有效保留了模型效用。

【应用价值 / Applications】
该研究为大型基础模型的隐私合规和安全部署提供了可靠的遗忘解决方案，适用于需要删除特定训练数据（如版权内容、敏感个人信息）或消除有害能力的场景，其参数高效特性使其能够低成本应用于数十亿参数规模的实际生产模型。
