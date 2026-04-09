---
title: "Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06767"
published: "2026-04-09"
fetched: "2026-04-10T07:05:06.897196"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models
View PDF HTML (experimental)Abstract:Language models operate on discrete tokens but compute in continuous vector spaces, inducing a Voronoi tessellation over the representation manifold. We study this tessellation empirically on Qwen3.5-4B-Base, making two contributions. First, using float32 margin recomputation to resolve bfloat16 quantization artifacts, we validate Mabrok's (2026) linear scaling law of the expressibility gap with $R^2$ = 0.9997 - the strongest confirmation to date - and identify a mid-layer geometric ambiguity regime where margin geometry is anti-correlated with cross-entropy (layers 24-28, $\rho$ = -0.29) before crystallizing into alignment at the final layer ($\rho$ = 0.836).
Second, we show that the Voronoi tessellation of a converged model is reshapable through margin refinement procedures (MRP): short post-hoc optimization runs that widen token-decision margins without retraining. We compare direct margin maximization against Fisher information distance maximization across a dose-response sweep. Both methods find the same ceiling of ~16,300 correctable positions per 256K evaluated, but differ critically in collateral damage. Margin maximization damage escalates with intervention strength until corrections are overwhelmed. Fisher damage remains constant at ~5,300 positions across the validated range ($\lambda$ = 0.15-0.6), achieving +28% median margin improvement at $\lambda$ = 0.6 with invariant downstream benchmarks - a geometric reorganization that compresses the expressibility gap while preserving its scaling law. However, frequency and token-class audits reveal that gains concentrate in high-frequency structural tokens (84% of net corrections at $\lambda$ = 0.6), with content and entity-like contributions shrinking at higher $\lambda$. Fisher MRP is therefore a viable geometric polishing tool whose practical ceiling is set not by aggregate damage but by the uniformity of token-level benefit.
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
