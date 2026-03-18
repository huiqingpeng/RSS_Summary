---
title: "TempCore: Are Video QA Benchmarks Temporally Grounded? A Frame Selection Sensitivity Analysis and Benchmark"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.01167"
published: "2026-03-18"
fetched: "2026-03-18T17:11:00.694411"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 1 Sep 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:TempCore: Are Video QA Benchmarks Temporally Grounded? A Frame Selection Sensitivity Analysis and Benchmark
View PDF HTML (experimental)Abstract:Vision-language models (VLMs) can ingest only a limited number of video frames, making frame selection a practical necessity. But do current Video QA benchmarks genuinely require temporal frame selection, or can most questions be answered regardless of which frames are shown? We introduce Frame Selection Sensitivity (FSS), a per-sample diagnostic that measures how much VLM accuracy changes when the most relevant frames are replaced with the least relevant ones. Across six benchmarks and eight VLMs, we find that a large majority of samples are frame-agnostic: only a minority are genuinely sensitive to frame choice. Combining FSS with a Language Independence Score (LIS) reveals that merely 8--33% of samples are Temporally Sensitive. We construct TempCore, compact evaluation subsets that isolate these temporal samples from existing benchmarks, and will release code and per-sample annotations upon publication.
Submission history
From: Hyunjong Ok [view email][v1] Mon, 1 Sep 2025 06:39:08 UTC (1,033 KB)
[v2] Tue, 17 Mar 2026 13:01:54 UTC (3,610 KB)
Current browse context:
cs.CV
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
