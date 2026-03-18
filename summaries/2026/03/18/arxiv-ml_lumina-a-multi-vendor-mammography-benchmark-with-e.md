---
title: "LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14644"
published: "2026-03-18"
summarized: "2026-03-18T17:16:48.133776"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出了LUMINA，一个经过精心策划的多厂商全视野数字乳腺X线摄影（FFDM）数据集，包含1824张来自468位患者的图像，涵盖6种采集系统和高低两种能量成像风格，并附有病理确认标签、BI-RADS评估和乳腺密度注释。为应对厂商和能量引起的域偏移，作者提出了一种前景像素空间对齐方法"能量协调"，将图像映射到低能量参考同时保留病灶形态。实验表明，协调方法能跨架构提升性能并产生更聚焦的Grad-CAM响应，EfficientNet-B0在诊断任务上达到93.54% AUC，Swin-T在密度预测上取得89.43%的宏观AUC。

【方法概述 / Method】

研究采用前景像素空间对齐技术进行"能量协调"，仅对乳腺组织区域进行变换，将高能量图像映射到低能量参考分布，同时保持病灶形态学特征不变。该方法在像素空间直接操作，无需对抗训练或风格迁移网络，具有模型无关性。基准测试涵盖了CNN（EfficientNet-B0/B4）和Transformer（Swin-T）架构，在单视图和双视图设置下评估三种临床任务。

【实验结果 / Results】

双视图模型持续优于单视图模型；EfficientNet-B0在良恶性诊断任务上达到93.54% AUC，Swin-T在乳腺密度预测上取得最佳宏观AUC 89.43%；能量协调方法跨架构一致提升性能，并使Grad-CAM热力图更加聚焦病灶区域而非分散到整个乳腺组织。协调后的模型对厂商和能量变化的鲁棒性显著增强。

【应用价值 / Applications】

LUMINA为乳腺AI研究提供了首个显式编码采集能量和厂商元数据的多厂商基准，解决了现有数据集规模小、标注有限、厂商单一等瓶颈。能量协调框架可直接部署于临床环境，使在不同设备（如GE、Hologic、Siemens等）采集的图像能够标准化处理，提升AI模型在实际医疗场景中的泛化能力和可靠性，推动可部署的乳腺筛查辅助诊断系统发展。
