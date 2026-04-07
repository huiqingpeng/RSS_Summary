---
title: "Mestra: Exploring Migration on Virtualized CGRAs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04694"
published: "2026-04-07"
fetched: "2026-04-08T07:02:21.022709"
---

Computer Science > Hardware Architecture
[Submitted on 6 Apr 2026]
Title:Mestra: Exploring Migration on Virtualized CGRAs
View PDF HTML (experimental)Abstract:As modern Coarse Grain Reconfigurable Arrays (CGRAs) grow in size, efficient utilization of the available fabric by a single application becomes increasingly difficult. Existing CGRA mappers either fail to utilize the available fabric or rely on rigid static code transformations with limited adaptability. Multi-tenant CGRAs have emerged as a promising solution to increase hardware utilization, but current attempts fail to address key challenges such as fabric fragmentation and live migration. To address this gap, we present Mestra, an end-to-end system for CGRA multi-tenancy that supports dynamic scheduling and resource allocation in a shared environment. Mestra addresses fabric fragmentation caused by kernels completing out of order by supporting both stateless and stateful live kernel migration as a de-fragmentation mechanism. We assess our solution on an Alveo-U280 data-center-grade FPGA card, reporting area, frequency, and power. Performance is evaluated using routines from the PolyBench benchmark suite and kernels derived from common machine learning operators. Results show that spatial sharing of the available fabric across multiple users improves workload makespan by up to 70.48%, while live kernel migration reduces tail latency on fragmented layouts by up to 29.60%. The custom tightly coupled controller and read-back paths required for virtualization and stateful migration introduce a LUT cost of 0.13% per region. Our evaluation reveals that multi-tenancy is important for efficient CGRA utilization, and live kernel migration can further improve performance by recovering fragmented space with minimal hardware cost.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
