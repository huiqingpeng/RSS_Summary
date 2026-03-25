---
title: "Designing Protein Binders Using the Generative Model Proteina-Complexa"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/designing-protein-binders-using-the-generative-model-proteina-complexa/"
published: "2026-03-25"
summarized: "2026-03-26T07:04:46.745829"
ai_provider: "openai"
---

【是什么 / What it is】

Proteina-Complexa 是 NVIDIA 发布的一款生成式 AI 模型，用于从头设计蛋白质结合剂（protein binders）和酶。它基于 La-Proteina 架构，采用部分隐式流匹配框架（partially latent flow-matching framework），能够同时生成氨基酸序列和全原子级 3D 结构（包括主链和侧链），实现"协同设计"（co-design）。该模型还整合了推理时计算扩展（inference-time compute scaling），通过搜索算法在生成过程中迭代优化设计。

Proteina-Complexa is a generative AI model released by NVIDIA for de novo design of protein binders and enzymes. Built on the La-Proteina architecture, it employs a partially latent flow-matching framework that simultaneously generates amino acid sequences and fully atomistic 3D structures (backbone and side-chains), enabling "co-design." The model also integrates inference-time compute scaling, using search algorithms to iteratively refine designs during generation.

---

【为什么重要 / Why it matters】

蛋白质结合剂设计是开发新疗法和生物催化剂的核心挑战，但搜索空间巨大且需要精细优化分子间相互作用。Proteina-Complexa 通过协同设计打破了传统分步方法的局限，实现了原子级精度的界面优化；其实验验证规模空前——在 133 个靶点上测试了约 100 万个候选分子，并成功攻克了糖分子结合等"几乎不可能"的靶点。这标志着 AI 蛋白质设计从概念验证走向实际治疗应用的关键转折。

Protein binder design is central to developing new therapeutics and biocatalysts, yet faces vast search spaces and requires meticulous optimization of molecular interactions. Proteina-Complexa's co-design breaks from traditional fragmented workflows, enabling atomistically precise interface optimization. Its unprecedented experimental validation—~1 million candidates tested across 133 targets, including "nearly impossible" sugar-binding tasks—marks a critical transition of AI protein design from proof-of-concept to practical therapeutic applications.

---

【我能用什么 / How I can use it】

研究人员可通过命令行接口（CLI）使用 Proteina-Complexa，需具备 Python/YAML 基础、蛋白质结构知识及 NVIDIA A100/H100 GPU 访问权限。应用场景包括：针对癌症/免疫/神经疾病靶点设计治疗性结合蛋白、开发小分子药物递送载体或生物传感器、以及为工业生物催化或环境修复设计全新酶。建议从 NVIDIA 官方文档入手，结合实验验证流程（如噬菌体筛选、SPR）建立端到端的设计-测试闭环。

Researchers can access Proteina-Complexa via command-line interface, requiring Python/YAML proficiency, basic protein structure knowledge, and NVIDIA A100/H100 GPU access. Application scenarios include: designing therapeutic binders for oncology/immunology/neurology targets, developing small-molecule drug delivery vehicles or biosensors, and engineering novel enzymes for industrial biocatalysis or environmental remediation. Start with NVIDIA's official documentation and establish end-to-end design-test workflows incorporating experimental validation (e.g., phage display, SPR).
