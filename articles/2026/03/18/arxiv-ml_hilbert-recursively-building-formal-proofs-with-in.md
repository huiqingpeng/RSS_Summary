---
title: "Hilbert: Recursively Building Formal Proofs with Informal Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22819"
published: "2026-03-18"
fetched: "2026-03-18T17:11:42.142583"
---

Computer Science > Artificial Intelligence
[Submitted on 26 Sep 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Hilbert: Recursively Building Formal Proofs with Informal Reasoning
View PDFAbstract:Large Language Models (LLMs) demonstrate impressive mathematical reasoning abilities, but their solutions frequently contain errors that cannot be automatically checked. Formal theorem proving systems such as Lean 4 offer automated verification with complete accuracy, motivating recent efforts to build specialized prover LLMs that generate verifiable proofs in formal languages. However, a significant gap remains: current prover LLMs solve substantially fewer problems than general-purpose LLMs operating in natural language. We introduce Hilbert, an agentic framework that bridges this gap by combining the complementary strengths of informal reasoning and formal verification. Our system orchestrates four components: an informal LLM that excels at mathematical reasoning, a specialized prover LLM optimized for Lean 4 tactics, a formal verifier, and a semantic theorem retriever. Given a problem that the prover is unable to solve, Hilbert employs recursive decomposition to split the problem into subgoals that it solves with the prover or reasoner LLM. It leverages verifier feedback to refine incorrect proofs as necessary. Experimental results demonstrate that Hilbert substantially outperforms existing approaches on key benchmarks, achieving 99.2\% on miniF2F, 6.6\% points above the best publicly available method. Hilbert achieves the \textbf{strongest known result} from a publicly available model on PutnamBench. It solves 462/660 problems (70.0\%), outperforming proprietary approaches like SeedProver (50.4\%) and achieving a 422\% improvement over the best publicly available baseline. Thus, Hilbert effectively narrows the gap between informal reasoning and formal proof generation. Code is available at this https URL.
Submission history
From: Sumanth Varambally [view email][v1] Fri, 26 Sep 2025 18:24:23 UTC (2,581 KB)
[v2] Mon, 16 Mar 2026 22:30:22 UTC (2,733 KB)
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
