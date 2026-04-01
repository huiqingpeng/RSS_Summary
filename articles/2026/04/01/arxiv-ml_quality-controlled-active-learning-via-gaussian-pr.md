---
title: "Quality-Controlled Active Learning via Gaussian Processes for Robust Structure-Property Learning in Autonomous Microscopy"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29135"
published: "2026-04-01"
fetched: "2026-04-02T07:15:32.988536"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Quality-Controlled Active Learning via Gaussian Processes for Robust Structure-Property Learning in Autonomous Microscopy
View PDF HTML (experimental)Abstract:Autonomous experimental systems are increasingly used in materials research to accelerate scientific discovery, but their performance is often limited by low-quality, noisy data. This issue is especially problematic in data-intensive structure-property learning tasks such as Image-to-Spectrum (Im2Spec) and Spectrum-to-Image (Spec2Im) translations, where standard active learning strategies can mistakenly prioritize poor-quality measurements. We introduce a gated active learning framework that combines curiosity-driven sampling with a physics-informed quality control filter based on the Simple Harmonic Oscillator model fits, allowing the system to automatically exclude low-fidelity data during acquisition. Evaluations on a pre-acquired dataset of band-excitation piezoresponse spectroscopy (BEPS) data from PbTiO3 thin films with spatially localized noise show that the proposed method outperforms random sampling, standard active learning, and multitask learning strategies. The gated approach enhances both Im2Spec and Spec2Im by handling noise during training and acquisition, leading to more reliable forward and inverse predictions. In contrast, standard active learners often misinterpret noise as uncertainty and end up acquiring bad samples that hurt performance. Given its promising applicability, we further deployed the framework in real-time experiments on BiFeO3 thin films, demonstrating its effectiveness in real autonomous microscopy experiments. Overall, this work supports a shift toward hybrid autonomy in self-driving labs, where physics-informed quality assessment and active decision-making work hand-in-hand for more reliable discovery.
Submission history
From: Md Hasan Jawad Chowdhury [view email][v1] Tue, 31 Mar 2026 01:35:12 UTC (15,823 KB)
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
