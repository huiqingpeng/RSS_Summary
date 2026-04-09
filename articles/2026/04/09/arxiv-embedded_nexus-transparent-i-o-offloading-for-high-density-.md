---
title: "Nexus: Transparent I/O Offloading for High-Density Serverless Computing"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2604.06682"
published: "2026-04-09"
fetched: "2026-04-10T07:04:50.104931"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 8 Apr 2026]
Title:Nexus: Transparent I/O Offloading for High-Density Serverless Computing
View PDF HTML (experimental)Abstract:Serverless computing relies on extreme multi-tenancy to remain economically viable, driving providers to rely on virtual machines (VMs) that ensure strong isolation and seamless ecosystem compatibility with the FaaS programming model. However, current architectures tightly couple application processing logic with I/O processing, forcing every VM to duplicate a heavy communication fabric (cloud SDK, RPC, and TCP/IP). Our analysis reveals this duplication consumes over 25% of a function's memory footprint, and may double the CPU cycles in VMs compared to bare-metal execution. While prior systems attempt to solve this using WebAssembly or library OSes, they naively sacrifice ecosystem compatibility, forcing developers to migrate code and dependencies to new languages.
We introduce Nexus, a serverless-native KVM-based hypervisor that transparently decouples compute from I/O. Nexus shifts the execution model by intercepting communication fabric at the API boundary and offloading it to an always-on host shared backend via zero-copy shared memory. This removes the heavyweight communication fabric from the guest VM, while preserving the conventional serverless programming model. By structurally separating these domains, Nexus unlocks asynchronous I/O optimizations: overlapping input payload prefetching with VM restoration from a snapshot and writing output payloads back to storage off the critical path. Compared to the production baseline, Nexus reduces overall node-level CPU and memory consumption by up to 44% and 31%, respectively, thus increasing deployment density by 37%. Also, Nexus reduces warm- and cold-start latency by 39% and 10%, respectively, bringing the response time within 20% of that of a WASM-based, ecosystem-incompatible hypervisor.
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
