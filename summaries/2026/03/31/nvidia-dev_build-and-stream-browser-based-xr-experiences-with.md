---
title: "Build and Stream Browser-Based XR Experiences with NVIDIA CloudXR.js"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/build-and-stream-browser-based-xr-experiences-with-nvidia-cloudxr-js/"
published: "2026-03-31"
summarized: "2026-04-01T07:14:34.136078"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA CloudXR.js 是一个全新的 JavaScript SDK，允许开发者通过标准网页浏览器直接流式传输 GPU 渲染的沉浸式 XR 内容，无需原生应用开发或应用商店分发。它采用双层架构（Node.js 网页服务器 + WebSocket/WebRTC 连接至 CloudXR Runtime），将 NVIDIA RTX 远程渲染能力引入 Web 平台，使企业级 VR/AR 体验能够通过 URL 直接触达用户。

NVIDIA CloudXR.js is a new JavaScript SDK that enables developers to stream GPU-rendered immersive XR content directly through standard web browsers, eliminating the need for native app development or app store distribution. It employs a two-tier architecture (Node.js web server + WebSocket/WebRTC connection to CloudXR Runtime) to bring NVIDIA RTX remote rendering capabilities to the web platform, allowing enterprise-grade VR/AR experiences to reach users via a simple URL.

---

【为什么重要 / Why it matters】

这标志着沉浸式应用构建与交付方式的根本性转变——从封闭的原生开发生态转向开放的 Web 技术栈，大幅降低开发门槛并扩展了可触达的开发者和用户群体。对于企业而言，它消除了设备管理、应用商店审核和跨平台构建的复杂性，同时支持高达 120fps 的硬件加速视频编码（AV1/H.265/H.264），为数字孪生、机器人遥操作和 3D 培训等关键场景提供高保真流式传输。

This represents a fundamental shift in how immersive applications are built and delivered—from closed native development ecosystems to open web technology stacks, significantly lowering barriers to entry and expanding the addressable developer and user base. For enterprises, it eliminates complexities around device management, app store approvals, and cross-platform builds, while supporting hardware-accelerated video encoding (AV1/H.265/H.264) at up to 120fps—enabling high-fidelity streaming for critical use cases like digital twins, robot teleoperation, and 3D training.

---

【我能用什么 / How I can use it】

开发者可从 NVIDIA NGC 下载 SDK，通过 `npm install` 快速集成到现有 Web 项目，使用 `createSession` API 建立与 CloudXR Runtime 的连接，并在 WebXR 渲染循环中调用 `sendTrackingStateToServer` 和 `render` 方法实现双向流式传输。建议从官方提供的 WebGL（极简原生 API）或 React（React Three Fiber 生产级架构）示例入手，结合 Docker 本地部署或 IWER 模拟器进行无头显开发测试，最终部署到 Meta Quest 2/3/3s 或 Pico 4 Ultra 等企业级 XR 设备。

Developers can download the SDK from NVIDIA NGC, quickly integrate it into existing web projects via `npm install`, establish connections to CloudXR Runtime using the `createSession` API, and implement bidirectional streaming by calling `sendTrackingStateToServer` and `render` within the WebXR render loop. Start with the official WebGL (minimal native API) or React (React Three Fiber production-grade architecture) samples, use Docker for local deployment or the IWER emulator for headset-free development testing, and ultimately deploy to enterprise XR devices such as Meta Quest 2/3/3s or Pico 4 Ultra.
