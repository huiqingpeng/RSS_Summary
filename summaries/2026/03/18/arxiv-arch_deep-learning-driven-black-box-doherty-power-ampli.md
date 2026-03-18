---
title: "Deep Learning-Driven Black-Box Doherty Power Amplifier with Pixelated Output Combiner and Extended Efficiency Range"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.16565"
published: "2026-03-18"
summarized: "2026-03-18T15:31:50.950137"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于深度学习的逆设计方法，用于具有多端口像素化输出合路网络的Doherty功率放大器（PA）。研究团队开发了深度卷积神经网络（CNN）作为电磁（EM）替代模型，以准确快速地预测像素化无源网络的S参数。通过将该CNN替代模型与黑盒Doherty框架及遗传算法（GA）优化器相结合，成功合成了复杂的Doherty合路器，实现了使用完全对称器件的扩展回退效率范围。

【方法概述 / Method】

该研究采用深度卷积神经网络（CNN）构建电磁替代模型，替代传统的耗时的全波电磁仿真；结合黑盒Doherty功率放大器框架和遗传算法（GA）优化器，对像素化的多端口无源合路网络进行自动化逆设计。像素化输出合路器通过离散化的金属像素单元实现，为优化算法提供了高度灵活的设计空间。

【实验结果 / Results】

研究团队设计并制造了两款采用GaN HEMT晶体管的三端口像素化合路器Doherty PA原型。测试结果显示：在2.75 GHz频率下，两款原型均实现超过74%的最大漏极效率和44.1 dBm以上的输出功率；在9 dB回退功率电平下，漏极效率保持在52%以上。使用20 MHz 5G NR类波形（PAPR=9.0 dB）测试时，经数字预失真（DPD）后，两款设计的平均功率附加效率（PAE）均超过51%，邻道泄漏比（ACLR）优于-60.8 dBc。

【应用价值 / Applications】

该研究为5G及未来无线通信系统中的高效率功率放大器设计提供了自动化、快速的设计方法，特别适用于需要宽动态范围高效率的基站应用场景。深度学习驱动的黑盒设计方法可显著缩短复杂无源网络的设计周期，降低对专家经验的依赖，有望推广至其他射频/微波电路的智能化设计领域。
