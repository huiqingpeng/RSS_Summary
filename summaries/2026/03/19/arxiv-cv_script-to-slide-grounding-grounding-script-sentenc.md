---
title: "Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16931"
published: "2026-03-19"
summarized: "2026-03-19T14:20:45.572240"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"Script-to-Slide Grounding (S2SG)"任务，旨在将讲解脚本中的句子与幻灯片中的对应对象进行自动匹配，从而实现教学视频的自动化生成。作为该任务的初步探索，作者开发了"Text-S2SG"方法，利用大语言模型完成文本对象的对齐，实验取得了0.924的F1分数。该研究将原本隐式的视频编辑流程形式化为可计算任务，为教学视频制作的自动化奠定了基础。

【方法概述 / Method】
本文采用大语言模型（LLM）作为核心工具，构建Text-S2SG方法来实现脚本句子与幻灯片文本对象之间的语义匹配与对齐。该方法通过理解脚本内容的语义信息，自动识别并关联到幻灯片中相关的文本元素，无需人工标注即可完成 grounding 任务。

【实验结果 / Results】
实验结果表明，所提出的Text-S2SG方法在脚本到幻灯片的文本对象对齐任务上表现优异，F1分数达到0.924，证明了该方法在自动识别和匹配脚本内容与幻灯片元素方面的高效性和准确性。

【应用价值 / Applications】
该研究可广泛应用于在线教育、企业培训和学术报告等领域，能够显著降低制作讲解型幻灯片视频的人力成本。通过自动化将语音脚本与视觉元素对齐并添加特效，该系统有望实现教学视频的快速批量生产，提升内容创作者的生产效率。
