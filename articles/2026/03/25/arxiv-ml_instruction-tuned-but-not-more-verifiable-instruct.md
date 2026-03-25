---
title: "Instruction-Tuned, but Not More Verifiable Instruction-Following: A Cross-Task Diagnosis for LoRA Adapters"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22379"
published: "2026-03-25"
fetched: "2026-03-26T07:14:04.575062"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Instruction-Tuned, but Not More Verifiable Instruction-Following: A Cross-Task Diagnosis for LoRA Adapters
View PDF HTML (experimental)Abstract:Adapters are often selected and deployed based on nominal labels (e.g., instruction-tuned), which implicitly suggest what capability improves after adaptation. We test whether nominal training objectives reliably align with realized cross-task capability gains by evaluating the same LoRA adapter across tasks. Our strongest evidence is tied to strict, automatically verifiable instruction following as measured by IFEval: across multiple seeds, base models, and LoRA settings, nominal labels recurrently but not universally fail to predict improvements on this verifiable target, with clear configuration sensitivity including a near-zero or negative case. As an illustrative strongest-case example in a controlled instruction-versus-numeric setting, an instruction-tuned adapter substantially improves off-target NM-based numeric benchmark performance from 0.133 to 0.632 while not improving verifiable instruction following on IFEval (ILA: 0.313 to 0.271; PLA: 0.250 to 0.143; values rounded to three decimals). We refer to this nominal-versus-realized mismatch pattern as capability drift as a descriptive label. The mismatch is visible in the raw cross-task performance matrix; we use a drift score only as a compact summary in the same units as the underlying metrics, not as a new formal metric contribution. Evidence from broader instruction-following benchmarks is benchmark-dependent and mixed, reflecting heterogeneity in how instruction following is operationalized; we therefore do not treat cross-benchmark agreement as a premise. Overall, the practical takeaway is to perform routine cross-task evaluation before deployment and to avoid treating nominal labels as reliable capability proxies.
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
