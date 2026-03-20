---
title: "What You Read is What You Classify: Highlighting Attributions to Text and Text-Like Inputs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.24149"
published: "2026-03-20"
fetched: "2026-03-20T14:11:50.643916"
---

Computer Science > Machine Learning
[Submitted on 27 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:What You Read is What You Classify: Highlighting Attributions to Text and Text-Like Inputs
View PDFAbstract:At present, there are no easily understood explainable artificial intelligence (AI) methods for discrete token inputs, like text. Most explainable AI techniques do not extend well to token sequences, where both local and global features matter, because state-of-the-art models, like transformers, tend to focus on global connections. Therefore, existing explainable AI algorithms fail by (i) identifying disparate tokens of importance, or (ii) assigning a large number of tokens a low value of importance. This method for explainable AI for tokens-based classifiers generalizes a mask-based explainable AI algorithm for images. It starts with an Explainer neural network that is trained to create masks to hide information not relevant for classification. Then, the Hadamard product of the mask and the continuous values of the classifier's embedding layer is taken and passed through the classifier, changing the magnitude of the embedding vector but keeping the orientation unchanged. The Explainer is trained for a taxonomic classifier for nucleotide sequences and it is shown that the masked segments are less relevant to classification than the unmasked ones. This method focused on the importance the token as a whole (i.e., a segment of the input sequence), producing a human-readable explanation.
Submission history
From: Daniel Berman [view email][v1] Fri, 27 Feb 2026 16:28:58 UTC (2,132 KB)
[v2] Thu, 19 Mar 2026 17:25:16 UTC (1,992 KB)
Current browse context:
cs.LG
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
