---
title: "Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06298"
published: "2026-04-09"
fetched: "2026-04-10T07:04:56.431888"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs
View PDF HTML (experimental)Abstract:Recent alignment work on Large Language Models (LLMs) suggests preference optimization can improve reasoning by shifting probability mass toward better solutions. We test this claim in a resource-constrained setting by applying GRPO with LoRA to SLMs (up to 3B) for math reasoning on GSM8K and MATH datasets with difficulty-stratified analyses. As problem difficulty increases, accuracy plateaus, revealing a capacity boundary: GRPO primarily reshapes output preferences without reliably improving hardest-tier solving. Consistent with this, training GRPO only on lower-difficulty problems matches full-dataset accuracy across difficulty tiers while using only ~45% training steps, indicating diminishing returns from harder samples in this regime. We also find a cross-dataset generalization effect: GSM8K-trained GRPO achieves higher accuracy on the numeric subset of MATH than MATH-trained GRPO, exceeding it by ~5% at 1.5B and by ~3% at 3B. We show that the best achievable gains depend strongly on the base model's prior reasoning competence and the dataset's difficulty profile.
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
