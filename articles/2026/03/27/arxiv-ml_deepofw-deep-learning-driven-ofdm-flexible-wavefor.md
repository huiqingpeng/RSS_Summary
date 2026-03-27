---
title: "DeepOFW: Deep Learning-Driven OFDM-Flexible Waveform Modulation for Peak-to-Average Power Ratio Reduction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23544"
published: "2026-03-27"
fetched: "2026-03-28T07:13:25.125582"
---

Computer Science > Information Theory
[Submitted on 15 Mar 2026]
Title:DeepOFW: Deep Learning-Driven OFDM-Flexible Waveform Modulation for Peak-to-Average Power Ratio Reduction
View PDF HTML (experimental)Abstract:Peak-to-average power ratio (PAPR) remains a major limitation of multicarrier modulation schemes such as orthogonal frequency-division multiplexing (OFDM), reducing power amplifier efficiency and limiting practical transmit power. In this work, we propose DeepOFW, a deep learning-driven OFDM-flexible waveform modulation framework that enables data-driven waveform design while preserving the low-complexity hardware structure of conventional transceivers. The proposed architecture is fully differentiable, allowing end-to-end optimization of waveform generation and receiver processing under practical physical constraints. Unlike neural transceiver approaches that require deep learning inference at both ends of the link, DeepOFW confines the learning stage to an offline or centralized unit, enabling deployment on standard transmitter and receiver hardware without additional computational overhead. The framework jointly optimizes waveform representations and detection parameters while explicitly incorporating PAPR constraints during training. Extensive simulations over 3GPP multipath channels demonstrate that the learned waveforms significantly reduce PAPR compared with classical OFDM while simultaneously improving bit error rate (BER) performance relative to state-of-the-art transmission schemes. These results highlight the potential of data-driven waveform design to enhance multicarrier communication systems while maintaining hardware-efficient implementations. An open-source implementation of the proposed framework is released to facilitate reproducible research and practical adoption.
Current browse context:
cs.IT
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
