---
title: "WolfIP Doesn’t Allocate"
source: "Hackaday"
url: "https://hackaday.com/2026/04/09/wolfip-doesnt-allocate/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:39.350255"
---

For some types of embedded systems — especially those that are safety-critical — it’s considered bad form to dynamically allocate memory during operation. While you can usually arrange for your own code to behave, it’s the libraries that get you. In particular, it is hard to find a TCP/IP stack that doesn’t allocate and free memory all over the place. Unless you’ve found wolfIP.
The library supports a BSD-like non-blocking socket API. It can act as an endpoint, but can also support multiple interfaces and forwarding if you were building something like a router. It doesn’t appear to be bare-bones either. In addition to the normal things you’d expect for IPv4, there’s also ICMP, IPSEC, ARP, DHCP, DNS, and HTTP with or without SSL TLS. There is also a FIPS-compliant implementation of WireGuard for VPN, although it is not directly compatible with standard WireGuard, only with other instances of itself (known as wolfGuard). There is a Linux kernel module for WolfGuard, though.
The code should be fairly easy to port, and it includes a binding for FreeRTOS already. If you’ve used wolfIP, let us know in the comments.
If you want to really get down to the low-level, try this project. Of, if you want a refresher on basics, we can help with that, too.
