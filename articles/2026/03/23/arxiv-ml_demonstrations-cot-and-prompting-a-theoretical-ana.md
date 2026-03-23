---
title: "Demonstrations, CoT, and Prompting: A Theoretical Analysis of ICL"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19611"
published: "2026-03-23"
fetched: "2026-03-24T07:19:53.593493"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Demonstrations, CoT, and Prompting: A Theoretical Analysis of ICL
View PDF HTML (experimental)Abstract:In-Context Learning (ICL) enables pretrained LLMs to adapt to downstream tasks by conditioning on a small set of input-output demonstrations, without any parameter updates. Although there have been many theoretical efforts to explain how ICL works, most either rely on strong architectural or data assumptions, or fail to capture the impact of key practical factors such as demonstration selection, Chain-of-Thought (CoT) prompting, the number of demonstrations, and prompt templates. We address this gap by establishing a theoretical analysis of ICL under mild assumptions that links these design choices to generalization behavior. We derive an upper bound on the ICL test loss, showing that performance is governed by (i) the quality of selected demonstrations, quantified by Lipschitz constants of the ICL loss along paths connecting test prompts to pretraining samples, (ii) an intrinsic ICL capability of the pretrained model, and (iii) the degree of distribution shift. Within the same framework, we analyze CoT prompting as inducing a task decomposition and show that it is beneficial when demonstrations are well chosen at each substep and the resulting subtasks are easier to learn. Finally, we characterize how ICL performance sensitivity to prompt templates varies with the number of demonstrations. Together, our study shows that pretraining equips the model with the ability to generalize beyond observed tasks, while CoT enables the model to compose simpler subtasks into more complex ones, and demonstrations and instructions enable it to retrieve similar or complex tasks, including those that can be composed into more complex ones, jointly supporting generalization to unseen tasks. All theoretical insights are corroborated by experiments.
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
