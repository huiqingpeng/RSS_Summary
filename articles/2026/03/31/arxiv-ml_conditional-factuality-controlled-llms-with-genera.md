---
title: "Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27403"
published: "2026-03-31"
fetched: "2026-04-01T07:23:34.285487"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling
View PDF HTML (experimental)Abstract:Large language models (LLMs) need reliable test-time control of hallucinations. Existing conformal methods for LLMs typically provide only \emph{marginal} guarantees and rely on a single global threshold, which can under-cover hard prompts, over-cover easy ones, and produce oversized prediction sets. We propose \emph{Conditional Factuality Control} (CFC), a post-hoc conformal framework that returns \emph{set-valued} outputs with \emph{conditional} coverage guarantees. CFC defines a continuous, feature-conditional acceptance threshold through augmented quantile regression on a latent ``success'' score, and deploys it through a fixed-point threshold rule at inference time. Theoretically, we show that CFC satisfies a conditional coverage guarantee under exchangeability and analyze its \emph{efficiency}, proving that, under mild assumptions on the score distributions, the conditional rule is strictly more sample-efficient than marginal conformal prediction at the same target coverage. We further derive a PAC-style variant, CFC-PAC, which shrinks the nominal risk level based on a stability bound, yielding a finite-sample certificate that the conditional miscoverage deviates from the target by at most $O(\sqrt{\log(1/\delta)/N})$. Empirically, on synthetic data, real-world reasoning and QA benchmarks, and a Flickr8k VLM setting, CFC and CFC-PAC consistently attain near-target coverage across difficulty groups while using smaller prediction sets than CP and non-CP baselines.
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
