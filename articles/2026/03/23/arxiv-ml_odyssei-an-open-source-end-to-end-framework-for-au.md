---
title: "ODySSeI: An Open-Source End-to-End Framework for Automated Detection, Segmentation, and Severity Estimation of Lesions in Invasive Coronary Angiography Images"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20021"
published: "2026-03-23"
fetched: "2026-03-24T07:24:10.372162"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:ODySSeI: An Open-Source End-to-End Framework for Automated Detection, Segmentation, and Severity Estimation of Lesions in Invasive Coronary Angiography Images
View PDF HTML (experimental)Abstract:Invasive Coronary Angiography (ICA) is the clinical gold standard for the assessment of coronary artery disease. However, its interpretation remains subjective and prone to intra- and inter-operator variability. In this work, we introduce ODySSeI: an Open-source end-to-end framework for automated Detection, Segmentation, and Severity estimation of lesions in ICA images. ODySSeI integrates deep learning-based lesion detection and lesion segmentation models trained using a novel Pyramidal Augmentation Scheme (PAS) to enhance robustness and real-time performance across diverse patient cohorts (2149 patients from Europe, North America, and Asia). Furthermore, we propose a quantitative coronary angiography-free Lesion Severity Estimation (LSE) technique that directly computes the Minimum Lumen Diameter (MLD) and diameter stenosis from the predicted lesion geometry. Extensive evaluation on both in-distribution and out-of-distribution clinical datasets demonstrates ODySSeI's strong generalizability. Our PAS yields large performance gains in highly complex tasks as compared to relatively simpler ones, notably, a 2.5-fold increase in lesion detection performance versus a 1-3\% increase in lesion segmentation performance over their respective baselines. Our LSE technique achieves high accuracy, with predicted MLD values differing by only $\pm$ 2-3 pixels from the corresponding ground truths. On average, ODySSeI processes a raw ICA image within only a few seconds on a CPU and in a fraction of a second on a GPU and is available as a plug-and-play web interface at this http URL. Overall, this work establishes ODySSeI as a comprehensive and open-source framework which supports automated, reproducible, and scalable ICA analysis for real-time clinical decision-making.
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
