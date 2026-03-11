---
title: "Introducing Storage Buckets on the Hugging Face Hub"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/storage-buckets"
published: "2026-03-10"
summarized: "2026-03-11T09:05:01.728106"
ai_provider: "openai"
---

【是什么 / What it is】

Hugging Face Hub 推出了 Storage Buckets，这是一种基于 Xet 技术构建的可变、类 S3 的对象存储服务，专门用于解决生产级机器学习中的中间文件存储问题——如训练检查点、优化器状态、处理后的数据分片、日志和追踪记录等。与 Git 版本控制的模型和数据集仓库不同，Buckets 提供非版本化的快速读写、覆盖和同步能力，可通过浏览器、Python API 或 hf CLI 进行管理。

Hugging Face Hub has launched Storage Buckets, a mutable, S3-like object storage service built on Xet technology, designed specifically for intermediate files in production ML—such as training checkpoints, optimizer states, processed data shards, logs, and traces. Unlike Git-versioned model and dataset repos, Buckets provide non-versioned fast read/write, overwrite, and sync capabilities, manageable via browser, Python API, or the hf CLI.

---

【为什么重要 / Why it matters】

生产级机器学习产生大量频繁变化、无需版本控制的中间产物，传统 Git 架构在此场景下效率低下；Storage Buckets 通过 Xet 的块级去重技术显著减少带宽和存储成本，并支持"预预热"功能将数据就近部署到计算区域，解决分布式训练中的数据访问延迟问题。这标志着 Hugging Face Hub 从单纯的模型发布平台向完整的 ML 数据基础设施演进，填补了"工作层"与"发布层"之间的关键空白。

Production ML generates massive amounts of frequently changing intermediate artifacts that don't need version control, where traditional Git architectures become inefficient; Storage Buckets leverage Xet's chunk-level deduplication to significantly reduce bandwidth and storage costs, and support "pre-warming" to deploy data close to compute regions, addressing data access latency in distributed training. This marks Hugging Face Hub's evolution from a model publishing platform to complete ML data infrastructure, filling the critical gap between "working" and "publishing" layers.

---

【我能用什么 / How I can use it】

可通过 `hf buckets create` 和 `hf buckets sync` 在 2 分钟内搭建检查点同步管道，或集成 `huggingface_hub` Python SDK（v1.5.0+）到训练脚本中实现程序化数据管理；利用 `HfFileSystem` 的 fsspec 兼容性，可直接用 pandas、Polars、Dask 等库读写 Bucket 中的数据，无需修改现有代码。建议将频繁变动的训练产物存入 Bucket，仅在模型定型后通过即将推出的双向传输功能迁移到版本化仓库，形成"工作-发布"分离的完整工作流。

You can set up checkpoint sync pipelines in under 2 minutes with `hf buckets create` and `hf buckets sync`, or integrate the `huggingface_hub` Python SDK (v1.5.0+) into training scripts for programmatic data management; leveraging `HfFileSystem`'s fsspec compatibility, you can read/write Bucket data directly with pandas, Polars, Dask, etc., without modifying existing code. Recommended practice: store frequently changing training artifacts in Buckets, then migrate to versioned repos only after models are finalized using the upcoming bidirectional transfer feature, establishing a complete "work-publish" separated workflow.
