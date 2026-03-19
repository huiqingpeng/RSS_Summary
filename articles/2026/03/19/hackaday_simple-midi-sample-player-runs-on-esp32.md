---
title: "Simple MIDI Sample Player Runs on ESP32"
source: "Hackaday"
url: "https://hackaday.com/2026/03/19/simple-midi-sample-player-runs-on-esp32/"
published: "2026-03-19"
fetched: "2026-03-19T16:16:36.899554"
---

[Jakub] is a musician, and found himself in need of a simple way to trigger samples via MIDI when on stage. So many commercial solutions exist, but most were overkill for the job or too messy and complicated to justify their use in a live environment. Thus, [Jakub] worked up Samplotron to do exactly the job needed with a minimum of fuss.
The project is based around the ESP32. It’s effectively a lightweight hardware sampler that can trigger sounds on command via MIDI. Sample data is loaded from an SD card, which also stores the device configuration. The Samplotron plays back mono 16-bit WAV files at 44,100 Hz, delivering audio via an ES8388 audio codec module connected via I2S. Two encoders are used to control the device, with a menu system presented via an SSD1309 OLED screen. Samples can be loaded and managed via this interface, and it allows tweaks to be made to volume levels and one-shot/loop playback as needed. MIDI input to the device is simply handled via the onboard UART functionality of the ESP32 itself.
It’s a neat little bit of music hardware that does exactly what [Jakub] needs and nothing more. We’ve featured similar builds before, like this neat RP2040 soundboard. If you’re building rad custom hardware for your own musical adventures, we’d love to know all about it.
