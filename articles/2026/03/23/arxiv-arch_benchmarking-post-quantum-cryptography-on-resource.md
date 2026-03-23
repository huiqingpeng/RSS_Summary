---
title: "Benchmarking Post-Quantum Cryptography on Resource-Constrained IoT Devices: ML-KEM and ML-DSA on ARM Cortex-M0+"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19340"
published: "2026-03-23"
fetched: "2026-03-24T07:14:11.116123"
---

Computer Science > Cryptography and Security
[Submitted on 19 Mar 2026]
Title:Benchmarking Post-Quantum Cryptography on Resource-Constrained IoT Devices: ML-KEM and ML-DSA on ARM Cortex-M0+
View PDF HTML (experimental)Abstract:The migration to post-quantum cryptography is urgent for Internet of Things devices with 10-20 year lifespans, yet no systematic benchmarks exist for the finalised NIST standards on the most constrained 32-bit processor class. This paper presents the first isolated algorithm-level benchmarks of ML-KEM (FIPS 203) and ML-DSA (FIPS 204) on ARM Cortex-M0+, measured on the RP2040 (Raspberry Pi Pico) at 133 MHz with 264 KB SRAM. Using PQClean reference C implementations, we measure all three security levels of ML-KEM (512/768/1024) and ML-DSA (44/65/87) across key generation, encapsulation/signing, and decapsulation/verification. ML-KEM-512 completes a full key exchange in 36.3 ms consuming 2.87 mJ--17x faster and 94% less energy than ECDH P-256 on the same hardware. ML-DSA signing exhibits high latency variance due to rejection sampling (coefficient of variation 61-71%, 99th-percentile up to 1,115 ms for ML-DSA-87). The M0+ incurs only a 1.8-1.9x slowdown relative to published Cortex-M4 results, despite lacking 64-bit multiply, DSP, and SIMD instructions. All code, data, and scripts are released as an open-source benchmark suite for reproducibility.
Current browse context:
cs.CR
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
