---
title: "FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.02691"
published: "2026-03-20"
summarized: "2026-03-20T16:14:13.090985"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了FSFSplatter，一种从自由稀疏图像中快速重建表面和新视角的方法。针对现有高斯溅射方法需要密集校准视角、稀疏输入易导致表面质量差和过拟合的问题，该方法通过端到端的密集高斯初始化、相机参数估计和几何增强场景优化，实现了2分钟内的快速重建。实验表明，FSFSplatter在DTU、Replica和BlendedMVS数据集上优于当前最先进的方法。

【方法概述 / Method】
FSFSplatter采用大型Transformer编码多视角图像，通过自分裂高斯头生成密集且几何一致的高斯场景初始化；同时引入基于贡献度的剪枝消除局部浮点，并利用深度和多视角特征监督结合可微相机参数进行快速优化，以缓解对有限视角的过拟合。

【实验结果 / Results】
该方法在广泛使用的DTU、Replica和BlendedMVS数据集上取得了优于现有最先进方法的性能，能够在2分钟内完成从稀疏自由视角图像到表面重建和新视角合成的完整流程。

【应用价值 / Applications】
FSFSplatter适用于需要快速三维重建的场景，如文化遗产数字化、增强现实内容生成、机器人导航和自动驾驶中的稀疏视觉重建等，显著降低了对密集采集设备的依赖，提升了实际部署的便捷性和效率。
