---
title: "Synergistic Bleeding Region and Point Detection in Laparoscopic Surgical Videos"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.22174"
published: "2026-03-19"
fetched: "2026-03-19T16:24:06.887161"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 28 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Synergistic Bleeding Region and Point Detection in Laparoscopic Surgical Videos
View PDF HTML (experimental)Abstract:Intraoperative bleeding in laparoscopic surgery causes rapid obscuration of the operative field to hinder the surgical process and increases the risk of postoperative complications. Intelligent detection of bleeding areas can quantify the blood loss to assist decision-making, while locating bleeding points helps surgeons quickly identify the source of bleeding and achieve hemostasis in time to improve surgical success rates. To fill the benchmark gap, we first construct a real-world laparoscopic surgical bleeding detection dataset, named SurgBlood, comprising 5,330 frames from 95 surgical video clips with bleeding region and point annotations. Accordingly, we develop a dual-task synergistic online detector called BlooDet, enabling simultaneous detection of bleeding regions and points in laparoscopic surgery. The baseline embraces a dual-branch bidirectional guid- ance design based on Segment Anything Model 2. The mask branch detects bleeding regions through adaptive edge and point prompt embeddings, while the point branch leverages mask memory to induce bleeding point memory modeling and captures point motion direction via inter-frame optical flow. By coupled bidirectional guidance, our framework explores spatial-temporal correlations while exploiting memory modeling to infer current bleeding status. Extensive experiments indicate that our method outperforms 13 counterparts in bleeding detection.
Submission history
From: Jialun Pei [view email][v1] Fri, 28 Mar 2025 06:27:55 UTC (6,013 KB)
[v2] Fri, 23 May 2025 17:38:17 UTC (10,598 KB)
[v3] Mon, 24 Nov 2025 07:45:44 UTC (4,733 KB)
[v4] Wed, 18 Mar 2026 09:49:51 UTC (3,874 KB)
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
