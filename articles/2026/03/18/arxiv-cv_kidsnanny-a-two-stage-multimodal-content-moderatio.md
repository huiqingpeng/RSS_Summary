---
title: "KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16181"
published: "2026-03-18"
fetched: "2026-03-18T18:07:51.763887"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety
View PDF HTML (experimental)Abstract:We present KidsNanny, a two-stage multimodal content moderation architecture for child safety. Stage 1 combines a vision transformer (ViT) with an object detector for visual screening (11.7 ms); outputs are routed as text not raw pixels to Stage 2, which applies OCR and a text based 7B language model for contextual reasoning (120 ms total pipeline). We evaluate on the UnsafeBench Sexual category (1,054 images) under two regimes: vision-only, isolating Stage 1, and multimodal, evaluating the full Stage 1+2 pipeline. Stage 1 achieves 80.27% accuracy and 85.39% F1 at 11.7 ms; vision-only baselines range from 59.01% to 77.04% accuracy. The full pipeline achieves 81.40% accuracy and 86.16% F1 at 120 ms, compared to ShieldGemma-2 (64.80% accuracy, 1,136 ms) and LlavaGuard (80.36% accuracy, 4,138 ms). To evaluate text-awareness, we filter two subsets: a text+visual subset (257 images) and a text-only subset (44 images where safety depends primarily on embedded text). On text-only images, KidsNanny achieves 100% recall (25/25 positives; small sample) and 75.76% precision; ShieldGemma-2 achieves 84% recall and 60% precision at 1,136 ms. Results suggest that dedicated OCR-based reasoning may offer recall-precision advantages on text-embedded threats at lower latency, though the small text-only subset limits generalizability. By documenting this architecture and evaluation methodology, we aim to contribute to the broader research effort on efficient multimodal content moderation for child safety.
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
