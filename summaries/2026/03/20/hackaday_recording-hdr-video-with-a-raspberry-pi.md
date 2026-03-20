---
title: "Recording HDR Video With A Raspberry Pi"
source: "Hackaday"
url: "https://hackaday.com/2026/03/19/recording-hdr-video-with-a-raspberry-pi/"
published: "2026-03-20"
summarized: "2026-03-20T14:03:24.140678"
ai_provider: "openai"
---

【是什么 / What it is】

这篇文章介绍了如何在树莓派（Raspberry Pi）上使用索尼IMX585图像传感器录制HDR（高动态范围）视频的技术方案。作者[Collimated Beard]探索了利用该传感器4K HDR拍摄能力的完整流程，包括硬件适配、内核重编译和Video4Linux2工具配置等关键步骤。

This article presents a technical approach for recording HDR (High Dynamic Range) video on Raspberry Pi using Sony's IMX585 image sensor. The author [Collimated Beard] explores the complete workflow to leverage the sensor's 4K HDR capabilities, including hardware adaptation, kernel recompilation, and Video4Linux2 tool configuration.

---

【为什么重要 / Why it matters】

这一方案突破了树莓派官方摄像头的功能限制，为低成本嵌入式系统带来了专业级的16位HDR视频采集能力。随着内容创作和机器视觉对画质要求的提升，这种"硬核"DIY方案为开发者提供了高性价比的替代选择，也展示了开源硬件生态的扩展潜力。

This solution breaks through the limitations of official Raspberry Pi cameras, bringing professional-grade 16-bit HDR video capture to low-cost embedded systems. As content creation and machine vision demand higher image quality, this "hardcore" DIY approach offers developers a cost-effective alternative and demonstrates the expansion potential of open-source hardware ecosystems.

---

【我能用什么 / How I can use it】

如果你需要高动态范围视频采集（如科研成像、影视制作或计算机视觉项目），可以参考这个方案组装IMX585+树莓派系统，但需预留时间处理内核编译和RAW格式后期流程。对于不想深入底层的技术爱好者，建议关注社区是否有更成熟的封装方案或替代传感器出现。

If you need high dynamic range video capture (e.g., for scientific imaging, filmmaking, or computer vision projects), you can reference this build to assemble an IMX585+Raspberry Pi system, but budget time for kernel compilation and RAW post-processing workflows. For tech enthusiasts who prefer avoiding low-level work, watch the community for more mature packaged solutions or alternative sensors.
