---
title: "Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16741"
published: "2026-03-18"
fetched: "2026-03-18T15:47:30.824174"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests
View PDF HTML (experimental)Abstract:Objective. We establish a principled method for inferring mental health related psychometric variables from neural and behavioral data using the Implicit Association Test (IAT) as the data generation engine, aiming to overcome the limited predictive performance (typically under 0.7 AUC) of the gold-standard D-score method, which relies solely on reaction times.
Approach. We propose a sparse hierarchical Bayesian model that leverages multi-modal data to predict experiences related to mental illness symptoms in new participants. The model is a multivariate generalization of the D-score with trainable parameters, engineered for parameter efficiency in the small-cohort regime typical of IAT studies. Data from two IAT variants were analyzed: a suicidality-related E-IAT ($n=39$) and a psychosis-related PSY-IAT ($n=34$).
Main Results. Our approach overcomes a high inter-individual variability and low within-session effect size in the dataset, reaching AUCs of 0.73 (E-IAT) and 0.76 (PSY-IAT) in the best modality configurations, though corrected 95% confidence intervals are wide ($\pm 0.18$) and results are marginally significant after FDR correction ($q=0.10$). Restricting the E-IAT to MDD participants improves AUC to 0.79 $[0.62, 0.97]$ (significant at $q=0.05$). Performance is on par with the best reference methods (shrinkage LDA and EEGNet) for each task, even when the latter were adapted to the task, while the proposed method was not. Accuracy was substantially above near-chance D-scores (0.50-0.53 AUC) in both tasks, with more consistent cross-task performance than any single reference method.
Significance. Our framework shows promise for enhancing IAT-based assessment of experiences related to entrapment and psychosis, and potentially other mental health conditions, though further validation on larger and independent cohorts will be needed to establish clinical utility.
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
