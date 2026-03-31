---
title: "From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27299"
published: "2026-03-31"
fetched: "2026-04-01T07:22:46.248138"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification
View PDF HTML (experimental)Abstract:The Semantic Router DSL is a non-Turing-complete policy language deployed in production for per-request LLM inference routing: content signals (embedding similarity, PII detection, jailbreak scoring) feed into weighted projections and priority-ordered decision trees that select a model, enforce privacy policies, and produce structured audit traces -- all from a single declarative source file. Prior work established conflict-free compilation for probabilistic predicates and positioned the DSL within the Workload-Router-Pool inference architecture.
This paper extends the same language from stateless, per-request routing to multi-step agent workflows -- the full path from inference gateway to agent orchestration to infrastructure deployment. The DSL compiler emits verified decision nodes for orchestration frameworks (LangGraph, OpenClaw), Kubernetes artifacts (NetworkPolicy, Sandbox CRD, ConfigMap), YANG/NETCONF payloads, and protocol-boundary gates (MCP, A2A) -- all from the same source.
Because the language is non-Turing-complete, the compiler guarantees exhaustive routing, conflict-free branching, referential integrity, and audit traces structurally coupled to the decision logic. Because signal definitions are shared across targets, a threshold change propagates from inference gateway to agent gate to infrastructure artifact in one compilation step -- eliminating cross-team coordination as the primary source of policy drift. We ground the approach in four pillars -- auditability, cost efficiency, verifiability, and tunability -- and identify the verification boundary at each layer.
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
