---
title: "Training-Only Heterogeneous Image-Patch-Text Graph Supervision for Advancing Few-Shot Learning Adapters"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18101"
published: "2026-03-20"
fetched: "2026-03-20T13:08:39.979682"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Training-Only Heterogeneous Image-Patch-Text Graph Supervision for Advancing Few-Shot Learning Adapters
View PDF HTML (experimental)Abstract:Recent adapter-based CLIP tuning (e.g., Tip-Adapter) is a strong few-shot learner, achieving efficiency by caching support features for fast prototype matching. However, these methods rely on global uni-modal feature vectors, overlooking fine-grained patch relations and their structural alignment with class text. To bridge this gap without incurring inference costs, we introduce a novel asymmetric training-only framework. Instead of altering the lightweight adapter, we construct a high-capacity auxiliary Heterogeneous Graph Teacher that operates solely during training. This teacher (i) integrates multi-scale visual patches and text prompts into a unified graph, (ii) performs deep cross-modal reasoning via a Modality-aware Graph Transformer (MGT), and (iii) applies discriminative node filtering to extract high-fidelity class features. Crucially, we employ a cache-aware dual-objective strategy to supervise this relational knowledge directly into the Tip-Adapter's key-value cache, effectively upgrading the prototypes while the graph teacher is discarded at test time. Thus, inference remains identical to Tip-Adapter with zero extra latency or memory. Across standard 1-16-shot benchmarks, our method consistently establishes a new state-of-the-art. Ablations confirm that the auxiliary graph supervision, text-guided reasoning, and node filtering are the essential ingredients for robust few-shot adaptation. Code is available at this https URL.
Submission history
From: Mohammed Rahman Sherif Khan Mohammad [view email][v1] Wed, 18 Mar 2026 12:03:23 UTC (21,486 KB)
Current browse context:
cs.CV
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
