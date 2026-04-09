---
title: "Upgrading a MacBook Neo Using a 1 TB iPhone NAND Flash"
source: "Hackaday"
url: "https://hackaday.com/2026/04/09/upgrading-a-macbook-neo-using-a-1-tb-iphone-nand-flash/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:37.320437"
---

For some reason the newly introduced MacBook Neo appears to be the subject of a lot of modding, though a recent mod by [dosdude1] leans into the fact that this laptop has been assembled using what are effectively iPhone 16 parts inside a laptop case. This consequently means that there’s an overlap with certain iPhone 16 components, such as the NAND Flash. Incidentally storage on the Neo is limited to 512 GB when you purchase it from Apple, which is weird since the same SoC in the iPhone 16 Pro happily uses 1 TB.
Even if it was just a price point thing that Apple went for, there’s seemingly nothing standing between a Neo owner with a hot air gun and sheer determination. As long as you’re comfortable soldering a fine-pitched BGA NAND Flash package, natch.
Of course, there was always the possibility that Apple used a different NAND Flash package footprint, but the installed 256 GB model chip that comes installed matches the replacement 1 TB model K8A5 chip as hoped. This just left disassembly and preparing the PCB for a storage replacement. Removal of the BGA underfill and desoldering the old chip without taking out surrounding SMD parts is definitely the hardest part, but handled in the video with the equivalent of an IC spatula and a temporary removal of some capacitors.
Interestingly, the uncovered IC footprint shows a whole perimeter of unused pads that might target other NAND Flash packages. Regardless, the new chip installed fine, giving the Neo 1 TB of storage and a slightly faster read/write performance.
