---
title: "How Small Can A Linux Executable Be?"
source: "Hackaday"
url: "https://hackaday.com/2026/03/31/how-small-can-a-linux-executable-be/"
published: "2026-03-31"
summarized: "2026-04-01T07:02:54.477196"
ai_provider: "openai"
---

【是什么 / What it is】
这篇文章展示了如何将一个 Linux "Hello, World!" 程序从典型的 12-15KB 压缩到极端的 120 字节。作者 Nathan Otterness 通过汇编语言、移除 ELF 节头、精心选择指令，以及利用 ELF 头和程序头中的空闲空间来嵌入代码，实现极致的二进制体积优化。

This article demonstrates how to compress a Linux "Hello, World!" program from a typical 12-15KB down to an extreme 120 bytes. Author Nathan Otterness achieves this through assembly language, removing ELF section headers, carefully selecting instructions, and exploiting unused spaces in the ELF and program headers to embed code.

【为什么重要 / Why it matters】
在软件体积不断膨胀（尤其是视频游戏）的背景下，这种极限优化技术揭示了底层系统的工作原理，并挑战了"抽象层必然带来开销"的假设。它对于嵌入式系统、引导程序、安全研究（如漏洞利用载荷）以及理解 ELF 格式都有重要价值。

Amid ever-growing software bloat (especially in video games), this extreme optimization technique reveals how underlying systems work and challenges the assumption that abstraction layers necessarily incur overhead. It holds significant value for embedded systems, bootloaders, security research (such as exploit payloads), and understanding the ELF format.

【我能用什么 / How I can use it】
可以借鉴这种"逐字节分析"的思维来优化自己的嵌入式或容器化应用；学习手动编写系统调用和汇编来深入理解用户态与内核的交互；在安全研究中应用这些技巧来分析或构造精简的 shellcode。也可以将此作为教学案例，展示编译器输出与手工优化之间的巨大差距。

One can adopt this "byte-by-byte analysis" mindset to optimize their own embedded or containerized applications; learn to write system calls and assembly manually to deeply understand user-kernel interaction; apply these techniques in security research to analyze or construct minimal shellcode. It also serves as an excellent teaching case demonstrating the vast gap between compiler output and hand-crafted optimization.
