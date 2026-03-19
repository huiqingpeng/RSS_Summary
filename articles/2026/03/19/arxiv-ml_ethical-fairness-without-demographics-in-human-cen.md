---
title: "Ethical Fairness without Demographics in Human-Centered AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13373"
published: "2026-03-19"
fetched: "2026-03-19T14:19:17.172147"
---

Computer Science > Computers and Society
[Submitted on 10 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Ethical Fairness without Demographics in Human-Centered AI
View PDF HTML (experimental)Abstract:Computational models are increasingly embedded in human-centered domains such as healthcare, education, workplace analytics, and digital well-being, where their predictions directly influence individual outcomes and collective welfare. In such contexts, achieving high accuracy alone is insufficient; models must also act ethically and equitably across diverse populations. However, fair AI approaches that rely on demographic attributes are impractical, as such information is often unavailable, privacy-sensitive, or restricted by regulatory frameworks. Moreover, conventional parity-based fairness approaches, while aiming for equity, can inadvertently violate core ethical principles by trading off subgroup performance or stability. To address this challenge, we present Flare (Fisher-guided LAtent-subgroup learning with do-no-harm REgularization), the first demographic-agnostic framework that aligns algorithmic fairness with ethical principles through the geometry of optimization. Flare leverages Fisher Information to regularize curvature, uncovering latent disparities in model behavior without access to demographic or sensitive attributes. By integrating representation, loss, and curvature signals, it identifies hidden performance strata and adaptively refines them through collaborative but do-no-harm optimization, enhancing each subgroup's performance while preserving global stability and ethical balance. We also introduce BHE (Beneficence-Harm Avoidance-Equity), a novel metric suite that operationalizes ethical fairness evaluation beyond statistical parity. Extensive evaluations across diverse physiological (EDA), behavioral (IHS), and clinical (OhioT1DM) datasets show that Flare consistently enhances ethical fairness compared to state-of-the-art baselines.
Submission history
From: Shaily Roy [view email][v1] Tue, 10 Mar 2026 09:09:07 UTC (9,816 KB)
[v2] Tue, 17 Mar 2026 23:08:24 UTC (13,032 KB)
Current browse context:
cs.CY
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
