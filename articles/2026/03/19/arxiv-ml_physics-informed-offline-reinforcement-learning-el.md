---
title: "Physics-informed offline reinforcement learning eliminates catastrophic fuel waste in maritime routing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17319"
published: "2026-03-19"
fetched: "2026-03-19T13:11:17.733817"
---

Computer Science > Artificial Intelligence
[Submitted on 18 Mar 2026]
Title:Physics-informed offline reinforcement learning eliminates catastrophic fuel waste in maritime routing
View PDF HTML (experimental)Abstract:International shipping produces approximately 3% of global greenhouse gas emissions, yet voyage routing remains dominated by heuristic methods. We present PIER (Physics-Informed, Energy-efficient, Risk-aware routing), an offline reinforcement learning framework that learns fuel-efficient, safety-aware routing policies from physics-calibrated environments grounded in historical vessel tracking data and ocean reanalysis products, requiring no online simulator. Validated on one full year (2023) of AIS data across seven Gulf of Mexico routes (840 episodes per method), PIER reduces mean CO2 emissions by 10% relative to great-circle routing. However, PIER's primary contribution is eliminating catastrophic fuel waste: great-circle routing incurs extreme fuel consumption (>1.5x median) in 4.8% of voyages; PIER reduces this to 0.5%, a 9-fold reduction. Per-voyage fuel variance is 3.5x lower (p<0.001), with bootstrap 95% CI for mean savings [2.9%, 15.7%]. Partial validation against observed AIS vessel behavior confirms consistency with the fastest real transits while exhibiting 23.1x lower variance. Crucially, PIER is forecast-independent: unlike A* path optimization whose wave protection degrades 4.5x under realistic forecast uncertainty, PIER maintains constant performance using only local observations. The framework combines physics-informed state construction, demonstration-augmented offline data, and a decoupled post-hoc safety shield, an architecture that transfers to wildfire evacuation, aircraft trajectory optimization, and autonomous navigation in unmapped terrain.
Current browse context:
cs.AI
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
