---
title: "Ensembles-based Feature Guided Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19653"
published: "2026-03-23"
fetched: "2026-03-24T07:20:49.004246"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Ensembles-based Feature Guided Analysis
View PDFAbstract:Recent Deep Neural Networks (DNN) applications ask for techniques that can explain their behavior. Existing solutions, such as Feature Guided Analysis (FGA), extract rules on their internal behaviors, e.g., by providing explanations related to neurons activation. Results from the literature show that these rules have considerable precision (i.e., they correctly predict certain classes of features), but the recall (i.e., the number of situations these rule apply) is more limited. To mitigate this problem, this paper presents Ensembles-based Feature Guided Analysis (EFGA). EFGA combines rules extracted by FGA into ensembles. Ensembles aggregate different rules to increase their applicability depending on an aggregation criterion, a policy that dictates how to combine rules into ensembles. Although our solution is extensible, and different aggregation criteria can be developed by users, in this work, we considered three different aggregation criteria. We evaluated how the choice of the criterion influences the effectiveness of EFGA on two benchmarks (i.e., the MNIST and LSC datasets), and found that different aggregation criteria offer alternative trade-offs between precision and recall. We then compare EFGA with FGA. For this experiment, we selected an aggregation criterion that provides a reasonable trade-off between precision and recall. Our results show that EFGA has higher train recall (+28.51% on MNIST, +33.15% on LSC), and test recall (+25.76% on MNIST, +30.81% on LSC) than FGA, with a negligible reduction on the test precision (-0.89% on MNIST, -0.69% on LSC).
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
