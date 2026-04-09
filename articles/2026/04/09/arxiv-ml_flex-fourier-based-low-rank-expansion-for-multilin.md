---
title: "FLeX: Fourier-based Low-rank EXpansion for multilingual transfer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06253"
published: "2026-04-09"
fetched: "2026-04-10T07:04:53.918562"
---

Computer Science > Machine Learning
[Submitted on 6 Apr 2026]
Title:FLeX: Fourier-based Low-rank EXpansion for multilingual transfer
View PDF HTML (experimental)Abstract:Cross-lingual code generation is critical in enterprise environments where multiple programming languages coexist. However, fine-tuning large language models (LLMs) individually for each language is computationally prohibitive. This paper investigates whether parameter-efficient fine-tuning methods and optimizer enhancements can improve cross-lingual transfer from Python to languages like Java. We fine-tune the Code Llama 7B model using low-rank adaptation (LoRA) to optimize a small subset of parameters and compare Adam and Sophia optimizers, while exploring a novel Fourier-based regularization technique. Our contributions include: (1)demonstrating that LoRA fine-tuning on a small, high-quality dataset (MBPP) can exceed the pass@1 performance of the more broadly fine-tuned Code Llama-Python-7B model (40.1% vs. 38.4%); (2) showing that while Sophia achieves faster convergence than Adam, final pass@1 scores show marginal differences; and (3) presenting evidence that Fourier-based regularization during fine-tuning significantly improves cross-lingual transfer, achieving 42.1% pass@1 on Java tasks compared to the 34.2% baseline. These findings suggest that combining LoRA, optimized training methods, and frequency-domain regularization can efficiently adapt single-language LLMs to perform well across multiple programming languages.
Submission history
From: Gaurav Narasimhan [view email][v1] Mon, 6 Apr 2026 19:26:13 UTC (2,435 KB)
Current browse context:
cs.LG
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
