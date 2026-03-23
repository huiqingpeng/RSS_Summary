---
title: "Scale-Dependent Radial Geometry and Metric Mismatch in Wasserstein Propagation for Reverse Diffusion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19670"
published: "2026-03-23"
fetched: "2026-03-24T07:21:03.801893"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Scale-Dependent Radial Geometry and Metric Mismatch in Wasserstein Propagation for Reverse Diffusion
View PDF HTML (experimental)Abstract:Existing analyses of reverse diffusion often propagate sampling error in the Euclidean geometry underlying \(\Wtwo\) along the entire reverse trajectory. Under weak log-concavity, however, Gaussian smoothing can create contraction first at large separations while short separations remain non-dissipative. The first usable contraction is therefore radial rather than Euclidean, creating a metric mismatch between the geometry that contracts early and the geometry in which the terminal error is measured. We formalize this mismatch through an explicit radial lower profile for the learned reverse drift. Its far-field limit gives a contraction reserve, its near-field limit gives the Euclidean load governing direct \(\Wtwo\) propagation, and admissible switch times are characterized by positivity of the reserve on the remaining smoothing window. We exploit this structure with a one-switch routing argument. Before the switch, reflection coupling yields contraction in a concave transport metric adapted to the radial profile. At the switch, we convert once from this metric back to \(\Wtwo\) under a \(p\)-moment budget, and then propagate the converted discrepancy over the remaining short window in Euclidean geometry. For discretizations of the learned reverse SDE under \(L^2\) score-error control, a one-sided Lipschitz condition of score error, and standard well-posedness and coupling hypotheses, we obtain explicit non-asymptotic end-to-end \(\Wtwo\) guarantees, a scalar switch-selection objective, and a sharp structural limit on the conversion exponent within the affine-tail concave class.
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
