---
title: "GNNVerifier: Graph-based Verifier for LLM Task Planning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14730"
published: "2026-03-18"
fetched: "2026-03-18T17:07:05.454123"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:GNNVerifier: Graph-based Verifier for LLM Task Planning
View PDF HTML (experimental)Abstract:Large language models (LLMs) facilitate the development of autonomous agents. As a core component of such agents, task planning aims to decompose complex natural language requests into concrete, solvable sub-tasks. Since LLM-generated plans are frequently prone to hallucinations and sensitive to long-context prom-pts, recent research has introduced plan verifiers to identify and correct potential flaws. However, most existing approaches still rely on an LLM as the verifier via additional prompting for plan review or self-reflection. LLM-based verifiers can be misled by plausible narration and struggle to detect failures caused by structural relations across steps, such as type mismatches, missing intermediates, or broken dependencies. To address these limitations, we propose a graph-based verifier for LLM task planning. Specifically, the proposed method has four major components: Firstly, we represent a plan as a directed graph with enriched attributes, where nodes denote sub-tasks and edges encode execution order and dependency constraints. Secondly, a graph neural network (GNN) then performs structural evaluation and diagnosis, producing a graph-level plausibility score for plan acceptance as well as node/edge-level risk scores to localize erroneous regions. Thirdly, we construct controllable perturbations from ground truth plan graphs, and automatically generate training data with fine-grained annotations. Finally, guided by the feedback from our GNN verifier, we enable an LLM to conduct local edits (e.g., tool replacement or insertion) to correct the plan when the graph-level score is insufficient. Extensive experiments across diverse datasets, backbone LLMs, and planners demonstrate that our GNNVerifier achieves significant gains in improving plan quality. Our data and code is available at this https URL.
Submission history
From: Yu Hao [view email][v1] Mon, 16 Mar 2026 02:05:21 UTC (3,454 KB)
[v2] Tue, 17 Mar 2026 04:26:31 UTC (3,454 KB)
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
