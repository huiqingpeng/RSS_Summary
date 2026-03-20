---
title: "HWE-Bench: Can Language Models Perform Board-level Schematic Designs?"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18102"
published: "2026-03-20"
fetched: "2026-03-20T12:03:49.020051"
---

Computer Science > Hardware Architecture
[Submitted on 18 Mar 2026]
Title:HWE-Bench: Can Language Models Perform Board-level Schematic Designs?
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) have demonstrated significant potential in various engineering tasks, including software development, digital logic generation, and companion document maintenance. However, their ability to perform board-level circuit design is understudied, as this task requires a synergized understanding of real-world physics and Integrated Circuit (IC) datasheets, the latter comprising detailed specifications for individual components. To address this challenge, we propose \hweb, an evaluation framework that benchmarks the ability of LLMs to perform such designs. It consists of 300 board-level design tasks pulled from open-source and crowdsourcing platforms such as GitHub and OSHWLab, covering 8 application domains, and is complemented with a knowledge base of 2,914 real IC datasheets. For each task, the LLMs are tasked with generating a schematic from scratch, using the provided circuit functional requirements and a set of component datasheets as input. The resulting schematic will be checked against a static electrical rules, and then passed to a circuit simulator to verify its dynamic behavior. Our evaluation show that although current models achieve initial engineering usability and documentation understanding, they lack physical intuition, as the top-performing model achieved an overall pass rate of 8.15\%. We envision that advancements on \hweb\ will pave the way for the development of practical Electronic Design Automation (EDA) agents, revolutionizing the field of board-level design.
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
