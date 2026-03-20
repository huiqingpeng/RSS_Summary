---
title: "SSP-SAM: SAM with Semantic-Spatial Prompt for Referring Expression Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18086"
published: "2026-03-20"
fetched: "2026-03-20T15:05:45.469493"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:SSP-SAM: SAM with Semantic-Spatial Prompt for Referring Expression Segmentation
View PDF HTML (experimental)Abstract:The Segment Anything Model (SAM) excels at general image segmentation but has limited ability to understand natural language, which restricts its direct application in Referring Expression Segmentation (RES). Toward this end, we propose SSP-SAM, a framework that fully utilizes SAM's segmentation capabilities by integrating a Semantic-Spatial Prompt (SSP) encoder. Specifically, we incorporate both visual and linguistic attention adapters into the SSP encoder, which highlight salient objects within the visual features and discriminative phrases within the linguistic features. This design enhances the referent representation for the prompt generator, resulting in high-quality SSPs that enable SAM to generate precise masks guided by language. Although not specifically designed for Generalized RES (GRES), where the referent may correspond to zero, one, or multiple objects, SSP-SAM naturally supports this more flexible setting without additional modifications. Extensive experiments on widely used RES and GRES benchmarks confirm the superiority of our method. Notably, our approach generates segmentation masks of high quality, achieving strong precision even at strict thresholds such as Pr@0.9. Further evaluation on the PhraseCut dataset demonstrates improved performance in open-vocabulary scenarios compared to existing state-of-the-art RES methods. The code and checkpoints are available at: this https URL.
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
