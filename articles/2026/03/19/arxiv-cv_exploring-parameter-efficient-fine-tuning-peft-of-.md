---
title: "Exploring parameter-efficient fine-tuning (PEFT) of billion-parameter vision models with QLoRA and DoRA: insights into generalization for limited-data image classification under a 98:1 test-to-train regime"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17782"
published: "2026-03-19"
fetched: "2026-03-19T15:17:46.654234"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Exploring parameter-efficient fine-tuning (PEFT) of billion-parameter vision models with QLoRA and DoRA: insights into generalization for limited-data image classification under a 98:1 test-to-train regime
View PDF HTML (experimental)Abstract:Automated behavior classification is essential for precision livestock farming but faces challenges of high computational costs and limited labeled data. This study systematically compared three approaches: training from scratch (ResNet-18, ViT-Small), frozen feature extraction, and parameter-efficient fine-tuning (PEFT) of the DINOv3 foundation model (6.7 billion parameters). We evaluated QLoRA and DoRA across multiple configurations varying rank (8, 16, 64) and target modules (q_proj versus all-linear layers).
With 2,160 verified training images, we assessed generalization of our model on 211,800 test samples, which is essentially a 98:1 test-to-train ratio. Results demonstrated that PEFT substantially outperformed alternatives, where the best QLoRA configuration (all-linear layers and rank=64) achieved 83.16% test accuracy with only 2.72% parameters (183.0M) in 5.8 hours, compared to 72.87% for ResNet-18 (16.8 hours), 61.91% for ViT-Small (18.7 hours), and 76.56% for frozen DINOv3 (17.5 hours). DoRA achieved comparable accuracy (83.14%) but with longer training time (11.0 hours).
Notably, increasing adapter capacity consistently improved generalization while simultaneously not causing overfitting: reducing rank from 16 to 8 decreased test accuracy from 78.38% to 77.17%, while expanding from q_proj-only to all-linear layers with rank=64 improved accuracy from 78.38% to 83.16%. This suggests underfitting, instead of overfitting, is the primary challenge when adapting foundation models to agricultural imagery. Our findings provide guidelines for deploying billion-parameter vision models with PEFT in agricultural livestock applications.
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
