---
title: "Edit-As-Act: Goal-Regressive Planning for Open-Vocabulary 3D Indoor Scene Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17583"
published: "2026-03-19"
fetched: "2026-03-19T15:14:24.828794"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Edit-As-Act: Goal-Regressive Planning for Open-Vocabulary 3D Indoor Scene Editing
View PDF HTML (experimental)Abstract:Editing a 3D indoor scene from natural language is conceptually straightforward but technically challenging. Existing open-vocabulary systems often regenerate large portions of a scene or rely on image-space edits that disrupt spatial structure, resulting in unintended global changes or physically inconsistent layouts. These limitations stem from treating editing primarily as a generative task. We take a different view. A user instruction defines a desired world state, and editing should be the minimal sequence of actions that makes this state true while preserving everything else. This perspective motivates Edit-As-Act, a framework that performs open-vocabulary scene editing as goal-regressive planning in 3D space. Given a source scene and free-form instruction, Edit-As-Act predicts symbolic goal predicates and plans in EditLang, a PDDL-inspired action language that we design with explicit preconditions and effects encoding support, contact, collision, and other geometric relations. A language-driven planner proposes actions, and a validator enforces goal-directedness, monotonicity, and physical feasibility, producing interpretable and physically coherent transformations. By separating reasoning from low-level generation, Edit-As-Act achieves instruction fidelity, semantic consistency, and physical plausibility - three criteria that existing paradigms cannot satisfy together. On E2A-Bench, our benchmark of 63 editing tasks across 9 indoor environments, Edit-As-Act significantly outperforms prior approaches across all edit types and scene categories.
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
