---
title: "Efficient Exploration at Scale"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17378"
published: "2026-03-19"
fetched: "2026-03-19T12:10:34.872630"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Efficient Exploration at Scale
View PDF HTML (experimental)Abstract:We develop an online learning algorithm that dramatically improves the data efficiency of reinforcement learning from human feedback (RLHF). Our algorithm incrementally updates reward and language models as choice data is received. The reward model is fit to the choice data, while the language model is updated by a variation of reinforce, with reinforcement signals provided by the reward model. Several features enable the efficiency gains: a small affirmative nudge added to each reinforcement signal, an epistemic neural network that models reward uncertainty, and information-directed exploration. With Gemma large language models (LLMs), our algorithm matches the performance of offline RLHF trained on 200K labels using fewer than 20K labels, representing more than a 10x gain in data efficiency. Extrapolating from our results, we expect our algorithm trained on 1M labels to match offline RLHF trained on 1B labels. This represents a 1,000x gain. To our knowledge, these are the first results to demonstrate that such large improvements are possible.
Submission history
From: Vikranth Dwaracherla [view email][v1] Wed, 18 Mar 2026 05:47:59 UTC (919 KB)
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
