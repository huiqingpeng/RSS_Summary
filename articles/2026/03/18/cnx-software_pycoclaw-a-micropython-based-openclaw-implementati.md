---
title: "PycoClaw – A MicroPython-based OpenClaw implementation for ESP32 and other microcontrollers"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/18/pycoclaw-a-micropython-based-openclaw-implementation-for-esp32-and-other-microcontrollers/"
published: "2026-03-18"
fetched: "2026-03-18T18:02:54.271301"
---

PycoClaw is a MicroPython-based platform for running AI agents on ESP32 and other microcontrollers that brings OpenClaw workspace-compatible intelligence to resource-constrained embedded devices.
We had already covered the C-based Miniclaw for ESP32-S3 SoCs, the PycoClaw’s developer (Jonathan Peace) told CNX Software that it is a “full OpenClaw-compliant agent” that supports more LLM providers (OpenAI, Gemini, Ollama, etc.), interfaces with not only Telegram, but also ScriptO Studio and WebRTC, and offers features like OTA updates, extensions, and battery-optimized operation.
The table below compares PycoClaw to OpenClaw, Nanobot, PicoClaw, NullClaw, and MimiClaw.
| Feature | PycoClaw | OpenClaw | Nanobot | PicoClaw | NullClaw | MimiClaw |
|---|---|---|---|---|---|---|
| Approach | 🔧 Scripted | 🔧 Scripted | 🔧 Scripted | ⚙️ Compiled | ⚙️ Compiled | ⚙️ Compiled |
| Runtime | MicroPython | Node.js (server) | Python (server) | Go (binary) | Zig (static) | C (ESP32) |
| Runtime Modifiable | ✓ Live on device | ✓ Hot reload | ✓ Edit & restart | ✗ Rebuild | ✗ Rebuild | ✗ Reflash |
| Install | One-click web flash | npm i -g | pip install | make install | zig build | ESP-IDF build |
| Agent Loop | ✓ Full dual-loop | ✓ Full dual-loop | ✓ Full | ✓ Full | ✓ Full | ✓ Basic ReAct |
| Streaming | ✓ C-native SSE | ✓ SSE | ✓ SSE | ✗ | ✓ SSE | ✗ |
| Tool Calling | ✓ Recursive | ✓ Recursive | ✓ Yes | ✓ Yes | ✓ 18+ tools | ✓ 5 tools |
| Sub-Agents | ✓ bg_tasks | ✓ sessions_spawn | ✓ Subagent | ✓ Spawn tool | ✓ Subagents | ✗ |
| Multi-Model | ✓ Provider routing | ✓ Failover + routing | ✓ 16+ providers | ✓ model_list | ✓ 22+ providers | 2 providers |
| Memory | ✓ Hybrid TF-IDF + Vector | ✓ Vector DB | Basic file | MEMORY.md | ✓ FTS5 + Vector | MEMORY.md only |
| Context Compaction | ✓ LLM summarization | ✓ LLM summarization | ✗ | ✗ | ✓ Auto | ✗ |
| Heartbeat / Cron | ✓ Full parity | ✓ Full | ✓ Full | ✓ Full | ✓ Full | ✓ Basic |
| Chat Channels | Studio + Telegram (Extensible) | 14+ channels | 9 channels | 6 channels | 18 channels | Telegram only |
| Hardware Control | ✓ GPIO, LVGL, CAN | ✗ | ✗ | ✗ | Serial, GPIO, Arduino | Basic GPIO |
| Display UI | ✓ LVGL touchscreen | Canvas (A2UI) | ✗ | ✗ | ✗ | ✗ |
| Skills / Plugins | ✓ ScriptoHub | ✓ ClawHub | ✓ ClawHub | ✓ ClawHub | ✓ Skill packs | ✗ |
| Binary / Footprint | ~2 MB firmware | ~28 MB dist | Scripts (~4K LoC) | ~8 MB binary | 678 KB binary | ~1 MB firmware |
| Power | 0.5W USB | ~15W server | ~15W server | ~2W SBC | ~2W SBC | 0.5W USB |
| Cost | $5 + API keys | Server + API keys | Server + API keys | $10 + API keys | $5 + API keys | $5 + API keys |
MimiClaw still offers the lowest footprint and highest efficiency, but PycoClaw appears to offer many more features, including improved GPIO support. It works on ESP32-S3 with at least 8MB flash and PSRAM, ESP32-P4, and should soon support Raspberry Pi RP2350 boards with PSRAM as well.
PycoClaw can be installed on supported hardware through a “one-click install” using a compatible web browser. You’ll find detailed documentation, firmware binaries, website source code, and Scripto Studio IDE resources on the Jetpax account on GitHub. However, while the project is described as an “open-source platform” released under an “MIT license”, I was unable to find the firmware source code, and the pycoclaw repository is only for the website source. More details may also be found on the project’s website.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
