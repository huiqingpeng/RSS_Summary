---
title: "Learning Response-Statistic Shifts and Parametric Roll Episodes from Wave--Vessel Time Series via LSTM Functional Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24431"
published: "2026-03-27"
fetched: "2026-03-28T07:09:41.975537"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Learning Response-Statistic Shifts and Parametric Roll Episodes from Wave--Vessel Time Series via LSTM Functional Models
View PDF HTML (experimental)Abstract:Parametric roll is a rare but high-consequence instability that can trigger abrupt regime changes in ship response, including pronounced shifts in roll statistics and tail risk. This paper develops a data-driven surrogate that learns the nonlinear, causal functional mapping from incident wave--motion time series to vessel motions, and demonstrates that the surrogate reproduces both (i) parametric roll episodes and (ii) the associated statistical shifts in the response. Crucially, the learning framework is data-source agnostic: the paired wave--motion time series can be obtained from controlled experiments (e.g., towing-tank or basin tests with wave probes and motion tracking) when a hull exists, or from high-fidelity simulations during design when experiments are not yet available. To provide a controlled severe-sea demonstration, we generate training data with a URANS numerical wave tank, using long-crested irregular seas synthesized from a modified Pierson--Moskowitz spectrum. The demonstration dataset comprises 49 random-phase realizations for each of three sea states, simulated at a fixed forward speed selected to yield encounter conditions under which parametric-roll episodes can occur. A stacked LSTM surrogate is trained on wave-elevation time series and evaluated on held-out realizations using time-domain accuracy and distributional fidelity metrics. In the most severe case, the model tracks the onset and growth of large-amplitude roll consistent with parametric excitation, and captures the corresponding changes in roll probability density functions (PDFs). We further compare loss-function choices (MSE, relative-entropy-based objectives, and amplitude-weighted variants) and show how they trade average error for improved tail fidelity relevant to operability and risk assessment.
Submission history
From: Jose Del Aguila Ferrandis Dr [view email][v1] Wed, 25 Mar 2026 15:38:26 UTC (3,676 KB)
Current browse context:
cs.LG
Change to browse by:
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
