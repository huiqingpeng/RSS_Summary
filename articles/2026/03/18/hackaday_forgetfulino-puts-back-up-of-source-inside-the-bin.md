---
title: "Forgetfulino Puts Back Up of Source Inside the Binary"
source: "Hackaday"
url: "https://hackaday.com/2026/03/18/forgetfulino-puts-back-up-of-source-inside-the-binary/"
published: "2026-03-18"
fetched: "2026-03-19T01:02:59.906744"
---

How often have you pulled out old MCU-based project that still works fine, but you have no idea where the original source code has gone? Having the binary image and the source code as separate things to keep track of usually isn’t a problem, but there’s something to be said for adding the source — and documentation — to this image if you have some flash to spare. This is basically what the Forgetfulino Arduino library by [Nader Al Khatib] does.
Essentially, the library compresses the source files and assigns it to be burned onto the flash alongside the binary. There is also a bit of code added to the firmware so that this code can be retrieved via the serial port at any time, negating the need for a firmware dump and manual disassembly. For ease of use, the library has an Arduino IDE extension that automates the process. The basic idea could also be adapted to different environments should anyone wish to take up the challenge.
You probably wouldn’t want debug builds to feature this additional payload as writing it to flash will eat up time and write cycles. But for a release build that will be put out in the (literal) field for a few years or even decades, it could be very convenient. After all, you never know when that Git repository that you relied on might go AWOL.
