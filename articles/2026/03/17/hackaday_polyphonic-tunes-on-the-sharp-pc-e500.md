---
title: "Polyphonic Tunes On The Sharp PC-E500"
source: "Hackaday"
url: "https://hackaday.com/2026/03/17/polyphonic-tunes-on-the-sharp-pc-e500/"
published: "2026-03-17"
fetched: "2026-03-18T07:03:49.576033"
---

If you’re a diehard fan of the chiptune scene, you’ve probably heard endless beautiful compositions on the Nintendo Game Boy, Commodore 64, and a few phat FM tracks from Segas of years later. What the scene is yet to see is a breakout artist ripping hot tracks on the Sharp PC-E500. If you wanted to, though, you’d probably find use in this 3-voice music driver for the ancient 1993 mini-PC.
This comes to us from [gikonekos], who dug up the “PLAY3” code from the Japanese magazine “Pocket Computer Journal” published in November 1993. Over on GitHub, the original articles have been scanned, and the assembly source code for the PLAY3 driver has been reconstructed. There’s also documentation of how the driver actually works, along with verification against RAM dumps from actual Sharp PC-E500 hardware. The driver itself runs as a machine code extension to the BASIC interpreter on the machine. The “PLAY” command can then be used to specify a string of notes to play at a given tempo and octave. Polyphony is simulated using time-division sound generation, with output via the device’s rather pathetic single piezo buzzer.
It’s very cool to see this code preserved for the future. That said, don’t expect to see it on stage at the next Boston Bitdown or anything—as this example video shows, it’s not exactly the punchiest chiptune monster out there. We’ll probably stick to our luscious fake-bit creations for now, while Nintendo hardware will still remain the bedrock of the movement.
