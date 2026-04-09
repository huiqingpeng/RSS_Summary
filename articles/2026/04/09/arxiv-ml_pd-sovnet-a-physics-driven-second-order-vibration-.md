---
title: "PD-SOVNet: A Physics-Driven Second-Order Vibration Operator Network for Estimating Wheel Polygonal Roughness from Axle-Box Vibrations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06620"
published: "2026-04-09"
fetched: "2026-04-10T07:05:03.975639"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:PD-SOVNet: A Physics-Driven Second-Order Vibration Operator Network for Estimating Wheel Polygonal Roughness from Axle-Box Vibrations
View PDF HTML (experimental)Abstract:Quantitative estimation of wheel polygonal roughness from axle-box vibration signals is a challenging yet practically relevant problem for rail-vehicle condition monitoring. Existing studies have largely focused on detection, identification, or severity classification, while continuous regression of multi-order roughness spectra remains less explored, especially under real operational data and unseen-wheel conditions. To address this problem, this paper presents PD-SOVNet, a physics-guided gray-box framework that combines shared second-order vibration kernels, a $4\times4$ MIMO coupling module, an adaptive physical correction branch, and a Mamba-based temporal branch for estimating the 1st--40th-order wheel roughness spectrum from axle-box vibrations. The proposed design embeds modal-response priors into the model while retaining data-driven flexibility for sample-dependent correction and residual temporal dynamics. Experiments on three real-world datasets, including operational data and real fault data, show that the proposed method provides competitive prediction accuracy and relatively stable cross-wheel performance under the current data protocol, with its most noticeable advantage observed on the more challenging Dataset III. Noise injection experiments further indicate that the Mamba temporal branch helps mitigate performance degradation under perturbed inputs. These results suggest that structured physical priors can be beneficial for stabilizing roughness regression in practical rail-vehicle monitoring scenarios, although further validation under broader operating conditions and stricter comparison protocols is still needed.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
