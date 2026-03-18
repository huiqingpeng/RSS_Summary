---
title: "Improving Generative Adversarial Network Generalization for Facial Expression Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15648"
published: "2026-03-18"
fetched: "2026-03-18T16:05:19.059423"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Mar 2026]
Title:Improving Generative Adversarial Network Generalization for Facial Expression Synthesis
View PDF HTML (experimental)Abstract:Facial expression synthesis aims to generate realistic facial expressions while preserving identity. Existing conditional generative adversarial networks (GANs) achieve excellent image-to-image translation results, but their performance often degrades when test images differ from the training dataset. We present Regression GAN (RegGAN), a model that learns an intermediate representation to improve generalization beyond the training distribution. RegGAN consists of two components: a regression layer with local receptive fields that learns expression details by minimizing the reconstruction error through a ridge regression loss, and a refinement network trained adversarially to enhance the realism of generated images. We train RegGAN on the CFEE dataset and evaluate its generalization performance both on CFEE and challenging out-of-distribution images, including celebrity photos, portraits, statues, and avatar renderings. For evaluation, we employ four widely used metrics: Expression Classification Score (ECS) for expression quality, Face Similarity Score (FSS) for identity preservation, QualiCLIP for perceptual realism, and Fréchet Inception Distance (FID) for assessing both expression quality and realism. RegGAN outperforms six state-of-the-art models in ECS, FID, and QualiCLIP, while ranking second in FSS. Human evaluations indicate that RegGAN surpasses the best competing model by 25% in expression quality, 26% in identity preservation, and 30% in realism.
Current browse context:
cs.CV
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
