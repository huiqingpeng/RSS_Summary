---
title: "ESP-IDF v6.0 framework adds support for ESP32-C5 and ESP32-C61, preview for ESP32-H21 and ESP32-H4"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/24/esp-idf-v6-0-framework-adds-support-for-esp32-c5-and-esp32-c61-preview-for-esp32-h21-and-esp32-h4/"
published: "2026-03-24"
fetched: "2026-03-25T07:03:04.080805"
---

Espressif Systems released the ESP-IDF v6.0 framework a few days ago with stable support for ESP32-C5 and ESP32-C61 SoCs, as well as preview support for ESP32-H21 and ESP32-H4 low-power wireless microcontrollers.
The framework also implements a new ESP-IDF Installation Manager (EIM) to make the ESP-IDF installation easier, relies on the low-footprint Picolibc C library, adds security and tooling updates, as well as a few Wi-Fi enhancements, and the ability to update the bootloader over the air.
Here are some of the ESP-IDF v6.0 highlights:
- ESP-IDF Installation Manager – Unified cross-platform tool to simplify the setup process for ESP-IDF and compatible IDEs. It’s available as a graphical interface or a CLI for automation and CI/CD pipelines. You can check the installation instructions for your OS.
- Picolibc replaces Newlib for a smaller memory footprint and better performance on resource-constrained devices. Check the Newlib vs Picolibc comparison for details. Contrary to some of the updates below, this change is transparent, and your code should still compile and run without modifications.
- Security updates
- ESP-IDF v6.0 upgrades MbedTLS to version 4.x and migrates cryptographic operations to the PSA Crypto API (Platform Security Architecture).
- Applications relying on legacy mbedtls_* cryptographic primitives will need to migrate to PSA Crypto APIs.
- Build System and tooling improvements
- New CMake build system (Preview) – ESP-IDF Build System v2
- Custom idf.py extensions – Allows developers to embed their own commands and tools into the standard ESP-IDF CLI using component-based extensions or Python package extensions
- Default Kconfig values are now marked with a # default: annotation
- Build configuration presets (e.g., development, production) can be stored in the CMakePresets.json file. So instead of typing:
1idf.py -B build_prod -D SDKCONFIG_DEFAULTS="sdkconfig.defaults.production" build
Developers can enter a much shorter command instead:
1idf.py --preset production build - Built-in MCP (Model Context Protocol) server for AI assistants. It’s particularly useful for IDE-based AI agents like VS Code Copilot or Cursor. Check the documentation for details.
- Wi-Fi enhancements – The ESP-IDF 6.0 adds experimental support for Wi-Fi Aware Unsynchronized Service Discovery (USD) proximity-based service discovery mechanism, and implements a “WPA3 Compatible” mode to serve both WPA2 and WPA3 clients simultaneously.
- Safe Bootloader OTA updates – This feature is supported on the ESP32-C5 and ESP32-C61, since the ROM bootloader can fall back to a recovery partition if the primary bootloader fails to load on these parts.
You can check the full changelog on the new release notes database, and access the ESP-IDF v6.0 release itself on GitHub.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
