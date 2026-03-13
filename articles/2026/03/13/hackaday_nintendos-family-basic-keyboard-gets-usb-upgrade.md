---
title: "Nintendo’s Family BASIC Keyboard Gets USB Upgrade"
source: "Hackaday"
url: "https://hackaday.com/2026/03/12/nintendos-family-basic-keyboard-gets-usb-upgrade/"
published: "2026-03-13"
fetched: "2026-03-14T07:03:52.673532"
---

America knew it as the Nintendo Entertainment System, but in Japan, it was the Family Computer (Famicom). It was more than just a home console—it was intended to actually do a whole lot more. All you had to do was plug in the keyboard and chuck in the right Family BASIC cartridge, and you had a computer hooked up to your TV! [Lucas Leadbetter] came across an old Family BASIC keyboard recently, and set about making it more useful in our modern age with a simple USB upgrade.
[Lucas] started with research, and soon found plenty of schematics and details on the keyboard on the NESdev wiki page. Hunting further turned up a video from [Circuit Rewind], who demonstrated how to hook up the keyboard to a Raspberry Pi Pico, including how to interface with the onboard chips to scan the keys. These resources told [Lucas] enough to get going—and that it should be as simple as wiring some custom hardware up to the internal keyboard matrix connector to get it speaking to USB.
[Lucas] went a slightly different path to [Circuit Rewind], implementing the popular QMK firmware to suit the Family Basic keyboard on an Adafruit KB2040. The Adafruit part is basically an RP2040 microcontroller slapped onto a tiny PCB in a form factor that’s ideal for making custom keyboards. [Lucas] was able to reimplement the scanning logic that [Circuit Rewind] had reverse engineered previously, and had the keyboard up and running in short order with all the usability benefits of the QMK firmware. Files are on Github for those eager to recreate the work.
As far as usability goes, [Lucas] notes that the Family BASIC keyboard is more of a conversation piece than a daily driver, thanks to its rather poor feel. Duly noted. We’ve explored how software development is done in Family BASIC before, too. Video after the break.
