---
title: "BAWSeg: A UAV Multispectral Benchmark for Barley Weed Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.01932"
published: "2026-03-18"
fetched: "2026-03-18T18:33:29.030766"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:BAWSeg: A UAV Multispectral Benchmark for Barley Weed Segmentation
View PDF HTML (experimental)Abstract:Accurate weed mapping in cereal fields requires pixel-level segmentation from UAV imagery that remains reliable across fields, seasons, and illumination. Existing multispectral pipelines often depend on thresholded vegetation indices, which are brittle under radiometric drift and mixed crop--weed pixels, or on single-stream CNN and Transformer backbones that ingest stacked bands and indices, where radiance cues and normalized index cues interfere and reduce sensitivity to small weed clusters embedded in crop canopy. We propose VISA, a two-stream segmentation network that decouples these cues and fuses them at native resolution. The radiance stream learns from calibrated five-band reflectance using local residual convolutions, channel recalibration, spatial gating, and skip-connected decoding, which preserve fine textures, row boundaries, and small weed structures that are often weakened after ratio-based index compression. The index stream operates on vegetation-index maps with windowed self-attention to model local structure efficiently, state-space layers to propagate field-scale context without quadratic attention cost, and Slot Attention to form stable region descriptors that improve discrimination of sparse weeds under canopy mixing. To support supervised training and deployment-oriented evaluation, we introduce BAWSeg, a four-year UAV multispectral dataset collected over commercial barley paddocks in Western Australia, providing radiometrically calibrated blue, green, red, red edge, and near-infrared orthomosaics, derived vegetation indices, and dense crop, weed, and other labels with leakage-free block splits. On BAWSeg, VISA achieves 75.6% mIoU and 63.5% weed IoU with 22.8 M parameters, outperforming a multispectral SegFormer-B1 baseline by 1.2 mIoU and 1.9 weed IoU. Under cross-plot and cross-year protocols, VISA maintains 71.2% and 69.2% mIoU, respectively.
Submission history
From: Haitian Wang [view email][v1] Mon, 2 Mar 2026 14:49:05 UTC (19,115 KB)
[v2] Tue, 17 Mar 2026 17:55:38 UTC (18,999 KB)
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
