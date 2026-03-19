---
title: "VideoAtlas: Navigating Long-Form Video in Logarithmic Compute"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17948"
published: "2026-03-19"
fetched: "2026-03-19T16:19:12.599759"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:VideoAtlas: Navigating Long-Form Video in Logarithmic Compute
View PDF HTML (experimental)Abstract:Extending language models to video introduces two challenges: representation, where existing methods rely on lossy approximations, and long-context, where caption- or agent-based pipelines collapse video into text and lose visual fidelity. To overcome this, we introduce \textbf{VideoAtlas}, a task-agnostic environment to represent video as a hierarchical grid that is simultaneously lossless, navigable, scalable, caption- and preprocessing-free. An overview of the video is available at a glance, and any region can be recursively zoomed into, with the same visual representation used uniformly for the video, intermediate investigations, and the agent's memory, eliminating lossy text conversion end-to-end. This hierarchical structure ensures access depth grows only logarithmically with video length. For long-context, Recursive Language Models (RLMs) recently offered a powerful solution for long text, but extending them to visual domain requires a structured environment to recurse into, which \textbf{VideoAtlas} provides. \textbf{VideoAtlas} as a Markov Decision Process unlocks Video-RLM: a parallel Master-Worker architecture where a Master coordinates global exploration while Workers concurrently drill into assigned regions to accumulate lossless visual evidence. We demonstrate three key findings: (1)~logarithmic compute growth with video duration, further amplified by a 30-60\% multimodal cache hit rate arising from the grid's structural reuse. (2)~environment budgeting, where bounding the maximum exploration depth provides a principled compute-accuracy hyperparameter. (3)~emergent adaptive compute allocation that scales with question granularity. When scaling from 1-hour to 10-hour benchmarks, Video-RLM remains the most duration-robust method with minimal accuracy degradation, demonstrating that structured environment navigation is a viable and scalable paradigm for video understanding.
Submission history
From: Mohamed Eltahir [view email][v1] Wed, 18 Mar 2026 17:20:19 UTC (21,001 KB)
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
