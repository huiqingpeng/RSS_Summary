---
title: "GASP: Guided Asymmetric Self-Play For Coding LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15957"
published: "2026-03-18"
fetched: "2026-03-18T15:38:26.086079"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:GASP: Guided Asymmetric Self-Play For Coding LLMs
View PDF HTML (experimental)Abstract:Asymmetric self-play has emerged as a promising paradigm for post-training large language models, where a teacher continually generates questions for a student to solve at the edge of the student's learnability. Although these methods promise open-ended data generation bootstrapped from no human data, they suffer from one major problem: not all problems that are hard to solve are interesting or informative to improve the overall capabilities of the model. Current asymmetric self-play methods are goal-agnostic with no real grounding. We propose Guided Asymmetric Self-Play (GASP), where grounding is provided by real-data goalpost questions that are identified to pose a hard exploration challenge to the model. During self-play, the teacher first generates an easier variant of a hard question, and then a harder variant of that easier question, with the goal of gradually closing the gap to the goalpost throughout training. Doing so, we improve pass@20 on LiveCodeBench (LCB) by 2.5% over unguided asymmetric self-play, and through the curriculum constructed by the teacher, we manage to solve hard goalpost questions that remain out of reach for all baselines.
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
