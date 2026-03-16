---
title: "Making a Better Kitchen Scale out of Junk Parts"
source: "Hackaday"
url: "https://hackaday.com/2026/03/16/making-a-better-kitchen-scale-out-of-junk-parts/"
published: "2026-03-16"
fetched: "2026-03-17T07:03:23.674043"
---

Kitchen scales are plentiful and cheap, but their accuracy and measuring speed often leave a lot to be desired. In particular the filtering out of noise can make small changes a nightmare as e.g. adding a little bit of weight slowly can result in the result never updating. This frustrated [Mark Furneaux] enough that he dug up the load cell and metal base of a scrapped laboratory scale and added a strain gauge amplifier to build a better kitchen scale around it.
The only purpose-bought part was an HX710-based strain gauge amplifier module for $7 with LED display, with the metal base getting some metal bits welded onto it to hold said module as well as a push button and toggle switch. Existing wiring from the load cell was wired into the HX710 module, with power provided from a single 18650 Li-ion cell. This was paired with the standard TP4056-based module and its protection IC.
Ultimately the entire assembly looks very much bodged together, with plentiful zip ties, hot glue and messy welding, but it’s hard to deny that it seems to work well. A plastic cutting board makes for a good surface for the items being weighed, and measured drift across the range was about 200 mg, while the amplifier module updates the output in real-time so that you can see even the smallest changes and noise.
Even if you’re not lucky enough to have such a nice load cell and base kicking around, strain gauges are everywhere, and you can absolutely hack an existing (kitchen) scale to be better with some custom hard- and software.
