---
title: "Generalizing Dynamics Modeling More Easily from Representation Perspective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22655"
published: "2026-03-25"
fetched: "2026-03-26T07:16:00.889029"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Generalizing Dynamics Modeling More Easily from Representation Perspective
View PDF HTML (experimental)Abstract:Learning system dynamics from observations is a critical problem in many applications over various real-world complex systems, e.g., climate, ecology, and fluid systems. Recently, neural dynamics modeling method have become a prevalent solution that embeds the object's observations into a latent space before learning dynamics using neural methods such as neural Ordinary Differential Equations (ODE). Existing dynamics modeling methods induce a specific model for each observation of different complex systems, resulting in poor generalization across systems. Inspired by the great success of pre-trained models, we conduct a generalized Pre-trained Dynamics EncoDER (PDEDER) which can embed the original state observations into a latent space where the dynamics can be captured more easily. To conduct the generalized PDEDER, we pre-train any Pre-trained Language Model (PLM) by minimizing the Lyapunov exponent objective, which constrains the chaotic behavior of governing dynamics learned in the latent space. By penalizing the divergence of embedded observations, our PDEDER promotes locally stable and well-structured latent dynamics, thereby facilitating more effective dynamics modeling than in the original observation space. In addition, we incorporate reconstruction and forecasting objectives to mitigate the risk of obtaining an over-smoothed latent space. Specifically, we collect 152 sets of real-world and synthetic observations from 23 complex systems as pre-training corpora and employ them to pre-train PDEDER. Given any future dynamic observation, we can fine-tune PDEDER with any specific dynamics modeling method. We evaluate PDEDER on 12 dynamic systems by short/long-term forecasting under both in-domain and cross-domain settings, and the empirical results indicate the effectiveness and generalizability of PDEDER.
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
