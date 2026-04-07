---
title: "Embedding-Only Uplink for Onboard Retrieval Under Shift in Remote Sensing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03301"
published: "2026-04-07"
fetched: "2026-04-08T07:02:42.177252"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 30 Mar 2026]
Title:Embedding-Only Uplink for Onboard Retrieval Under Shift in Remote Sensing
View PDF HTML (experimental)Abstract:Downlink bottlenecks motivate onboard systems that prioritize hazards without transmitting raw pixels. We study a strict setting where a ground station uplinks only compact embeddings plus metadata, and an onboard system performs vector search to triage new captures. We ask whether this embedding-only pipeline remains useful under explicit remote-sensing shift: cross-time (pre/post-event), cross-event/location (different disasters), cross-site cloud (15 geographic sites), and cross-city AOI holdout (buildings). Using OlmoEarth embeddings on a scaled public multi-task benchmark (27 Sentinel-2 L2A scenes, 15 cloud sites, 5 SpaceNet-2 AOIs; 10 seeds), we find that all effective methods rely on the same uplinked embeddings, but the optimal decision head is task-dependent: kNN retrieval is significantly superior for cloud classification (0.92 vs. centroid 0.91; p<0.01, Wilcoxon), while class centroids dominate temporal change detection (0.85 vs. retrieval 0.48; p<0.01). These results show that embedding-only uplink is the key enabler--once embeddings are onboard, the system can select the best head per task at no additional uplink cost, with all telemetry under 1 KB per query.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
