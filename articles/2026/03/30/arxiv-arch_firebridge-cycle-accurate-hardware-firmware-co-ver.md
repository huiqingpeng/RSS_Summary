---
title: "FireBridge: Cycle-Accurate Hardware + Firmware Co-Verification for Modern Accelerators"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25969"
published: "2026-03-30"
fetched: "2026-03-31T07:05:33.406817"
---

Computer Science > Hardware Architecture
[Submitted on 26 Mar 2026]
Title:FireBridge: Cycle-Accurate Hardware + Firmware Co-Verification for Modern Accelerators
View PDF HTML (experimental)Abstract:Hardware-firmware integration is becoming a productivity bottleneck due to the increasing complexity of accelerators, characterized by intricate memory hierarchies and firmware-intensive execution. While numerous verification techniques focus on early-stage, approximate modeling of such systems to speed up initial development, developers still rely heavily on FPGA emulation to integrate firmware with RTL/HLS hardware, resulting in significant delays in debug iterations and time-to-market. We present a fast, cycle-accurate co-verification framework that bridges production firmware and RTL/gate-level hardware. FIREBRIDGE enables firmware debugging, profiling, and verification in seconds using standard simulators such as VCS, Vivado Xsim, or Xcelium, by compiling the firmware for x86 and bridging it with simulated subsystems via randomized memory bridges. Our approach provides off-chip data movement profiling, memory congestion emulation, and register-level protocol testing, which are critical for modern accelerator verification. We demonstrate a speedup of up to 50x in debug iteration over the conventional FPGA-based flow for system integration between RTL/HLS and production firmware on various types of accelerators, such as systolic arrays and CGRAs, while ensuring functional equivalence. FIREBRIDGE accelerates system integration by supporting robust co-verification of hardware and firmware, and promotes a structured, parallel development workflow tailored for teams building heterogeneous computing platforms.
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
