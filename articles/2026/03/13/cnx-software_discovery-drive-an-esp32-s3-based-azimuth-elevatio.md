---
title: "Discovery Drive – An ESP32-S3-based azimuth/elevation rotator for satellite dishes and SDR antennas (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/13/discovery-drive-esp32-s3-based-azimuth-elevation-rotator-for-satellite-dishes-and-sdr-antennas/"
published: "2026-03-13"
fetched: "2026-03-14T07:01:19.921534"
---

KrakenRF, the team behind the KrakenSDR, has designed the Discovery Drive ESP32-S3-based, low-cost, fully weatherproof, automatic azimuth/elevation (Az/El) antenna rotator for their Discovery Dish or other directional antennas, such as Yagis and Wi-Fi grids, weighing up to 5kg.
Compared to DIY projects like SatNOGS (which require 3D printing and hardware sourcing), the Discovery Drive is designed as a plug-and-play solution. You can simply mount it to a mast, attach the dish, connect to 12V power and Wi-Fi, and use its web UI to start tracking polar-orbiting weather satellites (like METEOR-M2 or FENGYUN), CubeSats, or amateur radio satellites.
KrakenRF Discovery Drive specifications:
- Controller – Espressif Systems ESP32-S3-based control board
- Connectivity – 2.4 GHz 802.11 b/g/n Wi-Fi 4 (via ESP32) with external antenna
- Motor and Rotation
- Torque – Up to 125 kg·cm (12.25 Nm); supports antenna payloads up to 5 kg
- Azimuth Range – -360° to +360°
- Elevation Range – 0° to 90°
- Speed – 1.5 RPM (Azimuth); 0.25 RPM (Elevation)
- Accuracy – ± 1.5°
- Drive Mechanism – Worm gear-locked output drives (prevents dropping on power off)
- USB – 6-meter USB Type-C cable for power and data logging
- Misc
- Wind-tracking mode that stows the dish perpendicular to prevailing winds
- Removable compass shelf for north alignment
- Side rails for optional SBC / SDR pod modules
- Power
- 12 V DC (barrel jack or USB-C Power Delivery)
- Consumption
- ~10 W during tracking
- ~1 W idle
- Dimensions – 40 x 20 x 16 cm (15.75″ x 6.3″ x 7.87″)
- Weight – 6.4 kg (14.1 lbs), including the mount
- Mast Compatibility – Supports mast diameters from 2 cm to 50 cm (0.8″ to 19.7″)
- Operating Temperature – -10°C to 40°C (14°F to 104°F)
- Enclosure – IP55-rated weatherproof outdoor housing
The company highlights that the device is very low power (under 10W), and both the Discovery Drive and an SBC/SDR mounted on the device can be powered from a single standard PoE+ (802.3at) supply, which provides up to 25.5W. This means you have about 15W of “headroom” left to power other things on the same cable.
On the software side, the Discovery Drive is compatible with the SDR and Ham radio ecosystem. It supports the rotctl (Hamlib) protocol over TCP/IP and the EasyComm II protocol over serial. This allows it to work out-of-the-box with:
- SatDump / GPredict / Look4Sat: For automated tracking of weather satellites (NOAA, METEOR, etc.) and CubeSats.
- Stellarium: Via the Remote Control plugin for radio astronomy (e.g., mapping the Hydrogen Line).
- Web Dashboard: A built-in browser interface for manual control and firmware updates.
The C++ firmware is open-source and available on GitHub, allowing developers to customize the motion control or integrate new sensors. Detailed assembly, installation, configuration, and usage instructions for the Discovery Drive are available on the project’s wiki.
The device also supports automatic wind-stow protection, firmware updates via web UI, and rails for optional side pods to mount SBCs and RTL-SDR receivers. Applications include weather-satellite reception (e.g., METEOR-M2, METOP, FENGYUN), CubeSat and amateur radio satellite tracking, radio astronomy hydrogen-line mapping, LoRa directional links, radiosonde tracking, Wi-Fi heat mapping, meteor detection, and drone signal monitoring.
The Discovery Drive is currently crowdfunding on Crowd Supply for $699 with free worldwide shipping. The kit includes the Discovery Drive rotator unit, a 6-meter USB-A-to-USB-C cable, a 6-meter 12V DC extension cable, a DC barrel splitter, mast-mounting brackets and bolts, a Wi-Fi antenna, a temporary compass shelf for alignment, a crossbar/antenna mounting bracket, and a 12V universal power supply. Shipping is estimated to begin in August 2026.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
