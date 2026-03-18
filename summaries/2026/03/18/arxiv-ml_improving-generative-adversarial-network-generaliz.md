---
title: "Improving Generative Adversarial Network Generalization for Facial Expression Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15648"
published: "2026-03-18"
summarized: "2026-03-18T16:05:28.829156"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Regression GAN (RegGAN)，一种用于面部表情合成的新型生成对抗网络，旨在解决现有条件GAN在测试图像与训练数据分布不一致时性能下降的问题。RegGAN通过学习中间表示来提升模型在训练分布之外的泛化能力，在CFEE数据集上训练后，在分布外数据（包括名人照片、肖像、雕像和虚拟形象）上均表现出色。实验结果表明，RegGAN在表情质量、真实感和综合性能指标上均优于六种最先进的方法，人工评估显示其在表情质量、身份保持和真实感方面分别比最佳竞争模型提升25%、26%和30%。

【方法概述 / Method】
RegGAN由两个核心组件构成：一是具有局部感受野的回归层，通过岭回归损失最小化重建误差来学习表情细节；二是通过对抗训练优化的精化网络，用于增强生成图像的真实感。这种分解式架构使模型能够显式学习表情表示，从而更好地泛化到未见过的数据分布。

【实验结果 / Results】
研究采用四种评估指标：表情分类分数（ECS）、人脸相似度分数（FSS）、QualiCLIP感知真实度以及Fréchet Inception Distance（FID）。RegGAN在ECS、FID和QualiCLIP三项指标上均排名第一，在FSS上排名第二。人工评估进一步验证了RegGAN在表情质量、身份保持和真实感方面的显著优势。

【应用价值 / Applications】
该研究可广泛应用于需要鲁棒面部表情合成的场景，如影视制作中的数字人表情驱动、游戏角色动画生成、虚拟现实中的化身表情控制，以及跨域人脸图像编辑（如艺术肖像、雕像风格迁移）。其强大的分布外泛化能力使其特别适用于训练数据受限或目标域多样的实际应用环境。
