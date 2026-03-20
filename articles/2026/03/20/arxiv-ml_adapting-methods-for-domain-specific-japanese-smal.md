---
title: "Adapting Methods for Domain-Specific Japanese Small LMs: Scale, Architecture, and Quantization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18037"
published: "2026-03-20"
fetched: "2026-03-20T12:06:01.171606"
---

Computer Science > Machine Learning
[Submitted on 12 Mar 2026]
Title:Adapting Methods for Domain-Specific Japanese Small LMs: Scale, Architecture, and Quantization
View PDF HTML (experimental)Abstract:This paper presents a systematic methodology for building domain-specific Japanese small language models using QLoRA fine-tuning. We address three core questions: optimal training scale, base-model selection, and architecture-aware quantization. Stage 1 (Training scale): Scale-learning experiments (1k--5k samples) identify n=4,000 as optimal, where test-set NLL reaches minimum (1.127) before overfitting at 5k samples. Stage 2 (Compare finetuned SLMs): Comparing four Japanese LLMs shows that Llama-3 models with Japanese continual pre-training (Swallow-8B, ELYZA-JP-8B) outperform multilingual models (Qwen2.5-7B). Stage 3 (Quantization): Llama-3 architectures improve under Q4_K_M quantization, while GQA architectures degrade severely (Qwen2.5: -0.280 points). Production recommendation: Swallow-8B Q4_K_M achieves 2.830/3 score, 8.9 s/question, 4.9 GB size. The methodology generalizes to low-resource technical domains and provides actionable guidance for compact Japanese specialist LMs on consumer hardware.
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
