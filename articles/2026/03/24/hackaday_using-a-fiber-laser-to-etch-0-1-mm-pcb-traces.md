---
title: "Using a Fiber Laser to Etch 0.1 mm PCB Traces"
source: "Hackaday"
url: "https://hackaday.com/2026/03/24/using-a-fiber-laser-to-etch-0-1-mm-pcb-traces/"
published: "2026-03-24"
fetched: "2026-03-25T07:03:30.348919"
---

Creating PCBs at home is quite easy these days (vias not withstanding), but even the best DIY methods usually can’t match the resolution offered by commercial PCB production lines. Large traces are easy enough to carve out of copper-backed FR1 or FR4 with even a mill, what if you need something more like 100 µm sized traces with similar clearance? This is what [Giangix] has been experimenting with, using both a fiber laser and chemical etching to see what approach gives the best results.
The thin copper clad boards are put on the 20 Watt fiber laser and held in place with the vacuum table that [Giangix] previously made, using the power of suction to make sure the board doesn’t move. The used laser specifies a minimum line width of 0.01 mm, so that’s clearly fine enough to engrave away the chemical resist layer that is sprayed on top of the copper layer.
After some experimentation, it was found that increasing the trace clearance between the 0.1 mm traces to a hair above 0.1 mm was necessary for the subsequent chemical etching step to work the best, as otherwise some copper was still likely to remain. The chemical etching bath mixture consists of hydrochloric acid and hydrogen peroxide, in a ratio of 2 mL water to 2 mL 30% HCl and 2 drops of 35% H2O2. This is agitated for 90 s to get a pretty good result.
Although the final resistance measurements on the traces is a bit higher than theoretical, comments suggest that maybe some of the copper got removed along with the removal of the resist layer. Perhaps the most interesting question here is whether directly ablating the copper using the fiber laser would give even better results and bypass the etching chemicals.
