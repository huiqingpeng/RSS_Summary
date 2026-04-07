---
title: "SIEVE: Sample-Efficient Parametric Learning from Natural Language"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02339"
published: "2026-04-07"
fetched: "2026-04-08T07:02:30.496470"
---

Computer Science > Machine Learning
[Submitted on 2 Feb 2026]
Title:SIEVE: Sample-Efficient Parametric Learning from Natural Language
View PDF HTML (experimental)Abstract:Natural language context-such as instructions, knowledge, or feedback-contains rich signal for adapting language models. While in-context learning provides adaptation via the prompt, parametric learning persists into model weights and can improve performance further, though is data hungry and heavily relies on either high-quality traces or automated verifiers. We propose SIEVE, a method for sample-efficient parametric learning from natural language context that requires as few as three query examples. SIEVE uses a novel synthetic data generation pipeline, SIEVE-GEN, that leverages the insight that context is decomposable. Decomposing context allows us to generate higher quality rollouts by pairing synthetic queries with only the applicable context rather than the entirety, then using context distillation to internalize context into the model. We evaluate in reasoning settings where context is necessary, including custom domains and the RuleArena and Machine Translation from One Book tasks. Our results show that SIEVE outperforms prior context distillation methods using just three query examples, demonstrating how to achieve sample-efficient parametric learning from natural language.
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
