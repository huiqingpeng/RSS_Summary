---
title: "Better Faux-Analog VU Meters"
source: "Hackaday"
url: "https://hackaday.com/2026/03/23/better-faux-analog-vu-meters/"
published: "2026-03-23"
fetched: "2026-03-24T07:12:44.668132"
---

One of the coolest things about old hi-fi hardware is that it often came with flickety needles that danced with the audio level. You can still buy these if you want, or you can simulate the same look on a screen, as [mircemk] demonstrates.
It isn’t [mircemk]’s first rodeo in this regard. An earlier project involved creating simulated VU meters on round displays, but they were somewhat limited. Using the Adafruit GFX library on an ESP32 netted a working setup, but it was jerky and very jagged and digital-looking. It was more akin to a fake needle display running on an 8-bit computer than something that looked like a real vintage VU meter.
[mircemk] didn’t give up and figured the ESP32 microcontroller and GC9A01 round display could surely deliver better results. The trick was to leverage the LVGL graphics library instead, along with the Squarelinestudio UI editor. The library was able to display far richer graphics that look like an actual vintage VU meter, even appearing glowing and backlit like the real thing. The moving needle animates far more smoothly as well, pulsing with the music in a way that feels far more realistic compared to the earlier attempt.
It’s nice to see this simple project revisited and so boldly improved just a year later. If you’re looking to implement real-looking gauges while retaining the flexibility of a small LCD screen, you might like to try the LVGL library for yourself. With that said, sometimes you just can’t beat the real analog gauges themselves. Video after the break.
