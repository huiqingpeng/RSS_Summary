---
title: "AMD Ryzen AI Embedded P100 series expands with up to 12 Zen 5 cores, 80 TOPS of AI performance"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/amd-ryzen-ai-embedded-p100-series-expands-with-up-to-12-zen-5-cores-80-tops-of-ai-performance/"
published: "2026-03-11"
summarized: "2026-03-12T07:02:02.332899"
ai_provider: "openai"
---

【是什么 / What it is】

AMD在2026年嵌入式世界大会上扩展了其Ryzen AI Embedded P100系列嵌入式SoC产品线，新增6款8-12核的商用和工业级型号（P164/P174/P185及其工业级i版本），将CPU核心数从原有的4-6核提升至最高12核Zen 5架构，AI算力从50 TOPS提升至80 TOPS，并集成RDNA 3.5显卡与XDNA 2 NPU。

At Embedded World 2026, AMD expanded its Ryzen AI Embedded P100 series with six new 8-12 core commercial and industrial SKUs (P164/P174/P185 and their i variants), upgrading from the original 4-6 cores to up to 12 Zen 5 cores, boosting AI performance from 50 to 80 TOPS, with integrated RDNA 3.5 graphics and XDNA 2 NPU.

【为什么重要 / Why it matters】

这标志着x86架构在边缘AI计算领域的重大跃进，80 TOPS的AI性能配合统一内存架构，使单芯片即可处理多摄像头机器视觉、视觉SLAM等高带宽低延迟任务，同时NPU负责低功耗推理；相比前代嵌入式8000系列，多线程性能提升39%、系统TOPS提升2.1倍，且支持ROCm开源软件栈避免厂商锁定。

This marks a significant leap for x86 architecture in edge AI computing—80 TOPS combined with unified memory enables single-chip processing of high-bandwidth, low-latency tasks like multi-camera machine vision and Visual SLAM, while the NPU handles low-power inference; it delivers 39% better multi-threaded performance and 2.1× higher system TOPS than the previous Embedded 8000 Series, with ROCm open software stack support avoiding vendor lock-in.

【我能用什么 / How I can use it】

开发者可利用ROCm栈直接运行PyTorch/TensorFlow模型，结合Xen虚拟化参考架构在同一芯片上部署实时操作系统与Windows/Linux混合关键负载；针对Llama 3.2-Vision、YOLOv12、MobileSAM优化的特性，适合构建工业质检机器人、自动驾驶感知模块或多路视频分析边缘网关，新品预计2026年7月量产，可提前联系早期客户渠道评估。

Developers can leverage the ROCm stack to run PyTorch/TensorFlow models directly, using the Xen virtualization reference architecture to deploy mixed-criticality workloads (RTOS + Windows/Linux) on a single chip; with optimizations for Llama 3.2-Vision, YOLOv12, and MobileSAM, these are ideal for industrial inspection robots, autonomous driving perception modules, or multi-stream video analytics edge gateways—sampling now with production in July 2026, early access channels available for evaluation.
