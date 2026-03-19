---
title: "Teardown of a 2026 LEGO SMART Brick"
source: "Hackaday"
url: "https://hackaday.com/2026/03/18/teardown-of-a-2026-lego-smart-brick/"
published: "2026-03-19"
fetched: "2026-03-19T14:02:54.245873"
---

At the beginning of March this year LEGO released their new SMART brick, which looks like a 2×4 stud brick and is filled to the brim with sensors, LEDs, NFC and Bluetooth functionality, as well as a purported custom ASIC. The central idea behind it appears to be to add a lot of interactivity to LEGO builds while allowing for mesh-style communication with other SMART bricks. Naturally, this makes it a great subject for a teardown, which is what [EvilmonkeyzDesignz] over on YouTube did in a recent video.
Normally the only way you can purchase one of these new bricks is by buying them as part of a ‘Smart Play’ set, but someone was selling singular bricks on EBay. As the brick is inductively recharged, it’s pretty well-sealed, requiring a fairly destructive opening method.
Directly below the transparent top is a speaker, with the opposing PCB on the main body containing a microphone as well as a number of RGB LEDs. On the opposite side of this PCB we find the photo sensor, but to get to this part of the PCB the copper wires that wrap around the entire main assembly have to be disconnected from the PCB’s side pads with some force as they’re apparently pressed in place without the use of solder.
Freeing the main PCB from its plastic enclosure also ended up being fairly destructive, but gave the first good look at its guts. Courtesy of Redditor [PsychologicalYak4619] who previously did a teardown and analysis of such a brick, many details are already available. There’s a separate Bluetooth 5.4 SoC marked EM9305 from EM Microelectronics as well as a 16 Mb Winbond SPI Flash memory chip.
The main application ASIC – marked as DA000001-04 – is the real mystery, which is the marketed custom ASIC. Since this is a flip-chip package, taking a look at the die is super-easy, barely an inconvenience.
On this die shot we can see what looks like CSEM
along with some additional letters that may or may not give a hint as to its design origins. This unfortunately means that we do not get any in-depth details on what this ASIC contains and what its capacities are.
Since there is no RAM on the PCB, it appears to at least contain some amount of RAM inside, so assuming that the SPI Flash IC is used by it and not the Bluetooth SoC there might be some hints in the firmware if it were to be extracted.
It’s also of note just how well-sealed these bricks are, making them instant e-waste if anything were to go wrong with any of its components. Considering that the lifespan of Li-ion batteries is generally 2+ years before they begin to significantly degrade, its built-in battery might be the thing that these bricks become the most famous for, not to mention make it run afoul of EU regulations that come into effect next year.
