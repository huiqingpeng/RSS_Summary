---
title: "Jackknife ARAIM: Efficient GNSS Integrity Monitoring for Simultaneous Faults under Non-Gaussian Errors"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2507.04284"
published: "2026-03-18"
fetched: "2026-03-18T19:10:28.433192"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 6 Jul 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Jackknife ARAIM: Efficient GNSS Integrity Monitoring for Simultaneous Faults under Non-Gaussian Errors
View PDF HTML (experimental)Abstract:Legacy and advanced receiver autonomous integrity monitoring (RAIM/ARAIM) rely on Gaussian error models that can be overly conservative for real-world non-Gaussian errors. This paper proposes an extended jackknife detector capable of detecting multiple simultaneous faults with non-Gaussian nominal errors. Furthermore, an integrity monitoring algorithm, jackknife ARAIM, is developed by systematically exploiting the properties of the jackknife detector in the range domain. We prove that the proposed method has equivalent monitoring performance with the solution separation (SS) ARAIM, but is significantly computationally efficient for single-fault cases with non-Gaussian nominal errors, while maintaining similar efficiency to SS ARAIM for multiple-fault cases. The proposed method is examined in worldwide simulations, with the nominal measurement error simulated based on authentic experimental data, which reveals different findings in existing research. In a single Global Positioning System (GPS) constellation setting, the proposed method can reduce the 99.5 percentile vertical protection level (VPL) below 45 m, outperforming 50 m VPL produced by the ARAIM algorithm using Gaussian nominal error models. In GPS-Galileo dual-constellation setting, while these Gaussian-based ARAIM algorithms suffer VPL inflation over 60 m due to Galileo's heavy-tailed errors, the proposed method maintains VPL below 40 m, achieving over 92% normal operations for 35 m Vertical Alert Limit. Moreover, we tentatively implement the SS ARAIM using non-Gaussian overbounds and compare it with the proposed Jackknife ARAIM method regarding computation efficiency. The proposed method achieves up to 59.4% reduction in median processing time compared to SS ARAIM in single-constellation scenarios.
Submission history
From: Penggao Yan [view email][v1] Sun, 6 Jul 2025 07:57:29 UTC (5,520 KB)
[v2] Wed, 24 Sep 2025 14:35:53 UTC (5,520 KB)
[v3] Tue, 17 Mar 2026 11:39:35 UTC (6,312 KB)
Current browse context:
eess.SP
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
