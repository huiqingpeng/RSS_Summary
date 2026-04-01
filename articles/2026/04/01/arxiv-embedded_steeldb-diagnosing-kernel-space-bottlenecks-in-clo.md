---
title: "SteelDB: Diagnosing Kernel-Space Bottlenecks in Cloud OLTP Databases"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.29052"
published: "2026-04-01"
fetched: "2026-04-02T07:10:41.067854"
---

Computer Science > Databases
[Submitted on 30 Mar 2026]
Title:SteelDB: Diagnosing Kernel-Space Bottlenecks in Cloud OLTP Databases
View PDF HTML (experimental)Abstract:Modern cloud OLTP databases have sought performance primarily through user-space optimization - separating storage and compute layers, or distributing transactions across multiple nodes using consensus algorithms. This paper turns attention to a previously unexplored layer: kernel-space I/O behavior. From an on-premises perspective, where a single server with local storage delivers excellent performance, these elaborate designs seem puzzling. Why do cloud databases require such architectural complexity? We investigate this through a pathological analysis of databases that rely on OS-level I/O control in cloud-specific storage environments. We show that bottlenecks widely attributed to network or storage architectures in fact originate in kernel-space I/O behavior. Based on this diagnosis, we derive treatment principles and realize them as SteelDB, a zero-patch architecture that improves database performance on general-purpose cloud distributed block storage through strategic I/O optimization without requiring kernel or database patches. TPC-C evaluations demonstrate that SteelDB achieves up to 9x performance improvement at no additional cost. Against Amazon Aurora, SteelDB achieved 3.1x higher performance while reducing costs by 58%, leading to a 7.3x improvement in cost efficiency. While Aurora requires an average of 254 days for major version upgrades due to applying proprietary patches to newly released OSS databases, our zero-patch architecture reduces these software maintenance costs to near zero.
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
