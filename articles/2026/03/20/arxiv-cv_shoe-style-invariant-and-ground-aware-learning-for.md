---
title: "Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.22184"
published: "2026-03-20"
fetched: "2026-03-20T16:15:20.574635"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 27 Nov 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation
View PDF HTML (experimental)Abstract:Foot contact plays a critical role in human interaction with the world, and thus exploring foot contact can advance our understanding of human movement and physical interaction. Despite its importance, existing methods often approximate foot contact using a zero-velocity constraint and focus on joint-level contact, failing to capture the detailed interaction between the foot and the world. Dense estimation of foot contact is crucial for accurately modeling this interaction, yet predicting dense foot contact from a single RGB image remains largely underexplored. There are two main challenges for learning dense foot contact estimation. First, shoes exhibit highly diverse appearances, making it difficult for models to generalize across different styles. Second, ground often has a monotonous appearance, making it difficult to extract informative features. To tackle these issues, we present a FEet COntact estimation (FECO) framework that learns dense foot contact with shoe style-invariant and ground-aware learning. To overcome the challenge of shoe appearance diversity, our approach incorporates shoe style adversarial training that enforces shoe style-invariant features for contact estimation. To effectively utilize ground information, we introduce a ground feature extractor that captures ground properties based on spatial context. As a result, our proposed method achieves robust foot contact estimation regardless of shoe appearance and effectively leverages ground information. The codes are available at this https URL.
Submission history
From: Daniel Jung [view email][v1] Thu, 27 Nov 2025 07:50:47 UTC (2,486 KB)
[v2] Thu, 19 Mar 2026 04:49:19 UTC (2,487 KB)
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
