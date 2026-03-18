---
title: "AsgardBench - Evaluating Visually Grounded Interactive Planning Under Minimal Feedback"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15888"
published: "2026-03-18"
fetched: "2026-03-18T18:22:34.569033"
---

Computer Science > Artificial Intelligence
[Submitted on 16 Mar 2026]
Title:AsgardBench - Evaluating Visually Grounded Interactive Planning Under Minimal Feedback
View PDF HTML (experimental)Abstract:With AsgardBench we aim to evaluate visually grounded, high-level action sequence generation and interactive planning, focusing specifically on plan adaptation during execution based on visual observations rather than navigation or low-level manipulation. In the landscape of embodied AI benchmarks, AsgardBench targets the capability category of interactive planning, which is more sophisticated than offline high-level planning as it requires agents to revise plans in response to environmental feedback, yet remains distinct from low-level execution.
Unlike prior embodied AI benchmarks that conflate reasoning with navigation or provide rich corrective feedback that substitutes for perception, AsgardBench restricts agent input to images, action history, and lightweight success/failure signals, isolating interactive planning in a controlled simulator without low-level control noise.
The benchmark contains 108 task instances spanning 12 task types, each systematically varied through object state, placement, and scene configuration. These controlled variations create conditional branches in which a single instruction can require different action sequences depending on what the agent observes, emphasizing conditional branching and plan repair during execution.
Our evaluations of leading vision language models show that performance drops sharply without visual input, revealing weaknesses in visual grounding and state tracking that ultimately undermine interactive planning. Our benchmark zeroes in on a narrower question: can a model actually use what it sees to adapt a plan when things do not go as expected?
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
