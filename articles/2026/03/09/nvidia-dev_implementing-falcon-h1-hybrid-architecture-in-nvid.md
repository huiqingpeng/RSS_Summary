---
title: "Implementing Falcon-H1 Hybrid Architecture in NVIDIA Megatron Core"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/implementing-falcon-h1-hybrid-architecture-in-nvidia-megatron-core/"
published: "2026-03-09"
fetched: "2026-03-10T11:21:42.693874"
---

In the rapidly evolving landscape of large language model (LLM) development, NVIDIA Megatron Core has emerged as the foundational framework for training massive transformer models at scale. The open source library offers industry-leading parallelism and GPU-optimized performance. Now developed GitHub-first in the NVIDIA/Megatron-LM repo, Megatron Core is increasingly shaped by contributions from foundation model builders, making it a more flexible, future-proofed engine for open AI models.
This post provides a technical overview of how the Technology Innovation Institute (TII), creators of the Falcon model family, have contributed to and integrated with Megatron Core and Megatron Bridge frameworks. The first section examines the implementation of the Falcon-H1 parallel hybrid architecture within Megatron Bridge, highlighting the challenges of coordinating heterogeneous Transformer and Mamba layers alongside non-learnable µP multipliers. The second section explores the integration of BitNet into Megatron Core, detailing the replacement of standard linear layers with ternary-parameter counterparts and the implications for training efficiency and scalability.
These contributions demonstrate how Megatron Core users can extend the framework to support their own custom model architectures and complex training features and leverage the work of others in the community.
Falcon-H1 hybrid architecture integration in Megatron Bridge
The implementation of the Falcon-H1 parallel hybrid architecture within Megatron Bridge highlights the challenges of coordinating heterogeneous Transformer and Mamba layers alongside non-learnable µP multipliers. Details of this integration are provided in the following sections.
Hybrid parallel design
At the core of the TII contributions to Megatron is the Falcon-H1 parallel hybrid architecture. The design diverges from the sequential layering found in other recent hybrid models. As shown in Figure 1, within each block, the attention mechanism and the SSM operate in parallel, and their outputs are concatenated before being passed through the block’s output projection. The number of SSM and attention heads is configurable and can be adjusted as needed.
Instead of stacking distinct layers, Falcon-H1 adopts a parallel design in which transformer-based attention and Mamba-2 state-space model (SSM) components process the input simultaneously within each core processing block.
The outputs from the attention and Mamba branches are concatenated prior to projection, allowing the model to fuse the superior long-context memory and efficiency of SSMs with the long-range dependency modeling of attention.
The ratio of parallel hybrid layers, pure Mamba layers, attention-only layers, and multilayer perceptron (MLP)-only layers within the model can be configured independently, enabling flexible architecture exploration.
Two-repo integration
The Falcon-H1 support spans two repositories with distinct responsibilities. In Megatron Core (Megatron-LM), TII contributed:
- The foundational
ParallelHybridLayer
, a layer that runs Mamba and attention in parallel and sums their outputs - The updated layer allocation logic that introduces the
PARALLEL
symbol alongside existing Mamba, attention, and MLP layer types.
This also includes checkpoint conversion tools for loading and saving parallel hybrid models. In Megatron Bridge, TII built the complete Falcon-H1 model on top of these primitives:
- The
FalconH1Layer
extends the parallel design to include an MLP component (forming the full Mamba plus attention plus MLP block) - The
FalconH1Bridge
provides bidirectional Hugging Face to Megatron weight conversion with specialized mappings for Mamba and attention parameters - The
FalconH1ModelProvider
(with size-specific variants for 0.5B, 1.5B-Deep, 7B, and 34B) encapsulates all model configurations, including forward µP non-learnable multipliers
Integrating this hybrid design into the Megatron ecosystem required TII to address significant engineering challenges through several key architectural innovations, as detailed below.
Layer spec unification
Megatron Core uses ModuleSpec
to define layer configurations. For Falcon-H1, this required extending MambaStackSubmodules
to hold separate specs for mamba_layer
, attention_layer
, mlp_layer
, and the new parallel_hybrid_layer
. The MambaStack
module iterates through a layer type list and builds the appropriate module for each position.
In Megatron Bridge, a corresponding FalconH1StackSubmodules
adds a falconh1_layer
spec that bundles all three components. This enables developers to mix and match Mamba and Transformer components within a single model definition.
Weight mapping for checkpoint conversion
In Megatron Bridge, converting Hugging Face checkpoints to Megatron format requires specialized parameter mappings. The MambaInProjMapping
class handles the complex splitting of Mamba in_proj
weights into z, x, B, C, and dt components. These components must be correctly distributed across tensor parallel ranks while preserving numerical correctness.
The FalconH1Bridge
manages tensor parallel resharding for both Mamba and Attention layers in a single pass, alongside QKVMapping
for fusing separate Q, K, and V projections and GatedMLPMapping
for combining gate and up projections. In Megatron Core, the checkpoint conversion tools (loader_parallelhybrid
and saver_parallelhybrid_hf
) handle the translation between the Megatron distributed format and Hugging Face FalconH1ForCausalLM
.
Tensor parallelism for SSM layers
Mamba layers have unique tensor parallel requirements. The A_log
, D
, and dt_bias
tensors split along dimension 0, while x_proj
splits along dimension 1. For Mamba-2, the in_proj
and conv1d
layers require special handling to correctly partition the z, x, B, C, and dt components across ranks.
Beyond classical μP
To optimize Falcon-H1 series, TII employed customized maximal update parametrization (μP). While classical μP is rooted in neural network theory to enable effortless hyperparameter transfer from a base model size to larger models, Falcon-H1 extends this by tuning μP multipliers themselves. This enables each component to train at the correct intensity.
Training spikes that are common in SSM-based models are addressed by applying dampening multipliers within the SSM block, leading to smoother training and cleaner experimental signals.
The µP multipliers in Falcon-H1 are stored as non-learnable tensors. They scale activations during the forward pass without accumulating gradients. This approach keeps memory overhead minimal while enabling fine-grained control over learning dynamics across 12 distinct scaling factors covering embeddings, attention, SSM, and MLP components.
For Megatron Bridge, this required adding multiplier extraction during Hugging Face checkpoint loading. The bridge reads multiplier values from the HF config and applies them at the correct forward pass locations. Both attention and Mamba components receive their respective scaling factors.
BitNet integration for Falcon Edge in Megatron Core
Falcon Edge is a series of ternary (1.58-bit) TII language models based on the BitNet architecture. To train Falcon Edge at scale, TII contributed BitNet pretraining support for GPT-like architectures to Megatron Core. This integration is a key step toward enabling scalable pretraining workflows with 1-bit LLMs, while preserving Megatron parallelism and performance characteristics.
TII introduced two new parallel linear layers: BitNetColumnParallelLinear
and BitNetRowParallelLinear
. These layers mirror existing Megatron tensor-parallel linear layers, but incorporate BitNet quantization logic. By embedding BitNet directly at the layer-spec level, the integration remains compatible with Megatron tensor parallelism, pipeline parallelism, and distributed training infrastructure.
Under the hood, the implementation leverages onebitllms
Triton kernels for efficient activation and weight quantization.
During the forward pass, BitNet replaces full-precision matrix multiplications with quantized equivalents:
- Weights are quantized to ternary values {−1, 0, +1} using absolute mean scaling. The weight tensor is scaled by the reciprocal of its absolute mean, then rounded and clamped to {−1, 0, +1}.
- Activations are quantized to 8-bit precision using per-token
absmax
scaling. For each token, the maximum absolute value across the hidden dimension is computed, used to scale the activations into the [−128, 127] range, and the result is rounded to the nearest integer. - The core linear operations are performed using these quantized weights and activations, leveraging the custom Triton kernels provided by
onebitllms
for optimization. - By utilizing ternary weights (1.58-bit), the model significantly reduces its memory footprint and enables faster inference speeds compared to full-precision counterparts.
During the backward pass:
- Gradients bypass the nondifferentiable quantization functions, enabling backpropagation to proceed as if the quantization step were an identity function.
- Weight gradients are computed on the full-precision weights. Quantization is applied only during the forward pass, ensuring optimizer updates remain high fidelity.
- Activation gradients follow standard backpropagation through quantization-aware layers.
Implementation
The BitNet integration in Megatron Core introduces minimal changes while maintaining full compatibility with existing parallelism strategies, and Megatron Core scalability. Standard Linear layers are replaced with BitNetLinear
variants, enabling ternary weight quantization while maintaining Megatron Core layer interfaces.
Activation and weight quantization kernels are integrated directly into the Megatron computation pipeline. Tensor parallelism is extended to support sharded quantized weights, with scaling factors handled per shard to preserve numerical correctness. Megatron fused kernels and communication patterns are retained, ensuring that ternary quantization delivers memory and bandwidth savings without sacrificing throughput.
Core components
- Custom linear layers: Two new classes extend Megatron tensor-parallel layers:
BitNetColumnParallelLinear
extendsColumnParallelLinear
BitNetRowParallelLinear
extendsRowParallelLinear
- Quantization integration: Both layers
override _forward_impl
to apply ternary weight quantization and 8-bit activation quantization usingonebitllms
Triton kernels (weight_quant_triton
andactivation_quant_triton
) - Straight-through estimator (STE): Gradients bypass quantization using the pattern x_quantized = x + (quant(x) – x).detach().
This allows backpropagation through nondifferentiable quantization while maintaining full-precision weight updates.
Integration points
- Layer specification system: BitNet layers are registered in
get_gpt_layer_local_spec
andget_mlp_module_spec
, enabling activation through the--use-bitnet
flag - Tensor parallelism: Quantization is applied independently on each tensor-parallel shard after weights are partitioned, preserving numerical correctness across distributed computations
- Training requirements: BitNet requires
--transformer-impl
local and theonebitllms
package. The implementation reuses existing Megatron communication patterns and fused kernels without modification
The integration delivers significant weight memory savings and bandwidth improvements while maintaining compatibility with Megatron pipeline parallelism, gradient accumulation, and optimizer infrastructure.
Get started building foundation models with Megatron
TII Falcon-H1 hybrid architecture and BitNet ternary training support show how foundation model builders can extend Megatron Core and Megatron Bridge for their own architectures and training needs. These contributions are currently available.
To get started in Megatron-LM, check out BitNet pretraining and ParallelHybrid layer support. To get started in Megatron-Bridge, check out Falcon-H1 checkpoint conversion and µP multiplier handling.
