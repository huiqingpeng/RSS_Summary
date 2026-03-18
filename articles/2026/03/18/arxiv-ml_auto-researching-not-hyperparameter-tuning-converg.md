---
title: "Auto Researching, not hyperparameter tuning: Convergence Analysis of 10,000 Experiments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15916"
published: "2026-03-18"
fetched: "2026-03-18T15:37:22.396977"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Auto Researching, not hyperparameter tuning: Convergence Analysis of 10,000 Experiments
View PDF HTML (experimental)Abstract:When LLM agents autonomously design ML experiments, do they perform genuine architecture search -- or do they default to hyperparameter tuning within a narrow region of the design space? We answer this question by analyzing 10,469 experiments executed by two LLM agents (Claude Opus and Gemini 2.5 Pro) across a combinatorial configuration space of 108,000 discrete cells for dashcam collision detection over 27 days. Through ANOVA decomposition, we find that \textbf{architectural choices explain 94\% of performance variance} ($F = 1324$, $\eta^2 = 0.94$), while hyperparameter variation within a fixed architecture explains only 6\%. Cross-task validation on a second collision dataset confirms this finding (75\% architecture-explained variance) with a \emph{different} winning backbone, confirming genuine architecture discovery. The agents' key contribution is discovering that V-JEPA\,2 video features with Zipformer temporal encoders achieve 0.9245 AP -- a configuration no human proposed -- and concentrating search on productive architectural regions: at $N = 50$, LLM-guided search reaches AP $= 0.985$ versus $0.965$ for from-scratch random search. Post-bugfix convergence follows a power law ($c = 0.11$, $R^2 = 0.93$); the low exponent reflects the cost of broad exploration, not inefficiency, since the LLM discovers qualitatively better regions than random or Bayesian baselines. We characterize multi-agent search dynamics via entropy cycles and Jensen--Shannon specialization, providing the first large-scale empirical framework for LLM-guided combinatorial ML experiment design.
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
