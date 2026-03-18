---
title: "Do Not Leave a Gap: Hallucination-Free Object Concealment in Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15940"
published: "2026-03-18"
fetched: "2026-03-18T18:22:39.718387"
---

Computer Science > Cryptography and Security
[Submitted on 16 Mar 2026]
Title:Do Not Leave a Gap: Hallucination-Free Object Concealment in Vision-Language Models
View PDF HTML (experimental)Abstract:Vision-language models (VLMs) have recently shown remarkable capabilities in visual understanding and generation, but remain vulnerable to adversarial manipulations of visual content. Prior object-hiding attacks primarily rely on suppressing or blocking region-specific representations, often creating semantic gaps that inadvertently induce hallucination, where models invent plausible but incorrect objects. In this work, we demonstrate that hallucination arises not from object absence per se, but from semantic discontinuity introduced by such suppression-based attacks. We propose a new class of \emph{background-consistent object concealment} attacks, which hide target objects by re-encoding their visual representations to be statistically and semantically consistent with surrounding background regions. Crucially, our approach preserves token structure and attention flow, avoiding representational voids that trigger hallucination. We present a pixel-level optimization framework that enforces background-consistent re-encoding across multiple transformer layers while preserving global scene semantics. Extensive experiments on state-of-the-art vision-language models show that our method effectively conceals target objects while preserving up to $86\%$ of non-target objects and reducing grounded hallucination by up to $3\times$ compared to attention-suppression-based attacks.
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
