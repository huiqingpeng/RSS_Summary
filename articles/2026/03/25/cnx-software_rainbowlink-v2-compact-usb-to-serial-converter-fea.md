---
title: "RainbowLink-V2 compact USB-to-serial converter features 12V output, dual TTL, isolated RS-485 and RS-232 interfaces"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/25/rainbowlink-v2-compact-usb-to-serial-converter-features-12v-output-dual-ttl-isolated-rs-485-and-rs-232-interfaces/"
published: "2026-03-25"
fetched: "2026-03-26T07:01:36.357191"
---

DFRobot’s RainbowLink-V2 USB-to-serial converter features four independent channels, namely one isolated RS-485, one isolated RS-232, and two TTL interfaces usable simultaneously.
The compact tool also converts 5V provided from the host’s USB interface to 12V/800mA, 5V/2A, and 3.3V/200mA outputs, eliminating the need for a separate power adapter.
RainbowLink-V2 (TEL0190) specifications:
- USB – 1x USB Type-C port for power and adata
- Serial
- 2x TTL (3.3V) via headers
- 1x fully isolated RS485 channel via lever terminal
- 1x fully isolated RS232 channel via lever terminal
- Baud Rate – 2400 to 128000 bps
- Misc
- 3x Power LEDs for 3.3V, 5V, and 12V
- 4x Link LEDs for TTL 1/2, RS232, and RS485
- 12AWG – 22AWG wires supported on lever-type spring terminals
- Built-in short-circuit protection and overcurrent protection (but users are still recommended to avoid short-circuiting to prevent damage)
- Input voltage – 5V via USB-C port
- Output voltage
- 3.3V up to 200mA via header
- 5V up to 2A via header; note: this power interface is directly connected to the USB port. It supports up to 2A when connected to a USB-C port, and up to 500 mA when connected to a USB-A port
- 12V up to 800mA via level terminal and header
- Dimensions – 77 x 57 x 21 mm (PC housing)
The company says it works on Windows, Linux (including Raspberry Pi), and macOS. It’s not surprising, as it’s just seen as a standard USB to serial device named “RainbowLink RS485”. Still, the company provides CH343 drivers for Windows users just in case. You’ll find those on the wiki along with other basic instructions.
It can be used for debugging, like basic USB-to-TLL boards, but since it adds an extra TTL interface, you could also connect a GPS module or another UART-based module. RS-485 and RS-232 interfaces, in combination with 12V power output, also enable a wider range of sensors, for instance, an RS-485 soil sensor, and support for controlling RS-232-connected industrial PLCs. We’ve written about other USB to RS232/RS485 boards like the Ollie v2 and Protocol Droid, but I like the compact design, features set, and price point of the DFRobot USB-to-serial tool.
DFRobot sells the RainbowLink-V2 for $24.90 on Amazon and on its own store. Note that you may find a cheaper “RainbowLink” with a similar look-and-feel when searching, but that’s the first version lacking 12V power output and RS232/RS485 interfaces isolation.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
