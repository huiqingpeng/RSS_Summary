---
title: "Quotient Geometry and Persistence-Stable Metrics for Swarm Configurations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18041"
published: "2026-03-20"
summarized: "2026-03-20T12:06:24.518878"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对多智能体群体（swarm）和星座（constellation）重构问题，提出了一种商空间几何框架和持久稳定的度量方法。作者定义了商构型空间 $\mathcal{S}_n(M,G)=M^n/(G\times S_n)$ 和构型匹配度量 $d_{M,G}$，该度量通过对环境对称群 $G$ 和重标号群 $S_n$ 进行最坏情况分配优化得到，是Gromov-Hausdorff距离的结构化松弛。结合Vietoris-Rips持久同调的稳定性，证明了持久签名满足 $d_B(\Phi_k([x]),\Phi_k([y]))\le d_{M,G}([x],[y])$，为重构监控提供了稳定的拓扑签名。论文还分析了该度量空间的几何性质，并在相位圆模型中证明了条件逆定理，建立了持久签名与度量之间的双向控制。

【方法概述 / Method】

论文采用商空间构造方法，将无序点构型空间模去环境对称群 $G$（如旋转、平移）和置换群 $S_n$ 的作用，得到商构型空间 $\mathcal{S}_n(M,G)$。核心度量 $d_{M,G}$ 通过优化问题定义：在所有对称变换 $g\in G$ 和重标号 $\sigma\in S_n$ 上最小化最坏情况下的代理间距离误差。该方法将拓扑数据分析中的持久同调（persistence homology）与度量几何相结合，利用Vietoris-Rips复形构造持久签名 $\Phi_k$。

【实验结果 / Results】

论文证明了商度量空间 $(\mathcal{S}_n(M,G),d_{M,G})$ 的关键几何性质：在 $M$ 紧致/完备且 $G$ 紧致的假设下，该空间紧致/完备且度量诱导商拓扑；若 $M$ 为测地空间，则商空间也是测地的，并在碰撞和对称层上呈现分层奇异性。作者识别了签名非单射性的两种机制：对称不匹配（symmetry-mismatch）和持久压缩（persistence-compression）。在相位圆模型中，证明了在半圆支撑和间隙标号边距条件下，$H_0$ 签名关于 $d_{M,G}$ 是局部双Lipschitz的，并给出了显式Lipschitz常数。

【应用价值 / Applications】

该研究直接应用于卫星星座重构和无人机编队控制等场景，其中智能体身份可互换且系统具有物理对称性（如旋转不变性）。持久稳定的签名为实时监控群体构型变化、检测异常重构行为提供了计算高效的拓扑工具，避免了昂贵的最优分配计算。方法在 $\mathbb{S}^2$（球面卫星星座）和 $\mathbb{T}^m$（环面编队）上的示例展示了其对实际多智能体系统的适用性，可支持任务规划、碰撞避免和构型相似性评估等任务。
