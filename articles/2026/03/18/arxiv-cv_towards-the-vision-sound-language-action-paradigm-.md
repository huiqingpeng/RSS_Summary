---
title: "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16086"
published: "2026-03-18"
fetched: "2026-03-18T18:23:05.971146"
---

Computer Science > Robotics
[Submitted on 17 Mar 2026]
Title:Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation
View PDF HTML (experimental)Abstract:While recent Vision-Language-Action (VLA) models have begun to incorporate audio, they typically treat sound as static pre-execution prompts or focus exclusively on human speech. This leaves a significant gap in real-time, sound-centric manipulation where fleeting environmental acoustics provide critical state verification during task execution. Consequently, key sounds are easily missed due to low-frequency updates or system latency. This problem is exacerbated by action chunking with open-loop execution, which creates a Blind Execution Interval where acoustic events are lost between discrete audio observation windows. Recognizing the necessity of continuous auditory awareness, we formalize Vision-Sound-Language-Action (VSLA) as a continuous control paradigm conditioned on vision, streaming audio, language, and proprioception under delayed decision loops. As an instantiation, we introduce HEAR, a VSLA framework integrating four components: (i) a streaming Historizer to maintain a compact, causal audio context across execution gaps; (ii) an Envisioner adapted from omni foundation models to reason over multi-sensory inputs; (iii) an Advancer, formulated as an audio world model, to learn temporal dynamics by predicting near-future audio codes; and (iv) a flow-matching Realizer policy to generate smooth action chunks. To address the scarcity of pretraining data and evaluations for VSLA, we construct OpenX-Sound for pretraining, alongside HEAR-Bench, the first sound-centric manipulation benchmark with strict causal timing rules. Our results suggest that robust sound-centric manipulation necessitates causal persistence and explicit temporal learning. This framework provides a practical step toward multi-sensory foundation models for embodied agents, enabling robots to perceive and interact with dynamic environments. Code and videos are available at this https URL.
Current browse context:
cs.RO
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
