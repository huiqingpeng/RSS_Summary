---
title: "LenghuSky-8: An 8-Year All-Sky Cloud Dataset with Star-Aware Masks and Alt-Az Calibration for Segmentation and Nowcasting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16429"
published: "2026-03-18"
fetched: "2026-03-18T18:23:22.976898"
---

Astrophysics > Instrumentation and Methods for Astrophysics
[Submitted on 17 Mar 2026]
Title:LenghuSky-8: An 8-Year All-Sky Cloud Dataset with Star-Aware Masks and Alt-Az Calibration for Segmentation and Nowcasting
View PDF HTML (experimental)Abstract:Ground-based time-domain observatories require minute-by-minute, site-scale awareness of cloud cover, yet existing all-sky datasets are short, daylight-biased, or lack astrometric calibration. We present LenghuSky-8, an eight-year (2018-2025) all-sky imaging dataset from a premier astronomical site, comprising 429,620 $512 \times 512$ frames with 81.2% night-time coverage, star-aware cloud masks, background masks, and per-pixel altitude-azimuth (Alt-Az) calibration. For robust cloud segmentation across day, night, and lunar phases, we train a linear probe on DINOv3 local features and obtain 93.3% $\pm$ 1.1% overall accuracy on a balanced, manually labeled set of 1,111 images. Using stellar astrometry, we map each pixel to local alt-az coordinates and measure calibration uncertainties of approximately 0.37 deg at zenith and approximately 1.34 deg at 30 deg altitude, sufficient for integration with telescope schedulers. Beyond segmentation, we introduce a short-horizon nowcasting benchmark over per-pixel three-class logits (sky/cloud/contamination) with four baselines: persistence (copying the last frame), optical flow, ConvLSTM, and VideoGPT. ConvLSTM performs best but yields only limited gains over persistence, underscoring the difficulty of near-term cloud evolution. We release the dataset, calibrations, and an open-source toolkit for loading, evaluation, and scheduler-ready alt-az maps to boost research in segmentation, nowcasting, and autonomous observatory operations.
Current browse context:
astro-ph.IM
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
