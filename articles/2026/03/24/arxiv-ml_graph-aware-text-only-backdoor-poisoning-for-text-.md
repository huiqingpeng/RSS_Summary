---
title: "Graph-Aware Text-Only Backdoor Poisoning for Text-Attributed Graphs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20339"
published: "2026-03-24"
fetched: "2026-03-25T07:08:00.486668"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Graph-Aware Text-Only Backdoor Poisoning for Text-Attributed Graphs
View PDF HTML (experimental)Abstract:Many learning systems now use graph data in which each node also contains text, such as papers with abstracts or users with posts. Because these texts often come from open platforms, an attacker may be able to quietly poison a small part of the training data and later make the model produce wrong predictions on demand. This paper studies that risk in a realistic setting where the attacker edits only node text and does not change the graph structure. We propose TAGBD, a text-only backdoor attack for text-attributed graphs. TAGBD first finds training nodes that are easier to influence, then generates natural-looking trigger text with the help of a shadow graph model, and finally injects the trigger by either replacing the original text or appending a short phrase. Experiments on three benchmark datasets show that the attack is highly effective, transfers across different graph models, and remains strong under common defenses. These results demonstrate that text alone is a practical attack channel in graph learning systems and suggest that future defenses should inspect both graph links and node content.
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
