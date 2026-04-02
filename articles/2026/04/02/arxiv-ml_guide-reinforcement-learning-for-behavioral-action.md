---
title: "GUIDE: Reinforcement Learning for Behavioral Action Support in Type 1 Diabetes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00385"
published: "2026-04-02"
fetched: "2026-04-03T07:20:52.997913"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:GUIDE: Reinforcement Learning for Behavioral Action Support in Type 1 Diabetes
View PDF HTML (experimental)Abstract:Type 1 Diabetes (T1D) management requires continuous adjustment of insulin and lifestyle behaviors to maintain blood glucose within a safe target range. Although automated insulin delivery (AID) systems have improved glycemic outcomes, many patients still fail to achieve recommended clinical targets, warranting new approaches to improve glucose control in patients with T1D. While reinforcement learning (RL) has been utilized as a promising approach, current RL-based methods focus primarily on insulin-only treatment and do not provide behavioral recommendations for glucose control. To address this gap, we propose GUIDE, an RL-based decision-support framework designed to complement AID technologies by providing behavioral recommendations to prevent abnormal glucose events. GUIDE generates structured actions defined by intervention type, magnitude, and timing, including bolus insulin administration and carbohydrate intake events. GUIDE integrates a patient-specific glucose level predictor trained on real-world continuous glucose monitoring data and supports both offline and online RL algorithms within a unified environment. We evaluate both off-policy and on-policy methods across 25 individuals with T1D using standardized glycemic metrics. Among the evaluated approaches, the CQL-BC algorithm demonstrates the highest average time-in-range, reaching 85.49% while maintaining low hypoglycemia exposures. Behavioral similarity analysis further indicates that the learned CQL-BC policy preserves key structural characteristics of patient action patterns, achieving a mean cosine similarity of 0.87 $\pm$ 0.09 across subjects. These findings suggest that conservative offline RL with a structured behavioral action space can provide clinically meaningful and behaviorally plausible decision support for personalized diabetes management.
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
