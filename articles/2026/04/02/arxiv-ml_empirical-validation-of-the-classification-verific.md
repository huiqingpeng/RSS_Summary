---
title: "Empirical Validation of the Classification-Verification Dichotomy for AI Safety Gates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00072"
published: "2026-04-02"
fetched: "2026-04-03T07:16:49.748617"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Empirical Validation of the Classification-Verification Dichotomy for AI Safety Gates
View PDF HTML (experimental)Abstract:Can classifier-based safety gates maintain reliable oversight as AI systems improve over hundreds of iterations? We provide comprehensive empirical evidence that they cannot. On a self-improving neural controller (d=240), eighteen classifier configurations -- spanning MLPs, SVMs, random forests, k-NN, Bayesian classifiers, and deep networks -- all fail the dual conditions for safe self-improvement. Three safe RL baselines (CPO, Lyapunov, safety shielding) also fail. Results extend to MuJoCo benchmarks (Reacher-v4 d=496, Swimmer-v4 d=1408, HalfCheetah-v4 d=1824). At controlled distribution separations up to delta_s=2.0, all classifiers still fail -- including the NP-optimal test and MLPs with 100% training accuracy -- demonstrating structural impossibility.
We then show the impossibility is specific to classification, not to safe self-improvement itself. A Lipschitz ball verifier achieves zero false accepts across dimensions d in {84, 240, 768, 2688, 5760, 9984, 17408} using provable analytical bounds (unconditional delta=0). Ball chaining enables unbounded parameter-space traversal: on MuJoCo Reacher-v4, 10 chains yield +4.31 reward improvement with delta=0; on Qwen2.5-7B-Instruct during LoRA fine-tuning, 42 chain transitions traverse 234x the single-ball radius with zero safety violations across 200 steps. A 50-prompt oracle confirms oracle-agnosticity. Compositional per-group verification enables radii up to 37x larger than full-network balls. At d<=17408, delta=0 is unconditional; at LLM scale, conditional on estimated Lipschitz constants.
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
