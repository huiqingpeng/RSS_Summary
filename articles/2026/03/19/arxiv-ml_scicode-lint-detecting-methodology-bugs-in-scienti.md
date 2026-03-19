---
title: "scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17893"
published: "2026-03-19"
fetched: "2026-03-19T13:16:27.620023"
---

Computer Science > Software Engineering
[Submitted on 18 Mar 2026]
Title:scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns
View PDF HTML (experimental)Abstract:Methodology bugs in scientific Python code produce plausible but incorrect results that traditional linters and static analysis tools cannot detect. Several research groups have built ML-specific linters, demonstrating that detection is feasible. Yet these tools share a sustainability problem: dependency on specific pylint or Python versions, limited packaging, and reliance on manual engineering for every new pattern. As AI-generated code increases the volume of scientific software, the need for automated methodology checking (such as detecting data leakage, incorrect cross-validation, and missing random seeds) grows. We present scicode-lint, whose two-tier architecture separates pattern design (frontier models at build time) from execution (small local model at runtime). Patterns are generated, not hand-coded; adapting to new library versions costs tokens, not engineering hours. On Kaggle notebooks with human-labeled ground truth, preprocessing leakage detection reaches 65% precision at 100% recall; on 38 published scientific papers applying AI/ML, precision is 62% (LLM-judged) with substantial variation across pattern categories; on a held-out paper set, precision is 54%. On controlled tests, scicode-lint achieves 97.7% accuracy across 66 patterns.
Current browse context:
cs.SE
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
