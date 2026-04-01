---
title: "Realistic Market Impact Modeling for Reinforcement Learning Trading Environments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29086"
published: "2026-04-01"
summarized: "2026-04-02T07:15:13.651784"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对强化学习（RL）在金融交易中的应用，指出现有开源回测环境普遍忽略或简化交易成本，导致智能体学到的策略在真实执行中失效。作者开发了三个兼容Gymnasium的交易环境（MACE股票交易、保证金交易和组合优化），整合基于Almgren-Chriss框架和实证平方根冲击定律的非线性市场冲击模型。实验表明，成本模型显著改变算法绝对表现和相对排名，且与超参数优化、环境类型存在复杂交互作用。

【方法概述 / Method】

论文构建了MACE（Market-Adjusted Cost Execution）环境套件，采用Almgren-Chriss框架的永久冲击模型（含指数衰减）和平方根冲击定律的瞬时冲击模型，实现可插拔的成本计算模块。研究使用Optuna对五种深度强化学习算法（A2C、PPO、DDPG、SAC、TD3）进行超参数优化，在NASDAQ-100数据上对比固定10个基点基准与AC模型的差异。

【实验结果 / Results】

AC模型使日均交易成本从20万美元骤降至8千美元，换手率从19%降至1%；超参数优化可将成本降低82%；算法-成本模型交互呈现强环境特异性：DDPG在保证金交易中样本外夏普比率从-2.1跃升至0.3，而SAC则从-0.5跌至-1.2。成本模型同时改变了各算法的绝对收益和相对排序。

【应用价值 / Applications】

该研究为量化金融提供了更真实的RL训练基础设施，可帮助策略开发者识别在真实市场冲击下稳健的策略，避免因成本低估导致的过度交易。开源发布的FinRL-Meta扩展包支持学术界和业界开展更可靠的算法交易研究，尤其适用于高频交易、保证金交易等对执行成本敏感的场景。
