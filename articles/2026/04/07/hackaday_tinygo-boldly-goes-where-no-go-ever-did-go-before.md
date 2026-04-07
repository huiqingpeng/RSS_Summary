---
title: "TinyGo Boldly Goes Where No Go Ever Did Go Before"
source: "Hackaday"
url: "https://hackaday.com/2026/04/07/tinygo-boldly-goes-where-no-go-ever-did-go-before/"
published: "2026-04-07"
fetched: "2026-04-08T07:01:26.685573"
---

When you’re programming microcontrollers, you’re likely to think in C if you’re old-school, Rust if you’re trendy, or Python if you want it done quick and have resources to spare. What about Go? The programming language, not the game. That’s an option, too, with TinyGo now supporting over 100 different dev boards, along with webASM.
We covered TinyGo back in 2019, but they were just getting started at that point, targeting the Arduino and BBC:micro boards. They’ve grown that list to include everything from most of Adafruit’s fruitful suite of offerings, ESP32s, and even the Nintendo Game Boy Advance. So now you can go program go in Go so you can play go on the go.
The biggest drawback–which is going to be an absolute dealkiller for a lot of applications–is a lack of wireless connectivity support. Claiming to support the ESP8266 while not allowing one to use wifi is a bit of a stretch, considering that’s the whole raison d’être of that particular chip, but it’s usable as a regular microcontroller at least.
They’ve now implemented garbage collection, a selling point for those who like Go, but admit it’s slower in TinyGo compared to its larger cousin and won’t work on AVR chips or in WebAssembly. It’s still not complete Go, however, so just as we reported in 2019, you won’t be able to compile all the standard library packages you might be used to. There are more of them than there were, so progress has been made!
Still, knowing how people get about programming languages, this will please the Go fanatics out there. Others might prefer to go FORTH and program their Arduinos, or to wear out their parentheses keys with LISP. The more the merrier, we say!
