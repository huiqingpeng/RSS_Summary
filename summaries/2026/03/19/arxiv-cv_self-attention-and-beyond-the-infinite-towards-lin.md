---
title: "Self-Attention And Beyond the Infinite: Towards Linear Transformers with Infinite Self-Attention"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.00175"
published: "2026-03-19"
summarized: "2026-03-19T16:31:58.092598"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出无限自注意力机制（Infinite Self-Attention, InfSA），通过谱方法将自注意力层重新表述为内容自适应token图上的扩散步骤，利用折扣Neumann级数累积多跳交互，并建立与经典图中心性（Katz、PageRank、特征向量中心性）的理论联系。在此基础上，作者提出线性时间变体Linear-InfSA，以固定大小的辅助状态（与序列长度无关）近似隐式注意力算子的主特征向量，在不构建完整注意力矩阵的情况下实现线性复杂度，并在ImageNet上取得显著性能提升。

【方法概述 / Method】
InfSA将自注意力视为吸收马尔可夫链的基本矩阵，token的中心性对应随机游走被吸收前的期望访问次数；Linear-InfSA通过幂迭代近似主特征向量，仅维护与每头维度dh成正比的固定大小状态，避免显式计算N×N注意力矩阵。该方法可直接替换Vision Transformer中的softmax注意力，无需修改网络架构。

【实验结果 / Results】
在4层ViT（53.5M参数）上，Linear-InfSA达到84.7% ImageNet-1K top-1准确率，较同等配置softmax ViT提升3.2个百分点；ImageNet-V2上达79.8%，显著优于基线76.8%。在A100 GPU上，Linear-InfViT吞吐量达231 images/s、能耗0.87 J/image，较同等ViT提升13倍，且是唯一能在9216×9216（约332K tokens）分辨率完成推理而不OOM的模型；线性近似与二次算子主导特征向量的余弦相似度达0.985。

【应用价值 / Applications】
该方法为高分辨率视觉任务（如医学影像分析、卫星图像处理、4K/8K视频理解）提供了可扩展的Transformer方案，突破了传统自注意力的二次复杂度瓶颈。其线性复杂度和低内存占用使超大分辨率推理成为可能，同时保持与经典图中心性理论的可解释性联系，适用于资源受限边缘设备部署及需要全局上下文建模的视觉应用。
