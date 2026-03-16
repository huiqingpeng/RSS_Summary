---
title: "Run Autonomous, Self-Evolving Agents More Safely with NVIDIA OpenShell"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell/"
published: "2026-03-16"
summarized: "2026-03-17T07:08:40.537025"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA 推出了 **OpenShell**，一个开源安全运行时环境，专门用于安全部署自主、持续运行的 AI 代理（称为 "claws"）。它通过沙箱隔离、策略引擎和隐私路由器，在代理外部强制执行安全约束，解决传统代理运行时缺乏核心安全原语的问题。

NVIDIA has released **OpenShell**, an open-source secure runtime environment specifically designed for safely deploying autonomous, continuously running AI agents (called "claws"). It enforces security constraints outside the agent through sandbox isolation, a policy engine, and a privacy router, addressing the lack of core security primitives in traditional agent runtimes.

---

【为什么重要 / Why it matters】

自主 AI 代理正在从"助手"演变为能独立执行、自我进化、长期运行的"爪牙"，但现有基础设施存在根本安全缺陷：防护机制与代理同处一个进程，易被绕过。OpenShell 的"进程外策略执行"架构填补了关键空白，使企业能够真正信任并规模化部署这些生产力工具，未来 6-12 个月的基础设施决策将塑造企业代理部署的长期格局。

Autonomous AI agents are evolving from "assistants" to "claws" that execute independently, self-evolve, and run continuously—but existing infrastructure has fundamental security flaws where guardrails live inside the same process they protect. OpenShell's "out-of-process policy enforcement" architecture fills this critical gap, enabling enterprises to truly trust and scale these productivity tools; infrastructure decisions in the next 6-12 months will shape enterprise agent deployment for years to come.

---

【我能用什么 / How I can use it】

开发者可立即通过 `openshell sandbox create --remote spark --from openclaw` 一键启动沙箱，无需修改代码即可让 OpenClaw、Claude Code、Codex 等代理安全运行。建议结合企业场景：利用策略引擎定义细粒度权限边界，配置隐私路由器实现敏感数据本地处理，并通过实时策略更新与审计追踪建立可信的代理治理框架。

Developers can immediately launch a sandbox with `openshell sandbox create --remote spark --from openclaw` to run OpenClaw, Claude Code, Codex and other agents safely without code changes. For enterprise scenarios: use the policy engine to define granular permission boundaries, configure the privacy router for on-device sensitive data processing, and establish trustworthy agent governance through live policy updates and audit trails.
