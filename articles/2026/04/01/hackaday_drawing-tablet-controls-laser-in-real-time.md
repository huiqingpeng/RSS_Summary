---
title: "Drawing Tablet Controls Laser In Real-Time"
source: "Hackaday"
url: "https://hackaday.com/2026/04/01/drawing-tablet-controls-laser-in-real-time/"
published: "2026-04-01"
fetched: "2026-04-02T07:07:56.402409"
---

Some projects need no complicated use case to justify their development, and so it was with [Janne]’s BeamInk, which mashes a Wacom pen tablet with an xTool F1 laser engraver with the help of a little digital glue. For what purpose? So one can use a digital pen to draw with a laser in real time, of course!
Here’s how it works: a Python script grabs events from a USB drawing tablet via evdev (the Linux kernel’s event device, which allows user programs to read raw device events), scales the tablet size to the laser’s working area, and turns pen events into a stream of laser power and movement G-code. The result? Draw on tablet, receive laser engraving.
It’s a playful project, but it also exists as a highly modular concept that can be adapted to different uses. If you’re looking at this and sensing a visit from the Good Ideas Fairy, check out the GitHub repository for more technical details plus tips for adapting it to other hardware.
We’re reminded of past projects like a laser cutter with Etch-a-Sketch controls as well as an attempt to turn pen marks into laser cuts, but something about using a drawing tablet for real-time laser control makes this stand on its own.
