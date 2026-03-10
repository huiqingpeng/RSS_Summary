---
title: "Diagnosing a Mysterious Fault with a Commodore 1541 Disk Drive"
source: "Hackaday"
url: "https://hackaday.com/2026/03/09/diagnosing-a-mysterious-fault-with-a-commodore-1541-disk-drive/"
published: "2026-03-10"
fetched: "2026-03-10T15:33:35.403457"
---

Recently [TheRetroChannel] came across an interesting failure mode on a Commodore 1541 5.25″ floppy disk drive, in the form of the activity LED blinking just once after power-up with the drive motor continuously spinning. Since the Flash Codes that Commodore implemented and bothered to document start at 2 flashes (for RAM-related Zero Page), this raised the question of what fault this drive had, and whether a single flash is some kind of undocumented error code.
A cursory check showed that the heads were okay and not shorted, ruling out a common fault with the used floppy mechanism. Cleaning up the corrosion on IC sockets and similar basic operations were performed next, without making a change, nor did removing the ICs to induce it to produce the documented error codes, but this helped narrow down the potential causes. Especially after swapping in known-good ICs failed to make a difference. One possibility was that the drive was boot looping, as the activity LED is lit up once on boot.
Some probing around with an oscilloscope between the faulty and a working drive seemed to point to a faulty RAM IC, but while probing the faulty drive suddenly initialized successfully. After some more poking around it appeared that the drive was fine after it had a chance to warm up, which just deepened the mystery.
The drive did talk to a C64 with diagnostic cartridge at this point, but would often glitch out. Ultimately it appears that a dodgy IC socket and a few bad traces were to blame for the behavior, making it an ‘obvious in hindsight’ repair. The bottom of the PCB had some clear corrosion on it, but the affected traces were apparently still hanging on for dear life with the drive still initializing once warmed up.
