---
title: "FVRuleLearner: Operator-Level Reasoning Tree (OP-Tree)-Based Rules Learning for Formal Verification"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03245"
published: "2026-04-07"
fetched: "2026-04-08T07:02:14.680257"
---

Computer Science > Hardware Architecture
[Submitted on 6 Mar 2026]
Title:FVRuleLearner: Operator-Level Reasoning Tree (OP-Tree)-Based Rules Learning for Formal Verification
View PDF HTML (experimental)Abstract:The remarkable reasoning and code generation capabilities of large language models (LLMs) have recently motivated increasing interest in automating formal verification (FV), a process that ensures hardware correctness through mathematically precise assertions but remains highly labor-intensive, particularly through the translation of natural language into SystemVerilog Assertions (NL-to-SVA). However, LLMs still struggle with SVA generation due to limited training data and the intrinsic complexity of FV operators. Consequently, a more efficient and robust methodology for ensuring correct SVA operator selection is essential for producing functionally correct assertions. To address these challenges, we introduce FVRuleLearner, an Operator-Level Rule (Op-Rule) learning framework built on a novel Operator Reasoning Tree (OP-Tree), which models SVA generation as structured, interpretable reasoning. FVRuleLearner operates in two complementary phases: (1) Training: it constructs OP-Tree that decomposes NL-to-SVA alignment into fine-grained, operator-aware questions, combining reasoning paths that lead to correct assertions; and (2) Testing: it performs operator-aligned retrieval to fetch relevant reasoning traces from the learned OP-Tree and generate new rules for unseen specifications. In the comprehensive studies, the proposed FVRuleLearner outperforms the state-of-the-art baseline by 3.95% in syntax correctness and by 31.17% in functional correctness on average. Moreover, FVRuleLearner successfully reduces an average of 70.33% of SVA functional failures across diverse operator categories through a functional taxonomy analysis, showing the effectiveness of applying learned OP-Tree to the Op-Rule generations for unseen NL-to-SVA tasks. These results establish FVRuleLearner as a new paradigm for domain-specific reasoning and rule learning in formal verification.
Current browse context:
cs.AR
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
