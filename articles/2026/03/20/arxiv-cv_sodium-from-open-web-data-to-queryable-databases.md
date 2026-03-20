---
title: "SODIUM: From Open Web Data to Queryable Databases"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18447"
published: "2026-03-20"
fetched: "2026-03-20T16:08:08.613092"
---

Computer Science > Databases
[Submitted on 19 Mar 2026]
Title:SODIUM: From Open Web Data to Queryable Databases
View PDF HTML (experimental)Abstract:During research, domain experts often ask analytical questions whose answers require integrating data from a wide range of web sources. Thus, they must spend substantial effort searching, extracting, and organizing raw data before analysis can begin. We formalize this process as the SODIUM task, where we conceptualize open domains such as the web as latent databases that must be systematically instantiated to support downstream querying. Solving SODIUM requires (1) conducting in-depth and specialized exploration of the open web, which is further strengthened by (2) exploiting structural correlations for systematic information extraction and (3) integrating collected information into coherent, queryable database instances.
To quantify the challenges in automating SODIUM, we construct SODIUM-Bench, a benchmark of 105 tasks derived from published academic papers across 6 domains, where systems are tasked with exploring the open web to collect and aggregate data from diverse sources into structured tables. Existing systems struggle with SODIUM tasks: we evaluate 6 advanced AI agents on SODIUM-Bench, with the strongest baseline achieving only 46.5% accuracy. To bridge this gap, we develop SODIUM-Agent, a multi-agent system composed of a web explorer and a cache manager. Powered by our proposed ATP-BFS algorithm and optimized through principled management of cached sources and navigation paths, SODIUM-Agent conducts deep and comprehensive web exploration and performs structurally coherent information extraction. SODIUM-Agent achieves 91.1% accuracy on SODIUM-Bench, outperforming the strongest baseline by approximately 2 times and the weakest by up to 73 times.
Current browse context:
cs.DB
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
