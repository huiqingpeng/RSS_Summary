---
title: "Informationally Compressive Anonymization: Non-Degrading Sensitive Input Protection for Privacy-Preserving Supervised Machine Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15842"
published: "2026-03-18"
fetched: "2026-03-18T15:36:00.230266"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Informationally Compressive Anonymization: Non-Degrading Sensitive Input Protection for Privacy-Preserving Supervised Machine Learning
View PDF HTML (experimental)Abstract:Modern machine learning systems increasingly rely on sensitive data, creating significant privacy, security, and regulatory risks that existing privacy-preserving machine learning (ppML) techniques, such as Differential Privacy (DP) and Homomorphic Encryption (HE), address only at the cost of degraded performance, increased complexity, or prohibitive computational overhead. This paper introduces Informationally Compressive Anonymization (ICA) and the VEIL architecture, a privacy-preserving ML framework that achieves strong privacy guarantees through architectural and mathematical design rather than noise injection or cryptography. ICA embeds a supervised, multi-objective encoder within a trusted Source Environment to transform raw inputs into low-dimensional, task-aligned latent representations, ensuring that only irreversibly anonymized vectors are exported to untrusted Training and Inference Environments. The paper rigorously proves that these encodings are structurally non-invertible using topological and information-theoretic arguments, showing that inversion is logically impossible, even under idealized attacker assumptions, and that, in realistic deployments, the attackers conditional entropy over the original data diverges, driving reconstruction probability to zero. Unlike prior autoencoder-based ppML approaches, ICA preserves predictive utility by aligning representation learning with downstream supervised objectives, enabling low-latency, high-performance ML without gradient clipping, noise budgets, or encryption at inference time. The VEIL architecture enforces strict trust boundaries, supports scalable multi-region deployment, and naturally aligns with privacy-by-design regulatory frameworks, establishing a new foundation for enterprise ML that is secure, performant, and safe by construction, even in the face of post-quantum threats.
Submission history
From: Jeremy Samuelson [view email][v1] Mon, 16 Mar 2026 19:17:51 UTC (5,548 KB)
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
