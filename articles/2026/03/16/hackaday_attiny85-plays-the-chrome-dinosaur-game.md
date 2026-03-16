---
title: "ATtiny85 Plays the Chrome Dinosaur Game"
source: "Hackaday"
url: "https://hackaday.com/2026/03/16/attiny85-plays-the-chrome-dinosaur-game/"
published: "2026-03-16"
fetched: "2026-03-17T07:06:07.809357"
---

If you’ve ever had your internet connection drop out while running Chrome, you’ve probably seen a little dinosaur pop up to tell you what’s going on. You might have then tapped a key and learned that it’s actually a little mini-game built into the browser where you have to hop your intrepid T-rex over a bunch of cactii. [Albert David] is well familiar with this little Easter egg, and set about building a system to automatically play the game for him.
The build uses an Digispark ATtiny85 microcontroller board to run the show. It’s set up to plug in to a PC and enumerate as a USB HID device, so it can spoof the required key presses to play the game. To sense the game state, the device uses a pair of LM393 light-dependent resistor comparator modules. The bottom sensor is used to detect cactus obstacles in the game, while the upper sensor detects flying bird obstacles. Armed with this information, the microcontroller can deliver keypresses at just the right time to jump over cactuses while dodging birds overhead.
[Albert] does a great job of explaining how the project came together in the write-up. There are also useful calibration instructions that indicate how to place the sensors and tweak their thresholds so they trigger reliably and help you net a suitably high score.
Interestingly enough, this isn’t the first time we’ve seen a microcontroller take Chrome’s hidden game for a spin. The game itself has become popular enough that we’ve also seen it ported to other platforms.
