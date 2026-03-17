---
title: "Mini review of the ThinkNode M6 “outdoor solar power for Meshtastic”"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/17/review-thinknode-m6-outdoor-solar-power-for-meshtastic/"
published: "2026-03-17"
fetched: "2026-03-18T07:00:59.687411"
---

Elecrow has sent us a solar-powered ThinkNode M6 Meshtastic device for review. Last year, I reviewed the ThinkNode M1 and M2 Meshtastic nodes, and I was a bit disappointed by the point-to-point range in a suburban environment, where I got about 550 meters of range after switching to LONG SLOW mode.
Nine months have passed since that review, and there still doesn’t seem to be any Meshtastic community in the second-largest city in Thailand, probably because typical Meshtastic terminals are more expensive than entry-level Android smartphones, have limited functionality, and the mobile app is still a mess despite a revamp. Nevertheless, when Elecrow asked me whether I wanted to test the “ThinkNode M6 outdoor solar power for Meshtastic”, I thought it might be fun. The main purpose of this mini review is to check the range I get using the M6 as a router between the M1 and M2 nodes.
Elecrow ThinkNode M6 unboxing
I received the device in a cardboard package reading “ThinkNode M6 Meshtastic Device” and “Outdoor Solar Power” with a 6W panel. The top right stick mentioned the frequency band: 915 MHz, exactly what I need for Thailand (AS923). Note there’s also a version without Meshtastic firmware, to which you can install the firmware yourself.
The bottom side lists the key specifications (I added the missing part):
- SoC – Nordic Semi nRF52840 BLE microcontroller
- Wireless
- Bluetooth 5.4 LE
- LoRa – 915 MHz (US) or 868 MHz (EU)
- Expansion – UART and I2C waterproof connectors for optional sensors
- Misc – Power (Red) and data (Blue) LEDs
- Power Supply
- 5V/1A via USB-C port
- 6W panel
- 7,000 mAh 18650 Lithium-ion battery
- Dimensions – 210 x 156 x 42 mm excluding antenna and bracket
- Temperature Range – Operating: -20 to +60°C; storage: -30 to +70°C
- IP Rating – IP65
We’ll find the unit, GPS and LoRa (915 MHz) antennas, a USB-C cable for charging, a wall mount with screws and wall anchors, and a basic user manual.
The bottom side features the two LEDs, the USB-C port, and I2C/UART connectors with waterproof covers, as well as rails for the wall mount.
I then installed the LoRa antenna on the left side and the GPS antenna on the right side, as shown in the photo below with the unit upside down.
I’d usually go through a teardown at this point, and I attempted it with the ThinkNode M6, but eventually gave up, as there does not seem to be a non-destructive way to open the unit. All I could do was to remove the bottom cover, and it didn’t get me very far.
ThinkNode M6 configuration and range test
I noticed the data LEDs were active when I took the unit out of its package, so I didn’t even charge it and started to use it straightaway.
The ThinkNode M6 was detected as Meshtastic_4c93 device, which I could pair using the 123456 pairing code. After that, I configured LoRa to use Thailand and LONG_SLOW preset. I also enabled Precise location in the LongSlow channel.
The ThinkNode M1 and M2 were also configured the same way, but somehow the three devices could not see each other. I could get M1 and M2 shows or the M6 show, but not all three together.
I eventually figured out that it was because the Frequency slot was different (M1/M2 set to 27, while the M6 was set to 31), so I changed that, and I also switched the M6 mode to ROUTER mode. All three devices could be seen together.
Note that the ThinkNode M6 can also be used as a normal CLIENT attached to a smartphone, and Elecrow did just that to test the range between two ThinkNode M6, where they got over 6 kilometers between the two. However, the test was made from strategic locations along a meandering river with a direct line of sight.
My range test is a little different. We drove to a stadium, parked there, and placed the ThinkNode M6 on top of the car, unattended (Thailand is a civilized country).
The initial plan was for us to walk in opposite directions, one with the M1, the other with the M2, but finally, we changed our minds and decided to leave the M1 inside the car and walk together carrying the M2 device. I sent messages along the way with the names of the locations and did so until sending failed.
We walked for about 2 kilometers, and the distance between the car and the NACC provincial office is about 1.6km. It started to get dark, so we stopped testing at this stage, but in theory, that means the ThinkNode M6 can provide connectivity within a 3.2km diameter circle. That’s about six times the range we had when using P2P connectivity with only the M1 and M2 nodes.
I had also planned to install the ThinkNode M6 on a solar light pole for even a long range, but I could not find an easy and secure way to install it. I wish the kit would ship with a pole mount as well, instead of just a wall mount.
I’d like to thank Elecrow for sending the ThinkNode M6 Meshtastic device for review. It sells for $79.90 on the Elecrow store. While you’ll find the device on AliExpress ($86.39) and Amazon ($99) too, it’s usually without Meshtastic firmware, and if you prefer to have the M6 preloaded with Meshtastic, the Elecrow store is the only option for now.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
