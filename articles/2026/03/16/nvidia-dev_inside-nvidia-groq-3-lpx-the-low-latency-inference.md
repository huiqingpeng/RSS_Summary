---
title: "Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/"
published: "2026-03-16"
fetched: "2026-03-17T07:06:55.576577"
---

NVIDIA Groq 3 LPX is a new rack-scale inference accelerator for the NVIDIA Vera Rubin platform, designed for the low-latency and large-context demands of agentic systems. Co-designed with the NVIDIA Vera Rubin NVL72, LPX equips the AI factory with an engine optimized for fast, predictable token generation, while Vera Rubin NVL72 remains the flexible, general-purpose workhorse for training and inference, delivering high throughput across prefill and decode, including long-context processing, decode attention, and high-concurrency serving at scale.
This combination matters because the agentic future demands a new category of inference. As generation speeds approach 1,000 tokens per second per user, models move beyond conversation-speed interaction toward speed of thought computing. At that rate, AI systems can reason, simulate, and respond continuously, enabling experiences that feel less like turn-based chat and more like real-time collaboration.
This shift also raises the ceiling for multi-agent systems. Individual agents can be powerful on their own, but coordinated groups of agents can accomplish far more, much like human societies scale their capability through collective intelligence and coordination.
Supporting these emerging workloads requires infrastructure that can deliver both high throughput and low latency. The combination of Vera Rubin NVL72 and LPX enables this heterogeneous architecture, pairing large-scale AI factory performance with the fast token generation needed to power continuously running agentic systems and next-generation AI applications.
Introducing NVIDIA Groq 3 LPX
Vera Rubin and LPX unite the extreme performance of Rubin GPUs and LPUs to deliver up to 35x higher inference throughput per megawatt and up to 10x more revenue opportunity for trillion-parameter models. Integrated with the NVIDIA MGX ETL rack architecture and aligned with the broader Vera Rubin platform, LPX gives data centers a way to deploy a dedicated low-latency inference path alongside Vera Rubin NVL72 within a common infrastructure design.
The system is built around 256 interconnected NVIDIA Groq 3 LPU accelerators. Its architecture emphasizes deterministic execution, high on-chip SRAM bandwidth, and tightly coordinated scale-up communication so interactive inference can stay responsive even as concurrency rises and request shapes vary.
Deployed alongside Vera Rubin NVL72, LPX accelerates the latency-sensitive portions of the decode loop, including FFN and MoE expert execution, while Rubin GPUs continue to handle prefill and decode attention. Together, they deliver a heterogeneous serving path that improves interactive responsiveness without sacrificing AI factory throughput.
At rack scale, LPX delivers:
| Specification | NVIDIA Groq 3 LPX |
| AI inference compute | 315 PFLOPS |
| Total SRAM capacity | 128 GB |
| On-chip SRAM bandwidth | 40 PB/s |
| Scale-up density | 256 chips |
| Scale-up bandwidth | 640 TB/s |
Vera Rubin NVL72 and LPX create a more heterogeneous inference architecture for the AI factory—one that can support high aggregate token production and responsive interactive AI experiences.
Inside the NVIDIA Groq 3 LPX compute tray
The LPX rack-scale accelerator houses 32 liquid-cooled 1U compute trays, each designed to support low-latency inference at scale. Every tray integrates eight LPU accelerators, a host processor, and fabric expansion logic in a cableless design that simplifies rack-scale deployment and tightly couples compute with communication.
LPU chip-to-chip (C2C) links provide direct communication within the tray, across trays via the LPU C2C spine, and across racks as systems scale. Connectivity is important because interactive inference isn’t just about raw compute. It also depends on how efficiently the system can move data, coordinate work, and avoid variable delays as requests flow across devices.
Each tray provides:
| Resource | Per LPX Tray |
| LP30 chips | 8 |
| On-chip SRAM | 4 GB |
| SRAM bandwidth | 1.2 PB/s |
| DRAM via fabric expansion logic | Up to 256 GB |
| DRAM via host CPU | Up to 128 GB |
| AI inference compute (FP8) | 9.6 PFLOPS |
| Scale-up bandwidth | 20 TB/s |
At the system level, LPX is built for inference regimes where coordination overhead and jitter can quickly become visible to users. This is especially relevant as more AI applications move away from offline or throughput-oriented serving and toward interactive generation. To see how LPX is optimized for that regime, it helps to look at the processor architecture at the core of the system: the NVIDIA Groq 3 LPU.
First look at the architecture of the NVIDIA Groq 3 LPU—the seventh chip of the Vera Rubin Platform
At the heart of LPX is the NVIDIA Groq 3 LPU, designed to deliver fast, predictable token generation by tightly coupling compute, memory, and communication under compiler control. The architecture of the LPU is designed to deliver fast, predictable token generation by tightly coupling compute, memory, and communication under compiler control. Rather than optimizing only for peak arithmetic throughput, the LPU emphasizes deterministic execution, high on-chip memory bandwidth, and explicit data movement. These capabilities are especially important for decode-dominant, latency-sensitive inference regimes.
Tensor-first compute and explicit data movement
Compute and communication in the LPU are organized around 320-byte vectors as the unit of work. Arithmetic operations, memory access, and inter-device transfers all operate on these fixed-size vectors, simplifying scheduling and synchronization.
Specialized execution modules handle different classes of operations:
- Matrix execution modules (MXM) provide dense multiply-accumulate capability for tensor operations, operating on fixed data types with predictable throughput.
- Vector execution modules (VXM) handle pointwise arithmetic, type conversions, and activation functions using a mesh of arithmetic logic units (ALUs) per lane.
- Switch execution modules (SXM) perform structured data movement, including permutation, rotation, distribution, and transposition of vectors.
By making data movement explicit and programmable, the LPU enables memory access, compute, and communication to be overlapped, rather than relying on hardware heuristics.
MEM enables extreme on-chip memory bandwidth
A central element of the LPU is the MEM block—a flat, SRAM-first memory architecture where 500 MB of high-speed on-chip SRAM serves as the primary working storage for inference. Rather than relying on hardware-managed caches, the compiler and runtime place the active working set, including weights, activations, and KV state, into on-chip memory and move data explicitly. This reduces unpredictable stalls and helps deliver low, stable latency by keeping the most latency-sensitive data close to compute.
Because on-chip SRAM capacity is finite, larger models are scaled across many interconnected LPU accelerators using parallel execution strategies such as layer-wise partitioning, so the overall system presents a much larger effective working set. In this design, performance is governed less by peak arithmetic throughput and more by how consistently the system can keep compute fed, which is why the LPX pairs 150 TB/s of on-chip memory bandwidth with high bandwidth scale-up chip-to-chip (C2C) communication per LPU.
C2C scaling with predictable communication
To scale inference across multiple devices, the LPU includes high-radix, high-speed C2C links designed for deterministic data exchange. Each LPU connects through 96 C2C links running at 112 Gbps each, enabling a streamlined LPX scale-up topology with high aggregate I/O bi-directional bandwidth of 2.5 TB/s and predictable communication timing. This is especially important for distributed inference pipelines, where communication overhead can otherwise become a major source of latency.
Deterministic, compiler-orchestrated execution
The LPU builds on Groq’s spatial execution model, where the compiler explicitly schedules computation, data movement, and synchronization. Instead of relying on dynamic hardware schedulers at runtime, the compiler relies on plesiosynchronous, chip-to-chip protocol in hardware that cancels natural clock drift and aligns hundreds of LPU accelerators to act as a single coordinated system. With predictable data arrival and periodic software synchronization, developers can reason more directly about timing, and the system can coordinate both compute and network behavior with much greater determinism.
This execution model enables:
- Precise coordination between memory and compute.
- Explicit control over instruction timing.
- Reduced execution jitter under variable workloads
For real-time inference, this determinism helps keep time-to-first-token and per-token latency stable, even at small batch sizes.
The shift toward interactive inference
AI inference spans a broad performance spectrum. On one end are throughput-optimized services such as batch document processing, moderation, embeddings, and media pipelines, where the goal is to maximize tokens per GPU, tokens per watt, or overall cost efficiency. These workloads often support large-scale shared services, including free-tier and background AI offerings, where high utilization matters more than per-user responsiveness.
On the other end are latency-optimized services such as coding assistants, chatbots, voice assistants, copilots, and interactive agents, where delays are immediately visible to users. In these workloads, the most important metrics are time-to-first-token, tokens per second per user, and tail latency. Many modern AI platforms must support both regimes simultaneously, running high-throughput backends for large-scale processing while delivering responsive interactive experiences. This divergence is one reason heterogeneous inference architectures are becoming increasingly important.
What makes interactive inference harder
Several trends are making low-latency interactive inference both more important and harder to serve efficiently, as shown in Table 3. As models produce longer outputs and context windows grow, more of the workload shifts into decode, where tokens are generated sequentially, and responsiveness is exposed directly to the user.
| Force | Why it matters |
| Low-latency as a product feature | In interactive applications, responsiveness is no longer just an infrastructure metric; it is part of what users evaluate. |
| Longer reasoning outputs | As models generate longer outputs and multi-step chains of thought, more of the request shifts into sequential token generation. |
| Prefix caching | Reusing shared prompt state can reduce prefill cost, but it also increases the relative share of request-specific decode work that still has to be served quickly. |
| Longer contexts | As context grows, the Transformer’s self-attention mechanism becomes increasingly constrained by data movement and memory bandwidth. |
At the same time, longer contexts increase pressure on memory bandwidth and data movement, while serving many concurrent users reduces the batching efficiency that throughput-oriented systems rely on. As a result, systems optimized for maximum aggregate throughput are not always the best fit for workloads that require fast, predictable token generation for each request.
This challenge becomes even more pronounced in agentic AI, where systems repeatedly cycle through inference, retrieval, tool use, and reasoning. In these loops, latency compounds across each step, making stable per-token performance and strong tail-latency behavior critical for responsive user experiences.
The era of agentic inference requires a new architecture
Inference isn’t a single, uniform workload. Within a request, prefill and decode place different demands on hardware, and those demands shift with batch size, context length, and model structure. Some phases, including self-attention and sparse MoE, can become highly sensitive to memory bandwidth and data movement, while others, such as dense projection and feed-forward layers, scale efficiently on throughput-optimized hardware when enough parallelism is available. In interactive decode, many operations run at very small batch sizes, making latency much more sensitive to stalls, contention, and jitter.
Optimizing the entire pipeline for only one regime forces a compromise. Hardware tuned for peak throughput under large batches isn’t ideal for the most latency-sensitive execution paths, while hardware optimized for low-latency execution is less efficient for the most compute-intensive phases.
As shown in Figure 4, a heterogeneous system combines both approaches, pairing low-latency interactive performance with high AI factory throughput. The result is a two-engine architecture: GPUs deliver high output for context-heavy prefill and execute decode attention, while LPUs accelerate latency-sensitive decode components such as FFN/MoE execution. Together, they improve interactivity without giving up AI factory throughput.
Vera Rubin NVL72 meets LPX
Modern inference is a relay race. The same hardware that runs the heavy context leg doesn’t need to anchor the sprint to the next token. Rubin GPUs are the flexible, general-purpose workhorses for training and inference. They deliver high throughput across many model sizes, batch regimes, and serving patterns, from long-context prefill to decode attention and high-concurrency inference at scale.
LPX adds a specialized path optimized for fast, latency-sensitive token generation. Together, they enable a heterogeneous inference design that improves interactive responsiveness without giving up system-scale efficiency.
Decode phase: A repeated multi-engine loop
The prefill phase is dominated by ingesting large inputs and building the KV cache—a workload that benefits from dense parallel compute and large memory capacity. The Vera Rubin NVL72 handles this phase efficiently, especially for long-context workloads and MoE models where context can be large and highly variable.
The decode phase is different. Decode is a repeated per-token loop, and different parts of that loop stress different bottlenecks. In the Vera Rubin platform architecture with LPX, decode is best thought of as a two-engine loop. GPUs handle decode work that benefits most from throughput and large memory capacity, such as full-context attention over the accumulated KV cache. LPX accelerates latency-sensitive execution within decode, such as sparse MoE expert feed-forward networks (FFNs) and other pointwise operations. This split, often described as decode phase disaggregation or attention–FFN disaggregation (AFD), separates attention from FFN within decode and exchanges intermediate activations for each token, so each engine runs the part of the loop it is best suited to execute. This AFD loop expands the highest-value operating region of the Pareto frontier.
At rack scale and beyond, the LPX is designed to operate as a tightly coordinated unit of compute, minimizing coordination overhead and reducing jitter. This is valuable in decode-heavy, agentic workflows where small delays compound across many model calls and verification loops.
NVIDIA Dynamo makes heterogeneous decode operational
Making heterogeneous decode practical requires software that can classify requests, route work by latency targets, move intermediate activations with low overhead, and keep tail latency stable under bursty, variable traffic. NVIDIA Dynamo provides that orchestration layer by coordinating disaggregated serving and disaggregated decode across heterogeneous backends.
In practice, Dynamo routes prefill to GPU workers to process the large context and build the KV cache. During decode, Dynamo orchestrates the AFD loop where GPUs run attention over the accumulated KV cache, intermediate activations are handed off to LPUs for FFN/MoE execution, and outputs return to the GPUs to continue token generation. The result is a single coherent serving path with more predictable tail latency while sustaining high AI factory throughput.
With KV-aware routing, low-overhead transfers, and latency-target-driven scheduling, Dynamo helps keep interactive sessions out of long queues, reduces cross-tenant jitter, and maintains stable tail latency as concurrency and request shapes vary. The result is a production-ready heterogeneous serving model that delivers responsive user experiences while sustaining high AI factory throughput at scale.
Accelerating speculative decoding with LPX
Speculative decoding is an increasingly important technique for reducing latency in LLM inference. The approach uses a smaller draft model to generate multiple candidate tokens ahead of time, while a larger target model verifies and accepts those tokens in parallel. When the predictions match, multiple tokens can be committed at once, significantly increasing effective tokens per second and reducing response latency.
LPX is well-suited to act as the draft-generation engine in this architecture. The deterministic execution model and extremely high on-chip SRAM bandwidth of the LPU enable very fast draft token generation, enabling the draft model to run ahead of the verifier. At the same time, GPUs such as Rubin remain highly efficient for large-model execution tasks such as prefill, attention processing, and token verification.
By pairing the two, the system combines the strengths of both processors:
- LPX generates draft tokens rapidly using its low-latency architecture.
- Rubin GPUs verify and finalize tokens efficiently using high-throughput compute and large memory capacity.
This separation enables speculative decoding to run across heterogeneous processors, rather than running both draft and verifier models on the same hardware. The result is a system that can deliver faster draft generation without sacrificing the efficiency of GPU-based verification.
Unlocking intelligent agentic swarms
As AI use cases evolve from simple chat and batch inference to multi-step agentic workflows, responsiveness becomes a requirement. Offline inference and basic assistants can often prioritize aggregate throughput, but interactive applications, deep research, and agentic pipelines combine high token volume with tight feedback loops, where latency compounds across many model calls and tool interactions.
In this regime, heterogeneous inference matters. Pairing a high-throughput engine for long-context processing with a low-latency engine for decode FFNs makes it possible to increase user interactivity without sacrificing AI factory output.
Unlocking a new category of AI experiences on the Pareto frontier
A practical way to visualize this tradeoff between performance and cost is the Pareto frontier, plotting user interactivity, measured in tokens per second per user (TPS per user), on the horizontal axis against AI factory throughput, measured in tokens per second per megawatt (TPS per MW), on the vertical axis.
As shown in Figure 10, different AI services operate at very different points on this curve. Throughput-first services, including many free-tier and background workloads, typically prioritize maximum efficiency and high utilization and often use smaller models with shorter context windows. Premium AI services, by contrast, demand higher model capability and far more responsive user-visible performance, especially for long-context reasoning and agentic workflows. In Figure 10, that premium tier is represented by a 2-trillion-parameter MoE model with a 400K input context window operating at roughly 400 TPS per user and beyond.
Reaching these premium operating points with a single homogeneous platform forces a tradeoff between responsiveness and overall AI factory throughput because the workload mixes fundamentally different performance regimes within the same serving pipeline. A heterogeneous architecture expands the achievable region by combining complementary execution paths, allowing the system to sustain high factory output while delivering highly responsive, low-latency interactive experiences. As illustrated in Figure 10, the combination of Vera Rubin NVL72 and LPX delivers up to 35x higher TPS per megawatt at 400 TPS per user compared with the NVIDIA GB200 NVL72, effectively creating a new premium performance tier for interactive AI services.
This shift has a direct economic impact. Higher responsiveness expands the set of premium experiences an AI factory can serve and increases value per unit of infrastructure. With the Vera Rubin platform, AI factories can unlock up to 5x more revenue per megawatt compared with the GB200 NVL72, and up to 10x by pairing Vera Rubin NVL72 with LPX for the most latency-sensitive, high-value interactive workloads, such as agentic coding and multi-agent systems.
What NVIDIA Groq 3 LPX enables for Developers
Developers are increasingly building systems that require three things at once:
- Responsiveness: low and predictable latency for interactive experiences and agent loops.
- Capability: strong model quality, reasoning depth, and long-context understanding.
- Scale: high-throughput and cost efficiency to serve many concurrent users or agents.
LPX broadens the set of workloads an AI factory can serve efficiently. Use the low-latency path where predictable token generation improves experience, such as coding assistants, agentic workflows with tight tool-calling loops, voice interactions, and real-time translation. Keep throughput-first workloads on Rubin GPUs, such as batch serving, long-context throughput runs, where high concurrency and batching keep GPUs consistently busy and cost-efficient. The operational shift is mindset. Stop optimizing for one headline metric and start optimizing for a range of real-world operating points.
Learn more
Dive deeper into the architecture behind NVIDIA Groq 3 LPX and Vera Rubin by starting with the NVIDIA product pages and technical blogs covering the Vera Rubin platform, LPX, AFD, and Dynamo. Explore the underlying research on tensor streaming processors and software-defined silicon design for AI. Together, these resources offer a deeper look at the hardware, system architecture, and orchestration software behind heterogeneous, low-latency inference at scale. Next, join a NVIDIA Developer Forum thread focused on inference and deployment to compare notes with other teams building low-latency serving systems.
Resources
- NVIDIA LPX page
- Press Release: NVIDIA Vera Rubin Opens Agentic AI Frontier
- Tech Blog: Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer
- Tech Blog: NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer
- Tech Blog: Announcing NVIDIA Dynamo 1.0: Scaling MultiNode Inference in Production
- Video: The Future of AI Inference – Explainer on Attention-FFN Disaggregation AFD (starting at 18:00)
- Tech Blog: NVIDIA Vera CPU Delivers High Performance, Bandwidth, and Efficiency for AI Factories
- Research Paper: Think Fast: A Tensor Streaming Processor (TSP) for Accelerating Deep Learning Workloads
- Research Paper: A Software-defined Tensor Streaming Multiprocessor for Large-scale Machine Learning
- Video: Enabling PyTorch’s Thousand Ops for Software First Silicon Design
Acknowledgments
Thanks to Amr Elmeleegy, Andrew Bitar, Andrew Ling, Graham Steele, Itay Neeman, Jamie Li, Omar Kilani, Santosh Raghavan, and Stuart Pitts, along with many other NVIDIA product leaders, engineers, and architects who contributed to this post.
