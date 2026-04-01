---
title: "A Neural Tension Operator for Curve Subdivision across Constant Curvature Geometries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28937"
published: "2026-04-01"
fetched: "2026-04-02T07:13:20.575357"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:A Neural Tension Operator for Curve Subdivision across Constant Curvature Geometries
View PDF HTML (experimental)Abstract:Interpolatory subdivision schemes generate smooth curves from piecewise-linear control polygons by repeatedly inserting new vertices. Classical schemes rely on a single global tension parameter and typically require separate formulations in Euclidean, spherical, and hyperbolic geometries. We introduce a shared learned tension predictor that replaces the global parameter with per-edge insertion angles predicted by a single 140K-parameter network. The network takes local intrinsic features and a trainable geometry embedding as input, and the predicted angles drive geometry-specific insertion operators across all three spaces without architectural modification. A constrained sigmoid output head enforces a structural safety bound, guaranteeing that every inserted vertex lies within a valid angular range for any finite weight configuration. Three theoretical results accompany the method: a structural guarantee of tangent-safe insertions; a heuristic motivation for per-edge adaptivity; and a conditional convergence certificate for continuously differentiable limit curves, subject to an explicit Lipschitz constraint verified post hoc. On 240 held-out validation curves, the learned predictor occupies a distinct position on the fidelity--smoothness Pareto frontier, achieving markedly lower bending energy and angular roughness than all fixed-tension and manifold-lift baselines. Riemannian manifold lifts retain a pointwise-fidelity advantage, which this study quantifies directly. On the out-of-distribution ISS orbital ground-track example, bending energy falls by 41% and angular roughness by 68% with only a modest increase in Hausdorff distance, suggesting that the predictor generalises beyond its synthetic training distribution.
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
