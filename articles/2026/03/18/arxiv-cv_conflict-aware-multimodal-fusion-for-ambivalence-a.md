---
title: "Conflict-Aware Multimodal Fusion for Ambivalence and Hesitancy Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15818"
published: "2026-03-18"
fetched: "2026-03-18T17:18:57.718225"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Conflict-Aware Multimodal Fusion for Ambivalence and Hesitancy Recognition
View PDF HTML (experimental)Abstract:Ambivalence and hesitancy (A/H) are subtle affective states where a person shows conflicting signals through different channels -- saying one thing while their face or voice tells another story. Recognising these states automatically is valuable in clinical settings, but it is hard for machines because the key evidence lives in the \emph{disagreements} between what is said, how it sounds, and what the face shows.
We present \textbf{ConflictAwareAH}, a multimodal framework built for this problem. Three pre-trained encoders extract video, audio, and text representations. Pairwise conflict features -- element-wise absolute differences between modality embeddings -- serve as \emph{bidirectional} cues: large cross-modal differences flag A/H, while small differences confirm behavioural consistency and anchor the negative class. This conflict-aware design addresses a key limitation of text-dominant approaches, which tend to over-detect A/H (high F1-AH) while struggling to confirm its absence: our multimodal model improves F1-NoAH by +4.6 points over text alone and halves the class-performance gap. A complementary \emph{text-guided late fusion} strategy blends a text-only auxiliary head with the full model at inference, adding +4.1 Macro F1.
On the BAH dataset from the ABAW10 Ambivalence/Hesitancy Challenge, our method reaches \textbf{0.694 Macro F1} on the labelled test split and \textbf{0.715} on the private leaderboard, outperforming published multimodal baselines by over 10 points -- all on a single GPU in under 25 minutes of training.
Submission history
From: Salah Eddine Bekhouche Dr. [view email][v1] Mon, 16 Mar 2026 18:49:46 UTC (244 KB)
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
