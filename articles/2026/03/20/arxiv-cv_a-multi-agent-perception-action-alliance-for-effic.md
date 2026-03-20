---
title: "A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.14052"
published: "2026-03-20"
fetched: "2026-03-20T16:19:05.840415"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning
View PDF HTML (experimental)Abstract:This paper presents a multi-agent perception-action exploration alliance, dubbed A4VL, for efficient long-video reasoning. A4VL operates in a multi-round perception-action exploration loop with a selection of VLM agents. In each round, the team of agents performs video question-answer (VideoQA) via perception exploration followed by action exploration. During perception exploration, each agent learns to extract query-specific perception clue(s) from a few sampled frames and performs clue-based alignment to find the video block(s) that are most relevant to the query-specific event. During action exploration, A4VL performs video reasoning in three steps: (1) each agent produces its initial answer with rational, (2) all agents collaboratively scores one another through cross-reviews and relevance ranking, and (3) based on whether a satisfactory consensus is reached, the decision is made either to start a new round of perception-action deliberation by pruning (e.g., filtering out the lowest performing agent) and re-staging (e.g., new-clue and matching block based perception-action exploration), or to conclude by producing its final answer. The integration of the multi-agent alliance through multi-round perception-action exploration, coupled with event-driven partitioning and cue-guided block alignment, enables A4VL to effectively scale to real world long videos while preserving high quality video reasoning. Evaluation Results on five popular VideoQA benchmarks show that A4VL outperforms 18 existing representative VLMs and 11 recent methods optimized for long-video reasoning, while achieving significantly lower inference latency. Our code is released at this https URL.
Submission history
From: Xu Yichang [view email][v1] Sat, 14 Mar 2026 17:43:53 UTC (18,800 KB)
[v2] Thu, 19 Mar 2026 15:21:11 UTC (18,800 KB)
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
