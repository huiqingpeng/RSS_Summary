---
title: "DST-Net: A Dual-Stream Transformer with Illumination-Independent Feature Guidance and Multi-Scale Spatial Convolution for Low-Light Image Enhancement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16482"
published: "2026-03-18"
fetched: "2026-03-18T18:14:08.741581"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:DST-Net: A Dual-Stream Transformer with Illumination-Independent Feature Guidance and Multi-Scale Spatial Convolution for Low-Light Image Enhancement
View PDFAbstract:Low-light image enhancement aims to restore the visibility of images captured by visual sensors in dim environments by addressing their inherent signal degradations, such as luminance attenuation and structural corruption. Although numerous algorithms attempt to improve image quality, existing methods often cause a severe loss of intrinsic signal priors. To overcome these challenges, we propose a Dual-Stream Transformer Network (DST-Net) based on illumination-agnostic signal prior guidance and multi-scale spatial convolutions. First, to address the loss of critical signal features under low-light conditions, we design a feature extraction module. This module integrates Difference of Gaussians (DoG), LAB color space transformations, and VGG-16 for texture extraction, utilizing decoupled illumination-agnostic features as signal priors to continuously guide the enhancement process. Second, we construct a dual-stream interaction architecture. By employing a cross-modal attention mechanism, the network leverages the extracted priors to dynamically rectify the deteriorated signal representation of the enhanced image, ultimately achieving iterative enhancement through differentiable curve estimation. Furthermore, to overcome the inability of existing methods to preserve fine structures and textures, we propose a Multi-Scale Spatial Fusion Block (MSFB) featuring pseudo-3D and 3D gradient operator convolutions. This module integrates explicit gradient operators to recover high-frequency edges while capturing inter-channel spatial correlations via multi-scale spatial convolutions. Extensive evaluations and ablation studies demonstrate that DST-Net achieves superior performance in subjective visual quality and objective metrics. Specifically, our method achieves a PSNR of 25.64 dB on the LOL dataset. Subsequent validation on the LSRW dataset further confirms its robust cross-scene generalization.
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
