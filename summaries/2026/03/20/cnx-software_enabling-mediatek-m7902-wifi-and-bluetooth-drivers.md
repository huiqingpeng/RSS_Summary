---
title: "Enabling MediaTek M7902 WiFi and Bluetooth drivers on Ubuntu 24.04 the easy way"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/"
published: "2026-03-20"
summarized: "2026-03-20T16:03:26.966425"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍了如何在 Ubuntu 24.04 上为联发科 MT7902 WiFi 6E 和蓝牙 5.x 芯片组安装驱动程序。由于该驱动已合并到主线 Linux 内核（预计 Linux 7.0 发布），但尚未进入当前发行版，开发者 "hmtheyboy154" 将其向后移植到了 Linux 6.6 至 6.19 版本，使华硕 Vivobook 等 Windows 笔记本用户无需等待官方更新即可使用无线功能。

This article explains how to install drivers for the MediaTek MT7902 WiFi 6E and Bluetooth 5.x chipset on Ubuntu 24.04. While the driver has been merged into mainline Linux (expected in Linux 7.0 release) but not yet available in current distributions, developer "hmtheyboy154" backported it to Linux 6.6 through 6.19, enabling users of Windows laptops like ASUS Vivobook to use wireless functionality without waiting for official updates.

---

【为什么重要 / Why it matters】

MT7902 芯片组广泛应用于多款 Windows 笔记本，但 Linux 用户已等待近两年才获得官方驱动支持。这一向后移植方案解决了硬件兼容性的燃眉之急，避免了用户因无线功能缺失而被迫更换硬件或操作系统的困境，同时也展示了开源社区在填补厂商支持空白方面的关键作用。

The MT7902 chipset is widely used in many Windows laptops, yet Linux users had waited nearly two years for official driver support. This backporting solution addresses the urgent hardware compatibility issue, preventing users from being forced to replace hardware or operating systems due to missing wireless functionality, while also demonstrating the open-source community's critical role in filling vendor support gaps.

---

【我能用什么 / How I can use it】

如果你拥有搭载 MT7902 PCIe 模块的笔记本（可通过 `lspci | grep 7902` 确认），可从 GitHub 克隆仓库后执行 `make` 和 `sudo make install` 编译安装 WiFi 驱动，蓝牙功能需切换至 `bluetooth_backport` 分支并黑名单原有 `btusb` 和 `btmtk` 模块。此方法适用于 Ubuntu 24.04 及其他基于 Linux 6.6-6.19 内核的发行版，但 SDIO 模块用户需寻找其他解决方案。

If you own a laptop with an MT7902 PCIe module (verifiable via `lspci | grep 7902`), you can clone the GitHub repository and run `make` and `sudo make install` to compile and install the WiFi driver; for Bluetooth, switch to the `bluetooth_backport` branch and blacklist the original `btusb` and `btmtk` modules. This method works on Ubuntu 24.04 and other distributions based on Linux 6.6-6.19 kernels, though SDIO module users need to seek alternative solutions.
