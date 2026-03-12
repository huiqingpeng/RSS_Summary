---
title: "Build Next-Gen Physical AI with Edge‑First LLMs for Autonomous Vehicles and Robotics"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/build-next-gen-physical-ai-with-edge%e2%80%91first-llms-for-autonomous-vehicles-and-robotics/"
published: "2026-03-12"
fetched: "2026-03-13T07:04:56.264882"
---

Physical AI is rapidly evolving, from next-generation software-defined autonomous vehicles (AVs) to humanoid robots. The challenge is no longer how to run a large language model (LLM), but how to enable high-fidelity reasoning, real-time multimodal interaction, and trajectory planning within strict power and latency envelopes.
NVIDIA TensorRT Edge-LLM, a high-performance C++ inference runtime for LLMs and vision language models (VLMs) on embedded platforms, is designed to overcome these challenges.
As explained in this post, the latest TensorRT Edge-LLM release delivers a significant expansion in fundamental capabilities for NVIDIA DRIVE AGX Thor and NVIDIA Jetson Thor platforms. It introduces advanced edge architectures, including mixture of experts (MoE), the NVIDIA Cosmos Reason 2 open planning model for physical AI, and Qwen3-TTS and Qwen-ASR models for embedded speech processing. Building on these foundational pillars, the release also offers optimized support for the NVIDIA Nemotron family of open models. This provides developers with the essential runtime to build the next generation of autonomous machines.
Efficient reasoning at scale
Running massive models on embedded hardware requires a rethink of compute efficiency. The latest release of TensorRT Edge-LLM fully enables MoE support at the edge, specifically optimizing models like Qwen3 MoE. By activating only a subset of expert parameters per token, MoE architectures enable edge devices to access the reasoning capabilities of a massive model while maintaining the inference latency and active compute footprint of a much smaller one.
This architectural shift is critical for deploying high-fidelity reasoning on edge platforms like NVIDIA DRIVE AGX Thor and NVIDIA Jetson Thor. As a developer, you can drastically scale up the intelligence of your autonomous systems without exceeding the strict power and latency limits required for real-time, mission-critical operations.
Unlock hybrid reasoning at the edge
TensorRT Edge-LLM is a specialized runtime to fully support NVIDIA Nemotron 2 Nano. This enables a new class of System 2 reasoning directly on embedded chipsets, including NVIDIA DRIVE Thor and Jetson Thor.
For developers building advanced in-cabin AI assistants or robotic dialogue agents, deploying highly capable language models at the edge presents a significant memory and latency challenge. Nemotron 2 Nano addresses this challenge fundamentally by utilizing a novel Hybrid Mamba-2-Transformer architecture. This significantly reduces the memory footprint from KV cache storage with Mamba State Space architectures while maintaining high-fidelity precision from attention layers.
TensorRT Edge-LLM bridges the deployment gap by providing optimized kernels that accelerate these specific hybrid layers. This enables developers to use the model’s massive context window for complex edge retrieval-augmented generation (RAG) pipelines or agentic workflows while maintaining a strict, production-viable device memory footprint.
By enabling dynamic “thinking” at the edge with TensorRT Edge-LLM, developers can leverage a model’s ability to shift seamlessly between deep reasoning and immediate conversational action. This is a critical capability for advanced in-cabin assistants and robotic agents that must reason through complex user queries one moment and provide conversational responses the next.
- Deep reasoning mode (
/think
): TensorRT Edge-LLM efficiently handles the expanded token generation required for chain of thought (CoT) processing. By using the/think
system prompt, the runtime enables the model to think through complex logic, achieving a remarkable 97.8% on MATH500—before outputting a decision. - Conversational reflex mode (
/no_think
): For latency-critical voice interactions where the user expects an immediate reply, developers can issue a/no_think
command. TensorRT Edge-LLM optimizes this path to bypass reasoning traces, delivering immediate, intelligent responsiveness required for seamless conversational AI and agile on-device agents.
By supporting this hybrid architecture, TensorRT Edge-LLM enables compact, production-ready VLMs and LLMs to serve as both reasoned assistants and low-latency conversational agents, significantly reducing the memory constraints of physical AI.
Real-time multimodal interaction at the edge
TensorRT Edge-LLM now offers support for Qwen3-TTS and Qwen3-ASR, a native multimodal model with Thinker-Talker architecture capable of voice interaction. Unlike traditional pipelines that cascade ASR, LLM, and TTS models, adding latency at every hop, Qwen3-TTS/ASR handles end-to-end speech processing.
By optimizing both the Thinker and Talker components, TensorRT Edge-LLM enables low-latency, natural voice synthesis directly on the chip:
- Thinker: TensorRT Edge-LLM accelerates the reasoning core, allowing the model to process complex driver queries and environment context to generate intelligent, reasoned responses.
- Talker: TensorRT Edge-LLM complements the reasoning engine by delivering low latency, natural voice synthesis (TTS) directly on the chip.
In the case of AVs, this allows for seamless, interruptible conversations between the driver and the vehicle.
Equipping humanoid robotics with physical common sense
For humanoid robots and advanced vision agents, understanding the real world requires more than just identifying objects; it requires an intuitive grasp of physics and time. To meet this need, TensorRT Edge-LLM now supports Cosmos Reason 2, an open, customizable reasoning VLM purpose-built for physical AI and robotics.
Cosmos Reason 2 empowers embodied agents to reason like humans by using prior knowledge, physical common sense, and chain-of-thought capabilities to understand world dynamics without human annotations. With TensorRT Edge-LLM optimized, low-latency runtime, robots at the edge can efficiently leverage Cosmos Reason 2 as a primary planning model to reason through their next steps.
Key capabilities of Cosmos Reason 2 accelerated by TensorRT Edge-LLM include:
- Advanced spatio-temporal reasoning: Enhanced physical AI reasoning with improved timestamp precision and a deep understanding of space, time, and fundamental physics.
- 3D localization and explanation: The ability to not only detect objects but also provide 2D and 3D point localization, bounding-box coordinates, and contextual reasoning explanations for its labels.
- Massive context processing: Support for an improved long-context window of up to 256K input tokens, allowing edge agents to ingest extensive environmental and historical data.
By supporting Cosmos Reason 2, TensorRT Edge-LLM ensures that next-generation robots can continuously evaluate complex, long-tail physical scenarios and safely plan their actions in real time.
Advancing autonomous driving with end-to-end trajectory planning
Among the most significant shifts in autonomous production is the move from traditional modular stacks to end-to-end VLA models. NVIDIA Alpamayo is a family of open AI models, simulation frameworks, and physical AI datasets designed to accelerate the development of safe, transparent, and reasoning-based AVs.
Stay tuned for the forthcoming Alpamayo 1 workflow, a distillation recipe that brings System 2 rational thinking to the edge. Alpamayo 1 represents a leap forward from standard VLMs. It is not just describing a scene; it is planning a precise trajectory through it. The architecture utilizes a Cosmos Reason Backbone (distilled) to generate a chain of causation (reasoning trace) before outputting actions.
Key features of the Alpamayo integration in TensorRT Edge-LLM include:
- Flow matching trajectory decoding: Moving beyond simple regression, flow matching is used to generate diverse, high-fidelity future trajectories.
- History and context: The model tokenizes two-second historical trajectories and multicamera inputs, processing them through a Qwen3-VL backbone to output explainable driving decisions. For example, “Nudge to the left to increase clearance.”
- Performance: On DRIVE Thor, Alpamayo 1 achieves production-viable latencies, using FP8 acceleration for the Vision Transformer (ViT) components.
Get started with TensorRT Edge-LLM for physical AI
TensorRT Edge-LLM serves as the go-to-open-source, pure C++ inference runtime designed specifically for the mission-critical needs of automotive and robotics. It eliminates Python dependencies for deployment, ensuring predictable memory footprints.
From deploying the efficient expert routing of Qwen3 MoE today, to preparing for the future distilled reasoning of Alpamayo 1, NVIDIA provides the essential runtime to build the next generation of autonomous machines.
To get started, explore the new features, including the Alpamayo and MoE examples, in the updated TensorRT Edge-LLM GitHub repo or through the latest NVIDIA DriveOS releases.
