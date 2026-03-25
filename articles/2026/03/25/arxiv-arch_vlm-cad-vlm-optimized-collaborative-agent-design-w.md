---
title: "VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2601.07315"
published: "2026-03-25"
fetched: "2026-03-26T07:07:54.607126"
---

Computer Science > Multiagent Systems
[Submitted on 12 Jan 2026 (v1), last revised 24 Mar 2026 (this version, v4)]
Title:VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing
View PDF HTML (experimental)Abstract:Vision Language Models (VLMs) have demonstrated remarkable potential in multimodal reasoning, yet they inherently suffer from spatial blindness and logical hallucinations when interpreting densely structured engineering content, such as analog circuit schematics. To address these challenges, we propose a Vision Language Model-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing (VLM-CAD) designed for robust, step-by-step reasoning over multimodal evidence. VLM-CAD bridges the modality gap by integrating a neuro-symbolic structural parsing module, Image2Net, which transforms raw pixels into explicit topological graphs and structured JSON representations to anchor VLM interpretation in deterministic facts. To ensure the reliability required for engineering decisions, we further propose ExTuRBO, an Explainable Trust Region Bayesian Optimization method. ExTuRBO serves as an explainable grounding engine, employing agent-generated semantic seeds to warm-start local searches and utilizing Automatic Relevance Determination to provide quantified evidence for the VLM's decisions. Experimental results on two complex circuit benchmarks demonstrate that VLM-CAD significantly enhances spatial reasoning accuracy and maintains physics-based explainability. VLM-CAD consistently satisfies complex specification requirements while achieving low power consumption, with a total runtime under 66 minutes, marking a significant step toward robust, explainable multimodal reasoning in specialized technical domains.
Submission history
From: Guanyuan Pan [view email][v1] Mon, 12 Jan 2026 08:37:32 UTC (1,062 KB)
[v2] Thu, 22 Jan 2026 11:46:08 UTC (1,145 KB)
[v3] Wed, 28 Jan 2026 02:59:53 UTC (1,145 KB)
[v4] Tue, 24 Mar 2026 07:44:42 UTC (1,258 KB)
Current browse context:
cs.MA
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
