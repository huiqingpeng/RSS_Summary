---
title: "Federated Learning for Privacy-Preserving Medical AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15901"
published: "2026-03-18"
fetched: "2026-03-18T15:36:55.171165"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Federated Learning for Privacy-Preserving Medical AI
View PDF HTML (experimental)Abstract:This dissertation investigates privacy-preserving federated learning for Alzheimer's disease classification using three-dimensional MRI data from the Alzheimer's Disease Neuroimaging Initiative (ADNI). Existing methodologies often suffer from unrealistic data partitioning, inadequate privacy guarantees, and insufficient benchmarking, limiting their practical deployment in healthcare. To address these gaps, this research proposes a novel site-aware data partitioning strategy that preserves institutional boundaries, reflecting real-world multi-institutional collaborations and data heterogeneity. Furthermore, an Adaptive Local Differential Privacy (ALDP) mechanism is introduced, dynamically adjusting privacy parameters based on training progression and parameter characteristics, thereby significantly improving the privacy-utility trade-off over traditional fixed-noise approaches. Systematic empirical evaluation across multiple client federations and privacy budgets demonstrated that advanced federated optimisation algorithms, particularly FedProx, could equal or surpass centralised training performance while ensuring rigorous privacy protection. Notably, ALDP achieved up to 80.4% accuracy in a two-client configuration, surpassing fixed-noise Local DP by 5-7 percentage points and demonstrating substantially greater training stability. The comprehensive ablation studies and benchmarking establish quantitative standards for privacy-preserving collaborative medical AI, providing practical guidelines for real-world deployment. This work thereby advances the state-of-the-art in federated learning for medical imaging, establishing both methodological foundations and empirical evidence necessary for future privacy-compliant AI adoption in healthcare.
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
