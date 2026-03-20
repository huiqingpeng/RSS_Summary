---
title: "Balancing Performance and Fairness in Explainable AI for Anomaly Detection in Distributed Power Plants Monitoring"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18954"
published: "2026-03-20"
summarized: "2026-03-20T12:17:23.157598"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对分布式发电厂监控中的异常检测问题，提出了一个兼顾性能、可解释性和公平性的监督式机器学习框架。研究整合了多种集成学习模型（LightGBM、XGBoost等）与高级重采样技术（SMOTE-Tomek Links、ENN）来处理极端类别不平衡问题，并通过SHAP实现模型可解释性，利用差异影响比（DIR）和最大均值差异（MMD）分别量化公平性和域迁移。实验结果表明，LightGBM在F1分数达到0.99的同时保持了较低的跨集群偏差（DIR≈0.95），证明了三者平衡的可行性。

【方法概述 / Method】
论文采用集成学习方法（LightGBM、XGBoost、Random Forest、CatBoost、GBDT、AdaBoost）与基线模型（SVM、KNN、MLP、逻辑回归）相结合，并应用SMOTE-Tomek Links和ENN等高级重采样技术处理类别不平衡。可解释性通过SHAP值分析实现，公平性评估采用差异影响比（DIR），模型泛化能力则通过最大均值差异（MMD）衡量跨区域域迁移。

【实验结果 / Results】
集成模型显著优于基线模型，其中LightGBM表现最佳，F1分数达到0.99，且跨运营集群的差异影响比接近0.95，表明公平性良好。SHAP分析识别出燃油消耗率和日运行时间为异常检测的主导预测因子，为运营商提供了可操作的洞察。MMD分析有效捕捉了不同区域间的域迁移特征。

【应用价值 / Applications】
该研究为工业电力管理领域提供了可部署的实时异常检测解决方案，通过容器化服务实现低延迟预测和可解释输出，特别适用于依赖柴油发电机的电信基础设施监控。研究成果有助于降低维护成本、保障运营连续性，并推动能源领域更加公平、透明的人工智能系统应用，对发展中国家分布式能源管理具有重要实践意义。
