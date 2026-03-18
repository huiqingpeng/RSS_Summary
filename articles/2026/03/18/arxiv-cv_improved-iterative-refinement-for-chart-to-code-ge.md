---
title: "Improved Iterative Refinement for Chart-to-Code Generation via Structured Instruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.14837"
published: "2026-03-18"
fetched: "2026-03-18T18:26:09.355820"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 Jun 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Improved Iterative Refinement for Chart-to-Code Generation via Structured Instruction
View PDF HTML (experimental)Abstract:Recently, multimodal large language models (MLLMs) have attracted increasing research attention due to their powerful visual understanding capabilities. While they have achieved impressive results on various vision tasks, their performance on chart-to-code generation remains suboptimal. This task requires MLLMs to generate executable code that can reproduce a given chart, demanding not only precise visual understanding but also accurate translation of visual elements into structured code. Directly prompting MLLMs to perform this complex task often yields unsatisfactory results. To address this challenge, we propose {ChartIR}, an iterative refinement method based on structured instruction. First, we distinguish two tasks: visual understanding and code translation. To accomplish the visual understanding component, we design two types of structured instructions: description and difference. The description instruction captures the visual elements of the reference chart, while the difference instruction characterizes the discrepancies between the reference chart and the generated chart. These instructions effectively transform visual features into language representations, thereby facilitating the subsequent code translation process. Second, we decompose the overall chart generation pipeline into two stages: initial code generation and iterative refinement, enabling progressive enhancement of the final output. Experimental results show that, compared to other method, our method achieves superior performance on both the open-source model Qwen2-VL and the closed-source model GPT-4o.
Submission history
From: Chengzhi Xu [view email][v1] Sun, 15 Jun 2025 14:10:16 UTC (875 KB)
[v2] Tue, 17 Mar 2026 07:18:16 UTC (2,137 KB)
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
