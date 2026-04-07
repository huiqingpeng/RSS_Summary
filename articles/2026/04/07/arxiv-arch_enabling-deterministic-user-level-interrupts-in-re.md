---
title: "Enabling Deterministic User-Level Interrupts in Real-Time Processors via Hardware Extension"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04015"
published: "2026-04-07"
fetched: "2026-04-08T07:02:24.031442"
---

Computer Science > Cryptography and Security
[Submitted on 5 Apr 2026]
Title:Enabling Deterministic User-Level Interrupts in Real-Time Processors via Hardware Extension
View PDF HTML (experimental)Abstract:The growing complexity of real-time embedded systems demands strong isolation of software components into separate protection domains to reduce attack surfaces and limit fault propagation. However, application-supplied device interrupt handlers -- even untrusted -- have to remain in the kernel to minimize interrupt latency, undermining security and burdening manual certifications. Current hardware extensions accelerate interrupts only when the target protection domain is scheduled by the kernel; consequently, they are limited to improving average-case performance but not worst-case latency, and do not meet the requirements of critical real-time applications such as autonomous vehicles or robots.
To overcome this limitation, we propose a novel hardware extension that enables direct, deterministic switching to the appropriate protection domain upon user-level interrupt arrival -- without kernel intervention -- even when that domain is dormant. Our hardware extension reduces worst-case latency by more than 50x with a 19% increase in core area (2% of total die area) and 4.1% increase in dynamic power. To the best of our knowledge, this is the first integrated mechanism to guarantee user-level interrupt delivery with a nanosecond-scale yet bounded worst-case latency.
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
