---
title: "Reverse-Engineering The Holy Stone H120D Drone"
source: "Hackaday"
url: "https://hackaday.com/2026/03/31/reverse-engineering-the-holy-stone-h120d-drone/"
published: "2026-03-31"
fetched: "2026-04-01T07:03:17.072705"
---

There are plenty of drones (and other gadgets) you can buy online that use proprietary control protocols. Of course, reverse-engineering one of these protocols is a hacker community classic. Today, [Zac Turner] shows us how this GPS drone can be autonomously controlled by a simple Arduino program or Python script.
What started as [Zac] sniffing some UDP packets quickly evolved into him decompiling the Android app to figure out what’s going on inside. He talks about how the launch command needs accurate GPS, how there’s several hidden features not used by the Android app, et cetera. And it’s not like it’s just another Linux SoC in there, either. No, there’s a proper Real-Time Operating System (RTOS) running, with a shell and a telnet interface. The list of small curiosities goes on.
After he finished reverse-engineering the protocol, he built some Python scripts, through which you can see the camera feed and control the drone remotely. He also went on to make an Arduino program that can do the latter using an Arduino Nano 33 IoT.
