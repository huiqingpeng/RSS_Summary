---
title: "Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24511"
published: "2026-03-27"
fetched: "2026-03-28T07:10:52.709286"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs
View PDF HTML (experimental)Abstract:LLM agents like Claude Code can not only write code but also be used for autonomous AI research and engineering \citep{rank2026posttrainbench, novikov2025alphaevolve}. We show that an \emph{autoresearch}-style pipeline \citep{karpathy2026autoresearch} powered by Claude Code discovers novel white-box adversarial attack \textit{algorithms} that \textbf{significantly outperform all existing (30+) methods} in jailbreaking and prompt injection evaluations.
Starting from existing attack implementations, such as GCG~\citep{zou2023universal}, the agent iterates to produce new algorithms achieving up to 40\% attack success rate on CBRN queries against GPT-OSS-Safeguard-20B, compared to $\leq$10\% for existing algorithms (\Cref{fig:teaser}, left).
The discovered algorithms generalize: attacks optimized on surrogate models transfer directly to held-out models, achieving \textbf{100\% ASR against Meta-SecAlign-70B} \citep{chen2025secalign} versus 56\% for the best baseline (\Cref{fig:teaser}, middle). Extending the findings of~\cite{carlini2025autoadvexbench}, our results are an early demonstration that incremental safety and security research can be automated using LLM agents. White-box adversarial red-teaming is particularly well-suited for this: existing methods provide strong starting points, and the optimization objective yields dense, quantitative feedback. We release all discovered attacks alongside baseline implementations and evaluation code at this https URL.
Submission history
From: Alexander Panfilov [view email][v1] Wed, 25 Mar 2026 16:50:56 UTC (191 KB)
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
