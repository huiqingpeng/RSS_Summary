---
title: "Power Control for a Busy Workbench"
source: "Hackaday"
url: "https://hackaday.com/2026/03/10/power-control-for-a-busy-workbench/"
published: "2026-03-10"
fetched: "2026-03-11T09:02:48.049518"
---

Who among us does not have a plethora of mains-powered devices on their workbench, and a consequent mess of power strips to run them all? [Jeroen Brinkman] made his more controllable with a multi-way switch box.
At first sight it’s a bank of toggle switches, one for each socket. But this is far more than a wiring job, because of course there are a couple of microcontrollers involved, and each of those switches ultimately controls a relay. There are also status LEDs for each socket, and a master switch to bring them all down. Arduino code is provided, so you can build one too if you want to.
We like the idea of a handy power strip controller, and especially the master switch with the inherent state memory provided by the switches. This could find a home on a Hackaday bench, and we suspect on many others too. It’s by no means the first power strip with brains we’ve seen, but most others have been aimed at the home instead.
