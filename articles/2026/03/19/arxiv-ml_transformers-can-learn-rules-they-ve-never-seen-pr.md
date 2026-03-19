---
title: "Transformers Can Learn Rules They've Never Seen: Proof of Computation Beyond Interpolation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17019"
published: "2026-03-19"
fetched: "2026-03-19T12:06:30.934811"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Transformers Can Learn Rules They've Never Seen: Proof of Computation Beyond Interpolation
View PDF HTML (experimental)Abstract:A central question in the LLM debate is whether transformers can infer rules absent from training, or whether apparent generalisation reduces to similarity-based interpolation over observed examples. We test a strong interpolation-only hypothesis in two controlled settings: one where interpolation is ruled out by construction and proof, and one where success requires emitting intermediate symbolic derivations rather than only final answers. In Experiment 1, we use a cellular automaton with a pure XOR transition rule and remove specific local input patterns from training; since XOR is linearly inseparable, each held-out pattern's nearest neighbours have the opposite label, so similarity-based predictors fail on the held-out region. Yet a two-layer transformer recovers the rule (best 100%; 47/60 converged runs), and circuit extraction identifies XOR computation. Performance depends on multi-step constraint propagation: without unrolling, accuracy matches output bias (63.1%), while soft unrolling reaches 96.7%. In Experiment 2, we study symbolic operator chains over integers with one operator pair held out; the model must emit intermediate steps and a final answer in a proof-like format. Across all 49 holdout pairs, the transformer exceeds every interpolation baseline (mean 41.8%, up to 78.6%; mean KRR 4.3%; KNN and MLP score 0% on every pair), while removing intermediate-step supervision degrades performance. Together with a construction showing that a standard transformer block can implement exact local Boolean rules, these results provide an existence proof that transformers can learn rule structure not directly observed in training and express it explicitly, ruling out the strongest architectural form of interpolation-only accounts: that transformers cannot in principle discover and communicate unseen rules, while leaving open when such behaviour arises in large-scale language training.
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
