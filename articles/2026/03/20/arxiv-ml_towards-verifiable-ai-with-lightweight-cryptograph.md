---
title: "Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19025"
published: "2026-03-20"
fetched: "2026-03-20T13:19:06.485206"
---

Computer Science > Cryptography and Security
[Submitted on 19 Mar 2026]
Title:Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference
View PDF HTML (experimental)Abstract:When large AI models are deployed as cloud-based services, clients have no guarantee that responses are correct or were produced by the intended model. Rerunning inference locally is infeasible for large models, and existing cryptographic proof systems -- while providing strong correctness guarantees -- introduce prohibitive prover overhead (e.g., hundreds of seconds per query for billion-parameter models). We present a verification framework and protocol that replaces full cryptographic proofs with a lightweight, sampling-based approach grounded in statistical properties of neural networks. We formalize the conditions under which trace separation between functionally dissimilar models can be leveraged to argue the security of verifiable inference protocols. The prover commits to the execution trace of inference via Merkle-tree-based vector commitments and opens only a small number of entries along randomly sampled paths from output to input. This yields a protocol that trades soundness for efficiency, a tradeoff well-suited to auditing, large-scale deployment settings where repeated queries amplify detection probability, and scenarios with rationally incentivized provers who face penalties upon detection. Our approach reduces proving times by several orders of magnitude compared to state-of-the-art cryptographic proof systems, going from the order of minutes to the order of milliseconds, with moderately larger proofs. Experiments on ResNet-18 classifiers and Llama-2-7B confirm that common architectures exhibit the statistical properties our protocol requires, and that natural adversarial strategies (gradient-descent reconstruction, inverse transforms, logit swapping) fail to produce traces that evade detection. We additionally present a protocol in the refereed delegation model, where two competing servers enable correct output identification in a logarithmic number of rounds.
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
