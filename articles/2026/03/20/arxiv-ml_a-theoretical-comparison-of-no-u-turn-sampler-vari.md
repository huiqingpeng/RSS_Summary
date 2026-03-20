---
title: "A Theoretical Comparison of No-U-Turn Sampler Variants: Necessary and Su?cient Convergence Conditions and Mixing Time Analysis under Gaussian Targets"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18640"
published: "2026-03-20"
fetched: "2026-03-20T13:15:27.478079"
---

Statistics > Machine Learning
[Submitted on 19 Mar 2026]
Title:A Theoretical Comparison of No-U-Turn Sampler Variants: Necessary and Su?cient Convergence Conditions and Mixing Time Analysis under Gaussian Targets
View PDFAbstract:The No-U-Turn Sampler (NUTS) is the computational workhorse of modern Bayesian software libraries, yet its qualitative and quantitative convergence guarantees were established only recently. A significant gap remains in the theoretical comparison of its two main variants: NUTS-mul and NUTS-BPS, which use multinomial sampling and biased progressive sampling, respectively, for index selection. In this paper, we address this gap in three contributions. First, we derive the first necessary conditions for geometric ergodicity for both variants. Second, we establish the first sufficient conditions for geometric ergodicity and ergodicity for NUTS-mul. Third, we obtain the first mixing time result for NUTS-BPS on a standard Gaussian distribution. Our results show that NUTS-mul and NUTS-BPS exhibit nearly identical qualitative behavior, with geometric ergodicity depending on the tail properties of the target distribution. However, they differ quantitatively in their convergence rates. More precisely, when initialized in the typical set of the canonical Gaussian measure, the mixing times of both NUTS-mul and NUTS-BPS scale as $O(d^{1/4})$ up to logarithmic factors, where $d$ denotes the dimension. Nevertheless, the associated constants are strictly smaller for NUTS-BPS.
Current browse context:
stat.ML
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
