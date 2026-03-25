---
title: "TorR: Towards Brain-Inspired Task-Oriented Reasoning via Cache-Oriented Algorithm-Architecture Co-design"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22855"
published: "2026-03-25"
fetched: "2026-03-26T07:06:41.726444"
---

Computer Science > Hardware Architecture
[Submitted on 24 Mar 2026]
Title:TorR: Towards Brain-Inspired Task-Oriented Reasoning via Cache-Oriented Algorithm-Architecture Co-design
View PDF HTML (experimental)Abstract:Task-oriented object detection (TOOD) atop CLIP offers open-vocabulary, prompt-driven semantics, yet dense per-window computation and heavy memory traffic hinder real-time, power-limited edge deployment. We present \emph{TorR}, a brain-inspired \textbf{algorithm--architecture co-design} that \textbf{replaces CLIP-style dense alignment with a hyperdimensional (HDC) associative reasoner} and turns temporal coherence into reuse. On the \emph{algorithm} side, TorR reformulates alignment as HDC similarity and graph composition, introducing \emph{partial-similarity reuse} via (i) query caching with per-class score accumulation, (ii) exact $\delta$-updates when only a small set of hypervector bits change, and (iii) similarity/load-gated bypass under high system load. On the \emph{architecture} side, TorR instantiates a lane-scalable, bit-sliced item memory with bank/precision gating and a lightweight controller that schedules bypass/$\delta$/full paths to meet RT-30/RT-60 targets as object counts vary. Synthesized in a TSMC 28\,nm process and exercised with a cycle-accurate simulator, TorR sustains real-time throughput with millijoule-scale energy per window ($\approx$50\,mJ at 60\,FPS; $\approx$113\,mJ at 30\,FPS) and low latency jitter, while delivering competitive AP@0.5 across five task prompts (mean 44.27\%) within a bounded margin to strong VLM baselines, but at orders-of-magnitude lower energy. The design exposes deployment-time configurability (effective dimension $D'$, thresholds, precision) to trade accuracy, latency, and energy for edge budgets.
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
