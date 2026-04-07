---
title: "wolfIP – An open-source, lightweight TCP/IP stack with no dynamic memory allocations for embedded systems"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/07/wolfip-an-open-source-lightweight-tcp-ip-stack-with-no-dynamic-memory-allocations-for-embedded-systems/"
published: "2026-04-07"
fetched: "2026-04-08T07:01:18.700573"
---

Better known for its open-source wolfSSL SSL/TLS library, wolfSSL (the company) has now released the wolfIP open-source, lightweight TCP/IP stack with no dynamic memory allocations (e.g., no malloc calls) designed for resource-constrained embedded systems.
The company highlights that wolfIP “supports both endpoint-only mode and full multi-interface support with optional IP forwarding. By default, it operates as a network endpoint, but can be configured to forward traffic between multiple network interfaces”.
wolfIP key features:
- BSD-like, non-blocking socket API, with custom callbacks
- No dynamic memory allocation
- Fixed number of concurrent sockets
- Pre-allocated buffers for packet processing in static memory
- Parameters are adjustable in config.h:
12345#define MAX_TCPSOCKETS 4#define MAX_UDPSOCKETS 2#define MAX_ICMPSOCKETS 2#define RXBUF_SIZE (20 * 1024)#define TXBUF_SIZE (32 * 1024)
- Protocols
- Data Link – IEEE 802.3 Ethernet II frame encapsulation, ARP address resolution, request/reply
- Network
- IPv4 delivery
- Optional IPv4 forwarding with multi-interface routing
- ICMP echo request/reply
- IPsec
- Transport – UDP and TCP protocols
- Applications – DHCP (client only), DNS (client only), and HTTP/HTTPS (using wolfSSL)
- VPN – wolfGuard FIPS-compliant WireGuard implementation (P-256, AES-256-GCM, SHA-256); note: NOT interoperable with standard WireGuard peers.
- FreeRTOS port available
Microcontrollers and microprocessors used in embedded systems have not only limited resources, but often lack memory management units and offer limited heap space, making dynamic allocation a challenge that can often lead to crashes. Removing the need for malloc may make the system much more stable.
You’ll find the source code (C code) licensed under a GPLv3 license, API documentation (docs/API.md), a guide explaining how to use wolfIP on STM32 microcontrollers with Ethernet using STM32CubeMX and the wolfIP CMSIS pack, and tools on GitHub. If you prefer the Rust programming language or need IPv6 support, the smoltcp library can be configured not to use allocation as well.
Via Adafruit
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
