---
title: "RiboSphere: Learning Unified and Efficient Representations of RNA Structures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19636"
published: "2026-03-23"
summarized: "2026-03-24T07:20:42.192773"
ai_provider: "openai"
---

【论文摘要 / Abstract】

RiboSphere 是一个用于学习 RNA 结构离散几何表示的新型框架，通过结合向量量化和流匹配技术来解决 RNA 结构建模中骨架柔性高、非经典相互作用普遍以及实验测定 3D 结构稀缺的难题。该模型利用几何 Transformer 编码器生成 SE(3) 不变特征，并通过有限标量量化（FSQ）将其离散化为有限词汇的隐式编码，再由流匹配解码器重建原子坐标。实验表明，学习到的编码索引富集于特定 RNA 结构基序，且在结构重建（RMSD 1.25 Å，TM-score 0.84）、逆向折叠和 RNA-配体结合预测等任务上表现优异，尤其在数据稀缺场景下具有良好的泛化能力。

【方法概述 / Method】

RiboSphere 采用几何 Transformer 编码器提取 SE(3) 等变/不变的几何特征，并通过有限标量量化（FSQ）将这些连续特征离散化为紧凑的隐式编码词汇表。基于这些离散编码，流匹配（flow matching）解码器通过条件生成模型重建 RNA 原子坐标，实现高保真度的结构生成。

【实验结果 / Results】

RiboSphere 在结构重建任务上达到 RMSD 1.25 Å 和 TM-score 0.84 的优异性能，表明其原子级重建精度接近实验水平。预训练的离散表示在迁移学习中表现突出，在数据稀少的逆向折叠和 RNA-配体结合预测任务上展现出稳健的泛化能力，且学习到的编码与已知 RNA 结构基序存在显著对应关系。

【应用价值 / Applications】

该研究为 RNA 结构预测和功能注释提供了高效统一的表示学习框架，可加速 RNA 靶向药物设计中的配体结合预测和 RNA 工程中的序列-结构设计。其离散表示的紧凑性和可解释性有助于在实验数据有限的情况下实现知识迁移，对 RNA 生物学研究和合成生物学应用具有重要价值。
