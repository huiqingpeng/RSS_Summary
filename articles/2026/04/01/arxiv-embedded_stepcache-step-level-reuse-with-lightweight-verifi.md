---
title: "StepCache: Step-Level Reuse with Lightweight Verification and Selective Patching for LLM Serving"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.28795"
published: "2026-04-01"
fetched: "2026-04-02T07:10:04.668800"
---

Computer Science > Operating Systems
[Submitted on 24 Mar 2026]
Title:StepCache: Step-Level Reuse with Lightweight Verification and Selective Patching for LLM Serving
View PDF HTML (experimental)Abstract:We address LLM serving workloads where repeated requests share a common solution structure but differ in localized constraints, such as output schema, variable names, or numeric constants. Prior caching approaches typically reuse either full responses (semantic caching) or model-internal KV/prefix states, which are respectively brittle under partial changes or tightly coupled to specific backends. We present StepCache, a backend-agnostic step-level reuse layer that segments outputs into ordered steps, retrieves the best-matching cached request, verifies steps using lightweight task-aware checks, and regenerates only failing regions via selective patching. StepCache additionally supports strict structured-output enforcement for JSON, including single-step extraction, required-key constraints, and one-shot repair, as well as conservative skip-reuse fallbacks for semantic changes. For linear equations, StepCache promotes verification into correction via a bounded repair loop with a deterministic fallback that guarantees correctness when the backend model fails.
In a CPU-only perturbation-heavy micro-benchmark on math and JSON variants, averaged over three seeds, StepCache reduces mean latency from 2.13 s to 0.67 s, median latency from 2.42 s to 0.01 s, and p95 latency from 3.38 s to 3.30 s. It also reduces total token usage from 36.1k to 27.3k and improves end-to-end correctness from 72.5% to 100% under task-specific checks and a stitched-output integrity check. Across requests, 79.7% take the reuse-only fast path, 5.4% require patching, and 14.9% trigger skip-reuse.
Current browse context:
cs.OS
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
