---
title: "Few-Shot Left Atrial Wall Segmentation in 3D LGE MRI via Meta-Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24985"
published: "2026-03-27"
fetched: "2026-03-28T07:19:23.836575"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:Few-Shot Left Atrial Wall Segmentation in 3D LGE MRI via Meta-Learning
View PDFAbstract:Segmenting the left atrial wall from late gadolinium enhancement magnetic resonance images (MRI) is challenging due to the wall's thin geometry, low contrast, and the scarcity of expert annotations. We propose a Model-Agnostic Meta-Learning (MAML) framework for K-shot (K = 5, 10, 20) 3D left atrial wall segmentation that is meta-trained on the wall task together with auxiliary left atrial and right atrial cavity tasks and uses a boundary-aware composite loss to emphasize thin-structure accuracy. We evaluated MAML segmentation performance on a hold-out test set and assessed robustness under an unseen synthetic shift and on a distinct local cohort. On the hold-out test set, MAML appeared to improve segmentation performance compared to the supervised fine-tuning model, achieving a Dice score (DSC) of 0.64 vs. 0.52 and HD95 of 5.70 vs. 7.60 mm at 5-shot, and approached the fully supervised reference at 20-shot (0.69 vs. 0.71 DSC). Under unseen shift, performance degraded but remained robust: at 5-shot, MAML attained 0.59 DSC and 5.99 mm HD95 on the unseen domain shift and 0.57 DSC and 6.01 mm HD95 on the local cohort, with consistent gains as K increased. These results suggest that more accurate and reliable thin-wall boundaries are achievable in low-shot adaptation, potentially enabling clinical translation with minimal additional labeling for the assessment of atrial remodeling.
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
