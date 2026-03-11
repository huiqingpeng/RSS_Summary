---
title: "Mini Multi-Arcade Game Cabinets with an ESP32 and Galagino"
source: "Hackaday"
url: "https://hackaday.com/2026/03/11/mini-multi-arcade-game-cabinets-with-an-esp32-and-galagino/"
published: "2026-03-11"
fetched: "2026-03-12T07:03:57.340446"
---

Most people love arcade games, but putting a full-sized arcade cabinet in the living room can lead to certain unpleasant complications. Ergo the market for fun-sized cabinets has exploded alongside the availability of cheap SBCs and MCUs that can run classical arcade titles. Microcontrollers like the ESP32 with its dual 240 MHz cores can run circles around the CPU grunt of 1980s arcade hardware. Cue [Till Harbaum]’s Galagino ESP32-based arcade emulator project, that recently saw some community versions and cabinet takes.
There was a port to the PlatformIO framework by [speckhoiler] which also added a few more arcade titles and repurposed the enclosure of an off-the-shelf ‘My Arcade’ by stuffing in an ESP32-based ‘Cheap Yellow Display‘ (CYD) board instead. These boards include the ESP32 module, a touch display, micro SD card slot, sound output, and more; making it an interesting all-in-one solution for this purpose.
Most recently [Davide Gatti] and friends ported the Galagino software to the Arduino platform and added a 3D printed enclosure, though you will still need to source a stack of parts which are listed in the bill of materials. What you do get is a top display that displays the current game title in addition to the display of the usual CYD core, along with an enclosure that can be printed both in single- or multi-color.
There’s also a build video that [Davide Gatti] made, but it’s only in Italian, so a bit of a crash course in this language may be required for some finer details.
Thanks to [ZT] for the tip.
