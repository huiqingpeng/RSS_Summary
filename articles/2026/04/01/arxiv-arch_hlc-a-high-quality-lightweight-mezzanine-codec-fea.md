---
title: "HLC: A High-Quality Lightweight Mezzanine Codec Featuring High-Throughput Palette"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29864"
published: "2026-04-01"
fetched: "2026-04-02T07:11:05.752953"
---

Computer Science > Hardware Architecture
[Submitted on 31 Mar 2026]
Title:HLC: A High-Quality Lightweight Mezzanine Codec Featuring High-Throughput Palette
View PDF HTML (experimental)Abstract:Existing mezzanine image codecs lack specialized screen content coding tools and therefore struggle to maintain high image quality under bandwidth constraints, especially in areas with dense text. Although distribution codecs offer advanced screen content compression techniques, their high computational complexity makes them impractical for mezzanine coding. To address this shortfall, we introduce the High-quality Lightweight Codec (HLC), a solution centered on enabling practical, high-throughput palette for mezzanine coding. The core innovation is a novel data-dependency-free palette that eliminates the throughput bottlenecks. To ensure its effectiveness across all content, a co-designed rate-distortion optimization module arbitrates between the palette and traditional prediction modes, while a data reuse strategy between rate estimation and entropy coding minimizes the overall hardware resources required for the system. Experimental results show that, compared with a 4K@120fps JPEG-XS encoder, HLC achieves the same throughput while using only half the LUT resources and delivers BD-PSNR improvements of 3.461dB, 3.299dB, and 5.312dB on gaming, natural, and text content datasets, respectively.
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
