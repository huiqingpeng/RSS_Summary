---
title: "CUDA 13.2 Introduces Enhanced CUDA Tile Support and New Python Features"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/cuda-13-2-introduces-enhanced-cuda-tile-support-and-new-python-features/"
published: "2026-03-09"
summarized: "2026-03-10T11:21:42.158289"
ai_provider: "openai"
---

【是什么 / What it is】
CUDA 13.2 是 NVIDIA 发布的最新 GPU 计算平台版本，核心亮点包括将 CUDA Tile 编程模型扩展至 Ampere、Ada 和 Blackwell 架构，同时大幅增强 Python 开发生态（cuTile Python、CUDA Python 性能分析和 Numba 调试），并针对 Windows 驱动模式、内存管理和嵌入式设备（Jetson）引入多项底层优化。CUDA 13.2 is NVIDIA's latest GPU computing platform release, featuring expanded CUDA Tile programming model support for Ampere, Ada, and Blackwell architectures, significant Python ecosystem enhancements (cuTile Python, CUDA Python profiling, and Numba debugging), and numerous low-level optimizations for Windows driver modes, memory management, and embedded devices (Jetson).

【为什么重要 / Why it matters】
这标志着 GPU 编程正加速向 Python 开发者友好化转型，降低高性能计算门槛；同时 MIG 支持进入嵌入式领域（Jetson Thor），为人形机器人等安全关键型应用提供硬件级隔离保障；Windows 平台默认转向 MCDM 驱动模式，意味着 WSL2、容器和高级内存管理等功能将统一可用，跨平台开发体验趋于一致。This signals a major shift toward Python-friendly GPU programming, lowering barriers to high-performance computing; MIG support entering embedded space (Jetson Thor) enables hardware-level isolation for safety-critical applications like humanoid robotics; and Windows' default transition to MCDM driver mode unifies access to WSL2, containers, and advanced memory management, converging cross-platform development experiences.

【我能用什么 / How I can use it】
若使用 Ampere 及以上 GPU，可通过 `pip install cuda-tile[tileiras]` 快速体验 cuTile Python 的递归函数、闭包捕获和自定义归约等新特性；在 Windows 上开发时可利用 `CUDA_DISABLE_PERF_BOOST` 控制功耗，或借助 `cudaMemcpyWithAttributesAsync` 简化带属性的内存传输；针对 Jetson 嵌入式场景，可探索 MIG 分区实现关键与非关键任务的资源隔离。If using Ampere or newer GPUs, quickly explore cuTile Python's new features (recursive functions, closure capture, custom reductions) via `pip install cuda-tile[tileiras]`; on Windows, leverage `CUDA_DISABLE_PERF_BOOST` for power management or `cudaMemcpyWithAttributesAsync` for simplified attributed memory transfers; for Jetson embedded scenarios, investigate MIG partitioning to isolate critical from non-critical workloads.
