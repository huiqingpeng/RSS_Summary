---
title: "picoZ80 – A Z80 microprocessor drop-in replacement based on Raspberry Pi RP2350B and ESP32"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/26/picoz80-a-z80-microprocessor-drop-in-replacement-based-on-raspberry-pi-rp2350b-and-esp32/"
published: "2026-03-26"
summarized: "2026-03-27T07:10:40.305762"
ai_provider: "openai"
---

【是什么 / What it is】

picoZ80 是一款基于 Raspberry Pi RP2350B 微控制器和 ESP32 无线芯片的 Z80 微处理器直插替代方案，利用 RP2350B 的可编程 I/O（PIO）状态机精确模拟 Z80 的地址、数据和控制总线时序，可直接插入 legacy Z80 计算机的 DIP-40 插槽使用。

The picoZ80 is a drop-in replacement for the Z80 microprocessor based on the Raspberry Pi RP2350B microcontroller and ESP32 wireless SoC. It uses the RP2350B's Programmable I/O (PIO) state machines to reproduce cycle-accurate address, data, and control buses of the Z80 MPU, allowing direct insertion into legacy Z80 computers' DIP-40 sockets.

【为什么重要 / Why it matters】

Z80 处理器于 2024 年停产，结束了近 50 年的生产历史，而 picoZ80 为复古计算爱好者提供了一种硬件级替代方案，无需 FPGA 即可实现精确的时序仿真；此外，其通过 JSON 配置文件和"persona"系统支持多机型切换，大大降低了不同复古计算机平台的维护成本。

With the Z80 processor discontinued in 2024 after nearly 50 years of production, the picoZ80 offers retro computing enthusiasts a hardware-level alternative that achieves precise timing emulation without FPGA. Its JSON-based configuration and "persona" system for multi-machine switching significantly reduces maintenance costs across different vintage computer platforms.

【我能用什么 / How I can use it】

可用于修复或升级 Sharp MZ 系列、Amstrad PCW 等 Z80 复古计算机，通过 WiFi 进行远程配置和文件管理；开发者可关注其即将开源的 GitHub 仓库，基于硬件设计进行个人或非商业项目开发，或探索将其应用于教育场景的计算机体系结构教学。

It can be used to repair or upgrade Z80 vintage computers like Sharp MZ series and Amstrad PCW, with remote configuration and file management via WiFi. Developers can watch for its upcoming open-source release on GitHub to build personal or non-commercial projects based on the hardware design, or explore applications in computer architecture education.
