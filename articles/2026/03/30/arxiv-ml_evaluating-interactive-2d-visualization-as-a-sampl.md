---
title: "Evaluating Interactive 2D Visualization as a Sample Selection Strategy for Biomedical Time-Series Data Annotation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26592"
published: "2026-03-30"
fetched: "2026-03-31T07:25:34.505128"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Evaluating Interactive 2D Visualization as a Sample Selection Strategy for Biomedical Time-Series Data Annotation
View PDF HTML (experimental)Abstract:Reliable machine-learning models in biomedical settings depend on accurate labels, yet annotating biomedical time-series data remains challenging. Algorithmic sample selection may support annotation, but evidence from studies involving real human annotators is scarce. Consequently, we compare three sample selection methods for annotation: random sampling (RND), farthest-first traversal (FAFT), and a graphical user interface-based method enabling exploration of complementary 2D visualizations (2DVs) of high-dimensional data. We evaluated the methods across four classification tasks in infant motility assessment (IMA) and speech emotion recognition (SER). Twelve annotators, categorized as experts or non-experts, performed data annotation under a limited annotation budget, and post-annotation experiments were conducted to evaluate the sampling methods. Across all classification tasks, 2DV performed best when aggregating labels across annotators. In IMA, 2DV most effectively captured rare classes, but also exhibited greater annotator-to-annotator label distribution variability resulting from the limited annotation budget, decreasing classification performance when models were trained on individual annotators' labels; in these cases, FAFT excelled. For SER, 2DV outperformed the other methods among expert annotators and matched their performance for non-experts in the individual-annotator setting. A failure risk analysis revealed that RND was the safest choice when annotator count or annotator expertise was uncertain, whereas 2DV had the highest risk due to its greater label distribution variability. Furthermore, post-experiment interviews indicated that 2DV made the annotation task more interesting and enjoyable. Overall, 2DV-based sampling appears promising for biomedical time-series data annotation, particularly when the annotation budget is not highly constrained.
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
