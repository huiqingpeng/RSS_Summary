---
title: "MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24044"
published: "2026-03-26"
fetched: "2026-03-27T07:19:58.408649"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning
View PDF HTML (experimental)Abstract:Standard LoRA fine-tuning of Mixture-of-Experts (MoE) models applies adapters to every expert, yet our profiling shows that per-layer expert routing is highly skewed: a small subset of experts handles most tokens in each layer, while many others are rarely activated ("cold"). We propose MoE-Sieve, a simple routing-guided framework for LoRA fine-tuning, and pair it with a systematic profiling study of expert routing across architectures and tasks. The method is simple: profile routing counts on a small calibration set, select the top-k most-routed experts per layer, and apply LoRA only to those experts. Across two architecturally distinct MoE models and three diverse tasks, tuning only the top 25% routed experts per layer remains competitive with full LoRA, with mean differences within +/-1 percentage point across all conditions. This reduces LoRA trainable parameters by 70-73%, adapter checkpoint size by 71-73%, and wall-clock training time by up to 50%. We also observe a non-monotonic relationship between expert count and seed-to-seed variance, consistent with the hypothesis that adapting cold experts can introduce gradient noise without improving accuracy. Further ablations show that random expert selection at matched budget is about 2.5 percentage points worse, indicating that the routing signal matters, while greedy per-layer budget optimization does not improve over uniform top-k.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
