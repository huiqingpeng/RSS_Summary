---
title: "Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19544"
published: "2026-03-23"
summarized: "2026-03-24T07:19:22.076368"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本论文针对科学AI应用中的数据隐私、主权和规模限制问题，提出了一种跨高性能计算（HPC）设施的联邦学习（FL）框架。该框架基于APPFL构建，利用Globus Compute和Transfer进行跨设施编排，并在美国能源部（DOE）的四台领导级超级计算机上进行了评估。研究表明，跨HPC设施的FL实验在实践中可行，系统异构性和调度条件对训练性能有显著影响，且算法设计需考虑调度器感知。论文还通过化学指令数据集上的大语言模型微调验证了科学适用性。

【方法概述 / Method】

论文构建了基于Advanced Privacy-Preserving Federated Learning（APPFL）框架的跨设施联邦学习系统，采用Globus Compute和Globus Transfer实现跨异构HPC环境的任务编排与数据传输。该方案支持在多个DOE超级计算设施间进行分布式模型训练，无需集中原始数据，同时应对HPC特有的调度约束和网络拓扑挑战。

【实验结果 / Results】

研究成功在四台美国能源部领导级超级计算机（包括Argonne、Oak Ridge、Lawrence Berkeley和Sandia国家实验室的设施）上部署并运行了联邦学习实验。实验表征了影响训练性能的关键异构性来源，证明了在真实HPC调度条件下算法选择的重要性，并展示了跨设施FL在科学工作负载中的实际可行性。

【应用价值 / Applications】

该研究为科学基础模型训练提供了隐私保护和数据主权合规的解决方案，特别适用于涉及敏感数据（如医疗记录、专有实验数据）或地理分布数据的科学研究场景。跨HPC设施联邦学习使研究人员能够利用全国范围内的超算资源协同训练大规模模型，同时满足数据本地化要求，为气候建模、材料发现、生物信息学等领域的分布式科学AI应用奠定了基础。
