---
title: "When Generative Augmentation Hurts: A Benchmark Study of GAN and Diffusion Models for Bias Correction in AI Classification Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16134"
published: "2026-03-18"
fetched: "2026-03-18T16:10:34.958128"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:When Generative Augmentation Hurts: A Benchmark Study of GAN and Diffusion Models for Bias Correction in AI Classification Systems
View PDFAbstract:Generative models are widely used to compensate for class imbalance in AI training pipelines, yet their failure modes under low-data conditions are poorly understood. This paper reports a controlled benchmark comparing three augmentation strategies applied to a fine-grained animal classification task: traditional transforms, FastGAN, and Stable Diffusion 1.5 fine-tuned with Low-Rank Adaptation (LoRA). Using the Oxford-IIIT Pet Dataset with eight artificially underrepresented breeds, we find that FastGAN augmentation does not merely underperform at very low training set sizes but actively increases classifier bias, with a statistically significant large effect across three random seeds (bias gap increase: +20.7%, Cohen's d = +5.03, p = 0.013). The effect size here is large enough to give confidence in the direction of the finding despite the small number of seeds. Feature embedding analysis using t-distributed Stochastic Neighbor Embedding reveals that FastGAN images for severe-minority breeds form tight isolated clusters outside the real image distribution, a pattern consistent with mode collapse. Stable Diffusion with Low-Rank Adaptation produced the best results overall, achieving the highest macro F1 (0.9125 plus or minus 0.0047) and a 13.1% reduction in the bias gap relative to the unaugmented baseline. The data suggest a sample-size boundary somewhere between 20 and 50 training images per class below which GAN augmentation becomes harmful in this setting, though further work across additional domains is needed to establish where that boundary sits more precisely. All experiments run on a consumer-grade GPU with 6 to 8 GB of memory, with no cloud compute required.
Submission history
From: Shesh Narayan Gupta [view email][v1] Tue, 17 Mar 2026 05:37:17 UTC (1,574 KB)
Current browse context:
cs.CV
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
