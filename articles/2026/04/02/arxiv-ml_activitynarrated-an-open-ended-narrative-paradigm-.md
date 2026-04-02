---
title: "ActivityNarrated: An Open-Ended Narrative Paradigm for Wearable Human Activity Understanding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00767"
published: "2026-04-02"
fetched: "2026-04-03T07:24:22.552833"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:ActivityNarrated: An Open-Ended Narrative Paradigm for Wearable Human Activity Understanding
View PDF HTML (experimental)Abstract:Wearable HAR has improved steadily, but most progress still relies on closed-set classification, which limits real-world use. In practice, human activity is open-ended, unscripted, personalized, and often compositional, unfolding as narratives rather than instances of fixed classes. We argue that addressing this gap does not require simply scaling datasets or models. It requires a fundamental shift in how wearable HAR is formulated, supervised, and evaluated. This work shows how to model open-ended activity narratives by aligning wearable sensor data with natural-language descriptions in an open-vocabulary setting. Our framework has three core components. First, we introduce a naturalistic data collection and annotation pipeline that combines multi-position wearable sensing with free-form, time-aligned narrative descriptions of ongoing behavior, allowing activity semantics to emerge without a predefined vocabulary. Second, we define a retrieval-based evaluation framework that measures semantic alignment between sensor data and language, enabling principled evaluation without fixed classes while also subsuming closed-set classification as a special case. Third, we present a language-conditioned learning architecture that supports sensor-to-text inference over variable-length sensor streams and heterogeneous sensor placements. Experiments show that models trained with fixed-label objectives degrade sharply under real-world variability, while open-vocabulary sensor-language alignment yields robust and semantically grounded representations. Once this alignment is learned, closed-set activity recognition becomes a simple downstream task. Under cross-participant evaluation, our method achieves 65.3% Macro-F1, compared with 31-34% for strong closed-set HAR baselines. These results establish open-ended narrative modeling as a practical and effective foundation for real-world wearable HAR.
Submission history
From: Lala Shakti Swarup Ray [view email][v1] Wed, 1 Apr 2026 11:31:44 UTC (14,172 KB)
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
