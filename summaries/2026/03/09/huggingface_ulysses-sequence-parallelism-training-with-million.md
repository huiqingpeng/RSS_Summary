---
title: "Ulysses Sequence Parallelism: Training with Million-Token Contexts"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/ulysses-sp"
published: "2026-03-09"
summarized: "2026-03-10T12:53:09.627898"
ai_provider: "openai"
---

【是什么 / What it is】

Ulysses Sequence Parallelism 是一种分布式训练技术，由 DeepSpeed 提出并被 Snowflake AI Research 纳入其 Arctic Long Sequence Training (ALST) 协议，现已在 Hugging Face 生态系统中全面集成（包括 Accelerate、Transformers Trainer 和 TRL）。它通过将注意力头的计算分布到多个 GPU 上，解决了训练大语言模型时百万级 token 长序列的内存瓶颈问题。

Ulysses Sequence Parallelism is a distributed training technique introduced by DeepSpeed and adopted by Snowflake AI Research's Arctic Long Sequence Training (ALST) protocol, now fully integrated across the Hugging Face ecosystem (Accelerate, Transformers Trainer, and TRL). It addresses the memory bottleneck of training large language models on million-token sequences by distributing attention head computations across multiple GPUs.

---

【为什么重要 / Why it matters】

随着 AI 系统需要处理整本书籍、大型代码库、复杂推理链和 RAG 检索文档等任务，长序列训练已成为构建能力更强的模型的关键需求。传统数据并行无法解决注意力计算的二次方复杂度问题，而 Ulysses 以相对较低的通信开销（相比 Ring Attention 减少 h 倍通信量）实现了高效的序列并行，使得在消费级硬件上训练 128k+ token 的模型成为可能。

As AI systems increasingly need to process entire books, large codebases, complex reasoning chains, and RAG-retrieved documents, long-sequence training has become essential for building more capable models. Traditional data parallelism cannot address the quadratic complexity of attention computation, while Ulysses achieves efficient sequence parallelism with relatively low communication overhead (h times less communication than Ring Attention), making it feasible to train on 128k+ token contexts with commodity hardware.

---

【我能用什么 / How I can use it】

你可以通过三种方式立即使用：使用 `Accelerate` 的 `ParallelismConfig` 进行底层控制，通过 `Transformers Trainer` 的 `TrainingArguments.parallelism_config` 实现无缝集成，或直接使用 `TRL` 的 `SFTTrainer`。关键配置参数包括 `sp_size`（并行 GPU 数量）、`sp_backend="deepspeed"` 和注意力实现方式（推荐 FlashAttention 2/3）。最佳实践建议：确保 `dp_replicate × dp_shard × sp_size = num_processes`，对变长序列启用 `sp_seq_length_is_variable=True`，并注意使用 `position_ids` 而非 4D `attention_mask` 进行因果掩码。

You can start using it through three paths: `Accelerate`'s `ParallelismConfig` for low-level control, `Transformers Trainer`'s `TrainingArguments.parallelism_config` for seamless integration, or `TRL`'s `SFTTrainer` directly. Key configuration parameters include `sp_size` (number of parallel GPUs), `sp_backend="deepspeed"`, and attention implementation (FlashAttention 2/3 recommended). Best practices: ensure `dp_replicate × dp_shard × sp_size = num_processes`, enable `sp_seq_length_is_variable=True` for variable-length sequences, and use `position_ids` instead of 4D `attention_mask` for causal masking.
