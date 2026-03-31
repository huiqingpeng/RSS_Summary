---
title: "Liquid Networks with Mixture Density Heads for Efficient Imitation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27058"
published: "2026-03-31"
summarized: "2026-04-01T07:21:15.009315"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出将液态神经网络（Liquid Neural Networks）与混合密度头（Mixture Density Heads）相结合用于模仿学习，并与扩散策略（Diffusion Policies）在Push-T、RoboMimic Can和PointMaze任务上进行对比。研究发现，在控制输入、训练预算和评估设置一致的公平比较下，液态策略仅用约一半参数（4.3M vs. 8.6M），即可实现2.4倍的离线预测误差降低和1.8倍的推理速度提升。尤其在低数据和中等数据场景下，液态模型展现出更强的样本效率和鲁棒性，为迭代去噪方法提供了一种紧凑且实用的替代方案。

【方法概述 / Method】
论文采用共享主干网络（shared-backbone）的对比协议，单独隔离策略头（policy head）的影响，确保液态神经网络与扩散策略在相同输入、训练预算和评估条件下进行公平比较。液态神经网络通过连续时间动态系统建模时序依赖，结合混合密度头输出多模态动作分布，避免了扩散模型所需的迭代去噪过程。

【实验结果 / Results】
实验表明，液态策略在1%至46.42%的训练数据范围内始终保持更强的鲁棒性，在低数据和中等数据区间优势尤为显著。离线预测任务上，液态模型参数减半却实现2.4倍误差降低和1.8倍推理加速。闭环控制实验（Push-T和PointMaze）结果与离线排名方向一致但噪声更大，说明良好的离线密度建模有助于部署，但并不能完全决定闭环成功率。

【应用价值 / Applications】
该研究为机器人模仿学习提供了一种轻量级、高效率的替代方案，特别适用于计算资源受限或需要实时推理的嵌入式系统。液态多模态策略在数据稀缺的实际场景中具有显著优势，可降低数据采集成本并加速策略部署，适用于工业装配、家庭服务机器人等需要快速响应的交互式任务。
