---
title: "To See or To Please: Uncovering Visual Sycophancy and Split Beliefs in VLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18373"
published: "2026-03-20"
fetched: "2026-03-20T15:07:39.853508"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:To See or To Please: Uncovering Visual Sycophancy and Split Beliefs in VLMs
View PDF HTML (experimental)Abstract:When VLMs answer correctly, do they genuinely rely on visual information or exploit language shortcuts? We introduce the Tri-Layer Diagnostic Framework, which disentangles hallucination sources via three metrics: Latent Anomaly Detection (perceptual awareness), Visual Necessity Score (visual dependency, measured via KL divergence), and Competition Score (conflict between visual grounding and instruction following). Using counterfactual interventions (blind, noise, and conflict images) across 7 VLMs and 7,000 model-sample pairs, our taxonomy reveals that 69.6% of samples exhibit Visual Sycophancy--models detect visual anomalies but hallucinate to satisfy user expectations--while zero samples show Robust Refusal, indicating alignment training has systematically suppressed truthful uncertainty acknowledgment. A scaling analysis (Qwen2.5-VL 7B to 72B) shows larger models reduce Language Shortcuts but amplify Visual Sycophancy, demonstrating scale alone cannot resolve the grounding problem. Diagnostic scores further enable a post-hoc selective prediction strategy achieving up to +9.5pp accuracy at 50% coverage with no additional training cost.
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
