---
title: "Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17683"
published: "2026-03-19"
fetched: "2026-03-19T13:14:45.080246"
---

Computer Science > Artificial Intelligence
[Submitted on 18 Mar 2026]
Title:Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents
View PDF HTML (experimental)Abstract:Large language model (LLM) agents deployed in unknown environments must learn task structure at test time, but current approaches require thousands of interactions to form useful hypotheses. We present Sensi, an LLM agent architecture for the ARC-AGI-3 game-playing challenge that introduces structured test-time learning through three mechanisms: (1) a two-player architecture separating perception from action, (2) a curriculum-based learning system managed by an external state machine, and (3) a database-as-control-plane that makes the agents context window programmatically steerable. We further introduce an LLM-as-judge component with dynamically generated evaluation rubrics to determine when the agent has learned enough about one topic to advance to the next. We report results across two iterations: Sensi v1 solves 2 game levels using the two-player architecture alone, while Sensi v2 adds curriculum learning and solves 0 levels - but completes its entire learning curriculum in approximately 32 action attempts, achieving 50-94x greater sample efficiency than comparable systems that require 1600-3000 attempts. We precisely diagnose the failure mode as a self-consistent hallucination cascade originating in the perception layer, demonstrating that the architectural bottleneck has shifted from learning efficiency to perceptual grounding - a more tractable problem.
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
