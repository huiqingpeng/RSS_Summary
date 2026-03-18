---
title: "S2Act: Simple Spiking Actor"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15725"
published: "2026-03-18"
fetched: "2026-03-18T16:06:59.413025"
---

Computer Science > Multiagent Systems
[Submitted on 16 Mar 2026]
Title:S2Act: Simple Spiking Actor
View PDF HTML (experimental)Abstract:Spiking neural networks (SNNs) and biologically-inspired learning mechanisms are attractive in mobile robotics, where the size and performance of onboard neural network policies are constrained by power and computational budgets. Existing SNN approaches, such as population coding, reward modulation, and hybrid artificial neural network (ANN)-SNN architectures, have shown promising results; however, they face challenges in complex, highly stochastic environments due to SNN sensitivity to hyperparameters and inconsistent gradient signals. To address these challenges, we propose simple spiking actor (S2Act), a computationally lightweight framework that deploys an RL policy using an SNN in three steps: (1) architect an actor-critic model based on an approximated network of rate-based spiking neurons, (2) train the network with gradients using compatible activation functions, and (3) transfer the trained weights into physical parameters of rate-based leaky integrate-and-fire (LIF) neurons for inference and deployment. By globally shaping LIF neuron parameters such that their rate-based responses approximate ReLU activations, S2Act effectively mitigates the vanishing gradient problem, while pre-constraining LIF response curves reduces reliance on complex SNN-specific hyperparameter tuning. We demonstrate our method in two multi-agent stochastic environments (capture-the-flag and parking) that capture the complexity of multi-robot interactions, and deploy our trained policies on physical TurtleBot platforms using Intel's Loihi neuromorphic hardware. Our experimental results show that S2Act outperforms relevant baselines in task performance and real-time inference in nearly all considered scenarios, highlighting its potential for rapid prototyping and efficient real-world deployment of SNN-based RL policies.
Current browse context:
cs.MA
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
