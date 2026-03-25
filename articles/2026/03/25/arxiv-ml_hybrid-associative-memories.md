---
title: "Hybrid Associative Memories"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22325"
published: "2026-03-25"
fetched: "2026-03-26T07:11:27.255521"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Hybrid Associative Memories
View PDF HTML (experimental)Abstract:Recurrent neural networks (RNNs) and self-attention are both widely used sequence-mixing layers that maintain an internal memory. However, this memory is constructed using two orthogonal mechanisms: RNNs compress the entire past into a fixed-size state, whereas self-attention's state stores every past time step growing its state (the KV cache) linearly with the sequence length. This results in orthogonal strengths and weaknesses. Self-attention layers excel at retrieving information in the context but have large memory and computational costs, while RNNs are more efficient but degrade over longer contexts and underperform for precise recall tasks. Prior work combining these mechanisms has focused primarily on naively interleaving them to reduce computational cost without regard to their complementary mechanisms. We propose the Hybrid Associative Memory (HAM) layer, which combines self-attention and RNNs while leveraging their individual strengths: the RNN compresses the entire sequence, while attention supplements it *only* with information that is difficult for the RNN to predict, which is hence the most valuable information to explicitly store. HAM layers enable data-dependent growth of the KV cache, which can be precisely controlled by the user with a single, continuous threshold. We find that this fine-grained control of the KV cache growth rate has a smooth trade-off with loss and performance. Empirically, we show that our hybrid architecture offers strong, competitive performance relative to RNNs and Transformers even at substantially lower KV-cache usage.
Submission history
From: Kamesh Krishnamurthy [view email][v1] Fri, 20 Mar 2026 14:12:00 UTC (1,763 KB)
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
