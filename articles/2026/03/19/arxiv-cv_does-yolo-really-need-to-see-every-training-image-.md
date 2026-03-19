---
title: "Does YOLO Really Need to See Every Training Image in Every Epoch?"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17684"
published: "2026-03-19"
fetched: "2026-03-19T15:16:03.519942"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Does YOLO Really Need to See Every Training Image in Every Epoch?
View PDF HTML (experimental)Abstract:YOLO detectors are known for their fast inference speed, yet training them remains unexpectedly time-consuming due to their exhaustive pipeline that processes every training image in every epoch, even when many images have already been sufficiently learned. This stands in clear contrast to the efficiency suggested by the ``You Only Look Once'' philosophy. This naturally raises an important question: \textit{Does YOLO really need to see every training image in every epoch?} To explore this, we propose an Anti-Forgetting Sampling Strategy (AFSS) that dynamically determines which images should be used and which can be skipped during each epoch, allowing the detector to learn more effectively and efficiently. Specifically, AFSS measures the learning sufficiency of each training image as the minimum of its detection recall and precision, and dynamically categorizes training images into easy, medium, or hard levels accordingly. Easy training images are sparsely resampled during training in a continuous review manner, with priority given to those that have not been used for a long time to reduce redundancy and prevent forgetting. Moderate training images are partially selected, prioritizing recently unused ones and randomly choosing the rest from unselected images to ensure coverage and prevent forgetting. Hard training images are fully sampled in every epoch to ensure sufficient learning. The learning sufficiency of each training image is periodically updated, enabling detectors to adaptively shift its focus toward the informative training images over time while progressively discarding redundant ones. On widely used natural image detection benchmarks (MS COCO 2017 and PASCAL VOC 2007) and remote sensing detection datasets (DOTA-v1.0 and DIOR-R), AFSS achieves more than $1.43\times$ training speedup for YOLO-series detectors while also improving accuracy.
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
