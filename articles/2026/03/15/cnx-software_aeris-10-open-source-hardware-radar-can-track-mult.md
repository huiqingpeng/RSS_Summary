---
title: "AERIS-10 open-source hardware radar can track multiple objects up to 20km away"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/"
published: "2026-03-15"
fetched: "2026-03-16T07:00:24.190353"
---

AERIS-10 is an open-source hardware, “low-cost” (more on that later) 10.5 GHz phased array radar system featuring Pulse Linear Frequency Modulated (LFM) modulation and based on an AMD Artix-7 FPGA.
Two versions are available: the AERIS-10N (Nexus), providing up to 3km range with an 8×16 patch antenna array, and the AERIS-10X (Extended), offering up to 20km range thanks to a 32×16 dielectric-filled slotted waveguide array.
ARIES-10 key components and features:
- Main board
- FPGA – AMD Artix-7 XC7A100T for:
- PLFM Chirps generation via the DAC
- Raw ADC data read
- Automatic Gain Control (AGC)
- I/Q Baseband Down-Conversion
- Decimation
- Filtering
- Forward FFT
- Pulse Compression
- Doppler, MTI, and CFAR processing
- USB Interface
- MCU – ST STM32F746xx microcontroller for
- Power management
- FPGA communication
- Setup and interface with the components on the main, frequency synthesizer, and power amplifier boards, plus:
- GPS module for GUI map centering
- GY-85 IMU for pitch/roll correction of target coordinates
- BMP180 Barometer
- Stepper Motor
- 8x ADS7830 Temperature Sensors for cooling fan control
- RF switches
- DAC to generate the RADAR Chirps
- 2x LT5552 microwave mixers for up-conversion and IF-down-conversion
- 4x ADAR1000 4-channel phase shifters for Rx and Tx chain beamforming (RADAR pulse sequencing)
- 16x ADTR1107 front-end chips used for both LNA (Rx) and PA (Tx) stages
- FPGA – AMD Artix-7 XC7A100T for:
- Frequency synthesizer board based on an AD9523-1 low-jitter clock generator supplying phase-aligned clock references for:
- RX and TX Frequency Synthesizers (ADF4382)
- DAC, ADC
- FPGA
- 16x power amplifier boards (AERIS-10X version only) with 10Watt QPA2962 GaN amplifier for extended range
- Power management board
- Antenna Arrays
- AERIS-10N (Nexus) – 8×16 patch antenna array
- AERIS-10X (Extended) – 32×16 dielectric-filled slotted waveguide antenna array
- Miscellaneous
- Slip-ring, stepper motors and drivers, cooling fans, and enclosure
- Full electronic beam steering – ±45° electronic steering in elevation and azimuth
The AERIS-10 radar is supported by a Python GUI with a user-friendly interface with real-time target plotting, map integration, and a radar control interface. NawfalMotii79 provides all resources on GitHub, including EAGLE schematics and PCB layout, bill of materials (BoM), Gerber files, and mechanical drawings under a CERN Open Hardware Licence Version 2 – Permissive (CERN-OHL-P), while the FPGA code (VHDL/Verilog), STM32 firmware, and Python GUI and utilities are released under an MIT license. The “/10_docs/” is supposed to contain an assembly guide, but as I write this article, it’s not available in the repository just yet.
The low-cost AERIS-10 radar is designed for researchers, drone developers, and SDR enthusiasts wanting to experiment with phased array radar technology. But what does low-cost mean exactly? We can first get an idea thanks to an X post by chiefofautism that brought the project to my attention, and explains:
Commercial phased array radar starts at $250,000. military surplus is $10,000-50,000 but its decades old analog junk with no electronic beam steering
But we can get a more accurate estimate of the costs thanks to another X post by Daniel Bogdanoff listing the BoM cost for the most expensive parts (in the US):
- 2x LTC5552 = $120 in total
- 4x ADAR1000 phase shifters = $780 in total
- 16x ADTR1107 front end = $3600 in total
- AMD ADTXC7A100T FPGA = ~$200
So that’s about $5,000 in parts for the AERIS-10N, excluding the boards, which may add $1k to $3k. The AERIS-10X model requires 16 QPA2962TR7 power amplifiers at $450 each, so $7200, so you can expect to spend about $13k to $15k in total for the Extended model. So it’s indeed a low-cost radar in relative terms, but it’s probably out of the budget of most people for a weekend project :).
It’s not for sale as a preassembled kit, so you’d have to build it yourself. You’d also need to make sure you have all licenses and authorisations required to operate this type of equipment from your local FCC. Since I’d assume we’re dealing with dual-use commercial/military applications here, you may also want to double-check whether other local authorities are fine with this type of “toy”, as you wouldn’t want the military to pay you house, office, or research lab an unexpected visit.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
