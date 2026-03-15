---
title: "Building a Neatly Framed Word Clock"
source: "Hackaday"
url: "https://hackaday.com/2026/03/14/building-a-neatly-framed-word-clock/"
published: "2026-03-15"
fetched: "2026-03-16T07:02:05.269376"
---

Reading analog clocks is a pretty straightforward skill to learn. However, if you’ve already learned to read and don’t want to pick up the extra skill, a word clock is a perfect solution for telling time. [povey_tech] found some nice examples in the wild but didn’t appreciate the price, so he set about building his own.
The build is based around an ESP32 microcontroller. While many projects in this vein would use the onboard wireless connectivity to query network time servers, in this case, the board relies on the user manually setting the time and a DS1307 real-time-clock module to keep a steady tick. Also onboard is a VEML7700 ambient light sensor, which the microcontroller uses to control the brightness of the WS2812 LEDs inside the board.
The words themselves are laser cut out of acrylic panels, with everything set inside a tidy oak picture frame. A layer of anti-reflective glass in front helps cut down on glare, while [povey_tech] was so kind as to implement two LEDs per letter to allow for lovely color gradients to be displayed. Configuring the clock is easy thanks to a webpage hosted on the ESP32 that allows for control of dimming modes, colors, and setting the time. Home Assistant integration is something planned for the future.
We’ve seen many great word clocks over the years. Perhaps the biggest leap forward in this world was the development of the addressable LED strip which made constructing these clocks much easier.
