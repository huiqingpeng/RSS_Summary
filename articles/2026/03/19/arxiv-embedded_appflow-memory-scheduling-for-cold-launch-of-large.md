---
title: "AppFlow: Memory Scheduling for Cold Launch of Large Apps on Mobile and Vehicle Systems"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.17259"
published: "2026-03-19"
fetched: "2026-03-19T12:02:52.294956"
---

Computer Science > Operating Systems
[Submitted on 18 Mar 2026]
Title:AppFlow: Memory Scheduling for Cold Launch of Large Apps on Mobile and Vehicle Systems
View PDF HTML (experimental)Abstract:GB-scale large apps like on-device LLMs and rich media editors are becoming the next-generation trend, but their heavy memory and I/O demands, especially during multitasking, cause devices to reclaim or kill processes, turning warm apps into cold launches. The challenge lies not in storing them, but in fast, accurate launching. For users, 1s is the usability cliff, yet our measurements show 86.6\% of GB-scale cold launches exceed it. Also, Android Vitals flags only $\geq$ 5s as slow, exposing a large satisfaction gap. Existing optimizations are designed in isolation and conflict. For example, preloading reduces I/O stalls but consumes scarce memory and is undone by reclamation, while reclamation and killing free memory but sacrifice background survivability, leading to repeated cold relaunches. Our key insight is that, although multitasking makes runtime behavior complex, each app's file access pattern remains predictable. The challenge lies in exploiting this predictability, i.e., preloading without exhausting memory, reclaiming without undoing gains, and killing selectively to preserve background survivability. We introduce AppFlow, a prediction-based system-wide scheduler that integrates a Selective File Preloader, an Adaptive Memory Reclaimer, and a Context-Aware Process Killer. Implemented across the Android framework and Linux kernel without app changes, AppFlow cuts GB-scale cold-launch latency by 66.5\% (e.g., 2s$\rightarrow$690ms) and sustains 95\% of launches within 1s over a 100-day test, significantly improving responsiveness and multitasking experience.
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
