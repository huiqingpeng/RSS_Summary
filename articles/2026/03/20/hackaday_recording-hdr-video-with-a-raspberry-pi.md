---
title: "Recording HDR Video With A Raspberry Pi"
source: "Hackaday"
url: "https://hackaday.com/2026/03/19/recording-hdr-video-with-a-raspberry-pi/"
published: "2026-03-20"
fetched: "2026-03-20T14:03:16.356337"
---

The Raspberry Pi line of single-board computers can be hooked up with a wide range of compatible cameras. There are a number of first party options, but you don’t have to stick with those—there are other sensors out there with interesting capabilities, too. [Collimated Beard] has been exploring the use of the IMX585 camera sensor, exploiting its abilities to capture HDR content on the Raspberry Pi.
The IMX585 sensor from Sony is a neat part, capable of shooting at up to 3840 x 2160 resolution (4K) in high-dynamic range if so desired. Camera boards with this sensor that suit the Raspberry Pi aren’t that easy to find, but there are designs out there that you can look up if you really want one. There are also some tricks you’ll have to do to get this part working on the platform. As [Collimated Beard] explains, in the HDR modes, a lot of the standard white balance and image control algorithms don’t work, and image preview can be unusable at times due to the vagaries of the IMX585’s data format. You’ll also need to jump some hurdles with the Video4Linux2 tools to enable the full functionality of these modes.
Do all that, recompile the kernel with some tweaks and the right drivers, though, and you’ll finally be able to capture in 16-bit HDR modes. Oh, and don’t forget—you’ll need to find a way deal with the weird RAW video files this setup generates. It’s a lot of work, but that’s the price of entry to work with this sensor right now. If it helps convince you, the sample shots shared by [Collimated Beard] are pretty good.
If you’re looking to record some really juicy, colorful imagery with the Raspberry Pi, this is a difficult but viable way to go. We’ve seen some other hardcore Raspberry Pi camera hacks of late, too.
