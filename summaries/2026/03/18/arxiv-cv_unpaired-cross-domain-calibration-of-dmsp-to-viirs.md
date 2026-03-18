---
title: "Unpaired Cross-Domain Calibration of DMSP to VIIRS Nighttime Light Data Based on CUT Network"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16385"
published: "2026-03-18"
summarized: "2026-03-18T18:12:16.612083"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种基于对比非配对翻译（CUT）网络的跨传感器校准方法，将DMSP夜间灯光数据转换为VIIRS格式，以解决传感器不兼容导致的长期分析障碍。该方法利用多层块级对比学习最大化对应块间的互信息，在保持内容一致性的同时学习跨域相似性。验证结果表明生成的VIIRS-like数据与实际VIIRS观测具有高度一致性（R² > 0.87），为扩展夜间灯光时间序列提供了可靠方案。

【方法概述 / Method】
研究采用CUT网络进行无配对跨域图像翻译，通过多层块级对比学习机制提取DMSP与VIIRS数据间的域不变特征。网络利用2012-2013年重叠期数据进行训练，无需像素级配准的图像对，即可学习从DMSP域到VIIRS域的映射关系。

【实验结果 / Results】
生成的VIIRS-like数据与实际VIIRS观测在辐射特性上表现出高度一致性，R²系数超过0.87；校准后的数据与社会经济指标的相关性显著提升，有效消除了DMSP原始数据中的饱和和过曝等缺陷。该方法成功将1992-2013年的历史DMSP数据转换为与VIIRS兼容的格式。

【应用价值 / Applications】
该方法为城市化和人类活动长期监测提供了连贯的数据基础，解决了DMSP与VIIRS两代卫星数据融合的关键技术瓶颈。研究成果可支持气候变化研究、能源消费分析、可持续发展目标评估等需要长时序夜间灯光数据的应用领域。
