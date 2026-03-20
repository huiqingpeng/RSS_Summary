---
title: "Fork, Explore, Commit: OS Primitives for Agentic Exploration"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2602.08199"
published: "2026-03-20"
fetched: "2026-03-20T12:03:32.315013"
---

Computer Science > Operating Systems
[Submitted on 9 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Fork, Explore, Commit: OS Primitives for Agentic Exploration
View PDF HTML (experimental)Abstract:AI agents increasingly perform agentic exploration: pursuing multiple solution paths in parallel and committing only the successful one. Because each exploration path may modify files and spawn processes, agents require isolated environments with atomic commit and rollback semantics for both filesystem state and process state. We introduce the branch context, a new OS abstraction that provides: (1) copy-on-write state isolation with independent filesystem views and process groups, (2) a structured lifecycle of fork, explore, and commit/abort, (3) first-commit-wins resolution that automatically invalidates sibling branches, and (4) nestable contexts for hierarchical exploration. We realize branch contexts in Linux through two complementary components. First, BranchFS is a FUSE-based filesystem that gives each branch context an isolated copy-on-write workspace, with O(1) creation, atomic commit to the parent, and automatic sibling invalidation, all without root privileges. BranchFS is open sourced in this https URL, along with a Python integration library, BranchContext, that provides ready-to-use agent exploration patterns. Second, branch() is a proposed Linux syscall that spawns processes into branch contexts with reliable termination, kernel-enforced sibling isolation, and first-commit-wins coordination. Preliminary evaluation of BranchFS shows sub-350 us branch creation independent of base filesystem size, and modification-proportional commit overhead (under 1 ms for small changes).
Submission history
From: Cong Wang [view email][v1] Mon, 9 Feb 2026 01:46:52 UTC (18 KB)
[v2] Thu, 19 Mar 2026 04:38:30 UTC (19 KB)
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
