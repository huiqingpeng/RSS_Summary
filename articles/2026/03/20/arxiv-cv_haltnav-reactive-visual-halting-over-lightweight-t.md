---
title: "HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.12696"
published: "2026-03-20"
fetched: "2026-03-20T17:04:37.522113"
---

Computer Science > Robotics
[Submitted on 13 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation
View PDF HTML (experimental)Abstract:Vision-and-Language Navigation (VLN) is shifting from rigid, step-by-step instruction following toward open-vocabulary, goal-oriented autonomy. Achieving this transition without exhaustive routing prompts requires agents to leverage structural priors. While prior work often assumes computationally heavy 2D/3D metric maps, we instead exploit a lightweight, text-based osmAG (OpenStreetMap Area Graph), a floorplan-level topological representation that is easy to obtain and maintain. However, global planning over a prior map alone is brittle in real-world deployments, where local connectivity can change (e.g., closed doors or crowded passages), leading to execution-time failures. To address this gap, we propose a hierarchical navigation framework HaltNav that couples the robust global planning of osmAG with the local exploration and instruction-grounding capability of VLN. Our approach features an MLLM-based brain module, which is capable of high-level task grounding and obstruction awareness. Conditioned on osmAG, the brain converts the global route into a sequence of localized execution snippets, providing the VLN executor with prior-grounded, goal-centric sub-instructions. Meanwhile, it detects local anomalies via a mechanism we term Reactive Visual Halting (RVH), which interrupts the local control loop, updates osmAG by invalidating the corresponding topology, and triggers replanning to orchestrate a viable detour. To train this halting capability efficiently, we introduce a data synthesis pipeline that leverages generative models to inject realistic obstacles into otherwise navigable scenes, substantially enriching hard negative samples. Extensive experiments demonstrate that our hierarchical framework outperforms several baseline methods without tedious language instructions, and significantly improves robustness for long-horizon vision-language navigation under environmental changes.
Submission history
From: Pingcong Li [view email][v1] Fri, 13 Mar 2026 06:22:35 UTC (33,226 KB)
[v2] Thu, 19 Mar 2026 01:12:15 UTC (33,226 KB)
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
