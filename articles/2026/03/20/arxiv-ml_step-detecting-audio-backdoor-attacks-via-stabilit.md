---
title: "STEP: Detecting Audio Backdoor Attacks via Stability-based Trigger Exposure Profiling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18103"
published: "2026-03-20"
fetched: "2026-03-20T13:08:48.943610"
---

Computer Science > Cryptography and Security
[Submitted on 18 Mar 2026]
Title:STEP: Detecting Audio Backdoor Attacks via Stability-based Trigger Exposure Profiling
View PDF HTML (experimental)Abstract:With the widespread deployment of deep-learning-based speech models in security-critical applications, backdoor attacks have emerged as a serious threat: an adversary who poisons a small fraction of training data can implant a hidden trigger that controls the model's output while preserving normal behavior on clean inputs. Existing inference-time defenses are not well suited to the audio domain, as they either rely on trigger over-robustness assumptions that fail on transformation-based and semantic triggers, or depend on properties specific to image or text modalities. In this paper, we propose STEP (Stability-based Trigger Exposure Profiling), a black-box, retraining-free backdoor detector that operates under hard-label-only access. Its core idea is to exploit a characteristic dual anomaly of backdoor triggers: anomalous label stability under semantic-breaking perturbations, and anomalous label fragility under semantic-preserving perturbations. STEP profiles each test sample with two complementary perturbation branches that target these two properties respectively, scores the resulting stability features with one-class anomaly detectors trained on benign references, and fuses the two scores via unsupervised weighting. Extensive experiments across seven backdoor attacks show that STEP achieves an average AUROC of 97.92% and EER of 4.54%, substantially outperforming state-of-the-art baselines, and generalizes across model architectures, speech tasks, an open-set verification scenario, and over-the-air physical-world settings.
Current browse context:
cs.CR
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
