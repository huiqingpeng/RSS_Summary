---
title: "Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2512.01594"
published: "2026-03-24"
fetched: "2026-03-25T07:06:34.061636"
---

Computer Science > Cryptography and Security
[Submitted on 1 Dec 2025 (v1), last revised 21 Mar 2026 (this version, v4)]
Title:Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA
View PDF HTML (experimental)Abstract:Confidential Virtual Machines (CVMs) are increasingly adopted to protect sensitive workloads from privileged adversaries such as the hypervisor. While they provide strong isolation guarantees, existing CVM architectures lack first-class mechanisms for inter-CVM data sharing due to their disjoint memory model, making inter-CVM data exchange a performance bottleneck in compartmentalized or collaborative multi-CVM systems. Under this model, a CVM's accessible memory is either shared with the hypervisor or protected from both the hypervisor and all other CVMs. This design simplifies reasoning about memory ownership; however, it fundamentally precludes plaintext data sharing between CVMs because all inter-CVM communication must pass through hypervisor-accessible memory, requiring costly encryption and decryption to preserve confidentiality and integrity. In this paper, we introduce CAEC, a system that enables protected memory sharing between CVMs. CAEC builds on Arm Confidential Compute Architecture (CCA) and extends its firmware to support Confidential Shared Memory (CSM), a memory region securely shared between multiple CVMs while remaining inaccessible to the hypervisor and all non-participating CVMs. CAEC's design is fully compatible with CCA hardware and introduces only a modest increase (4%) in CCA firmware code size. CAEC delivers substantial performance benefits across a range of workloads. For instance, inter-CVM communication over CAEC achieves up to 209$\times$ reduction in CPU cycles compared to encryption-based mechanisms over hypervisor-accessible shared memory. By combining high performance, strong isolation guarantees, and attestable sharing semantics, CAEC provides a practical and scalable foundation for the next generation of trusted multi-CVM services across both edge and cloud environments.
Submission history
From: Sina Abdollahi Mr [view email][v1] Mon, 1 Dec 2025 12:10:43 UTC (1,102 KB)
[v2] Tue, 2 Dec 2025 08:57:45 UTC (1,102 KB)
[v3] Sat, 7 Mar 2026 15:16:30 UTC (1,103 KB)
[v4] Sat, 21 Mar 2026 13:31:25 UTC (1,103 KB)
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
