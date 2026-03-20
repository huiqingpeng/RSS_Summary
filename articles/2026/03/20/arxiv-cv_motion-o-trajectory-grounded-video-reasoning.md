---
title: "Motion-o: Trajectory-Grounded Video Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18856"
published: "2026-03-20"
fetched: "2026-03-20T15:17:03.556535"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Motion-o: Trajectory-Grounded Video Reasoning
View PDF HTML (experimental)Abstract:Recent research has made substantial progress on video reasoning, with many models leveraging spatio-temporal evidence chains to strengthen their inference capabilities. At the same time, a growing set of datasets and benchmarks now provides structured annotations designed to support and evaluate such reasoning. However, little attention has been paid to reasoning about \emph{how} objects move between observations: no prior work has articulated the motion patterns by connecting successive observations, leaving trajectory understanding implicit and difficult to verify. We formalize this missing capability as Spatial-Temporal-Trajectory (STT) reasoning and introduce \textbf{Motion-o}, a motion-centric video understanding extension to visual language models that makes trajectories explicit and verifiable. To enable motion reasoning, we also introduce a trajectory-grounding dataset artifact that expands sparse keyframe supervision via augmentation to yield denser bounding box tracks and a stronger trajectory-level training signal. Finally, we introduce Motion Chain of Thought (MCoT), a structured reasoning pathway that makes object trajectories through discrete \texttt{<motion/>} tag summarizing per-object direction, speed, and scale (of velocity) change to explicitly connect grounded observations into trajectories. To train Motion-o, we design a reward function that compels the model to reason directly over visual evidence, all while requiring no architectural modifications. Empirical results demonstrate that Motion-o improves spatial-temporal grounding and trajectory prediction while remaining fully compatible with existing frameworks, establishing motion reasoning as a critical extension for evidence-based video understanding. Code is available at this https URL.
Submission history
From: Sarah Ostadabbas [view email][v1] Thu, 19 Mar 2026 13:00:29 UTC (18,930 KB)
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
