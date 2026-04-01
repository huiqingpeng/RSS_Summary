---
title: "Generative Logic: A New Computer Architecture for Deterministic Reasoning and Knowledge Generation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2508.00017"
published: "2026-04-01"
fetched: "2026-04-02T07:12:13.957777"
---

Computer Science > Logic in Computer Science
[Submitted on 25 Jul 2025 (v1), last revised 31 Mar 2026 (this version, v4)]
Title:Generative Logic: A New Computer Architecture for Deterministic Reasoning and Knowledge Generation
View PDF HTML (experimental)Abstract:We present Generative Logic (GL), a deterministic architecture that starts from
user-supplied axiomatic definitions written in a minimalist Mathematical Programming
Language (MPL) and systematically explores a configurable region of their deductive
neighborhood. Definitions are compiled into a distributed grid of Logic Blocks (LBs)
that communicate via a unified hash-based inference engine; whenever the premises of
a rule unify, a new fact is emitted with full provenance, yielding replayable,
auditable proof graphs. The pipeline includes an Incubator that auto-generates
ground-level fact tables, a Compressor that eliminates post-proof redundancy, and an
independent external Verifier (34,320 checks, zero failures). Experimental validation
on Elementary Number Theory develops Peano arithmetic from axioms and autonomously
derives Gauss's summation formula. On commodity hardware, the core proving pipeline
completes in under one minute; the full run including Incubator fact generation
finishes in approximately ten minutes. The Incubator output further reveals that GL
can perform concrete numerical calculations -- each result a proved theorem with full
provenance -- opening a path toward a full-provenance Computer Algebra System (CAS).
Generated proofs export as navigable HTML for independent inspection. Code, proof
graphs, and reproduction instructions are available at this http URL
(commit 6e5b9a4) and archived at doi:https://doi.org/10.5281/zenodo.17206386.
Submission history
From: Nikolai Sergeev [view email][v1] Fri, 25 Jul 2025 17:29:19 UTC (234 KB)
[v2] Fri, 26 Sep 2025 11:33:45 UTC (216 KB)
[v3] Mon, 23 Feb 2026 14:37:20 UTC (254 KB)
[v4] Tue, 31 Mar 2026 14:11:56 UTC (324 KB)
Current browse context:
cs.LO
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
