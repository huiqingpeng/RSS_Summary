---
title: "Blues Notecard for Skylo IoT module offers 5G NTN satellite, NB-IoT/LTE-M cellular, WiFi, and GNSS connectivity"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/blues-notecard-for-skylo-iot-module-offers-5g-ntn-satellite-nb-iot-lte-m-cellular-wifi-and-gnss-connectivity/"
published: "2026-03-11"
fetched: "2026-03-12T07:00:49.390333"
---

Blues Notecard for Skylo is an IoT module combining subscription-free 5G NTN satellite, NB-IoT or LTE-M cellular, WiFi, and GNSS connectivity for asset tracking applications in transportation and logistics, energy, and commercial equipment.
provides an all-in-one satellite IoT solution that doesn’t require additional hardware or a satellite subscription contract. By default, the module connects over WiFi and switches to cellular when out of range. It only falls back to pay-as-you-go Skylo satellite connectivity when neither WiFi nor cellular connectivity is available, and ensures IoT connectivity at most times.
Blues Notecard for Skylo (NOTE-NBGLWX) specifications:
- Modem – Quectel BG95-S5 NTN satellite + LTE IoT communication module
- Data Networks – LTE-M, NB-IoT, GPRS, Skylo
- SIM card – Embedded MFF2 SIM, external SIM switch
- Data included
- Cellular: 500MB valid for 10 years
- Skylo: 10KB; enough to send 1 message a day for 6 months. Additional data is priced at $0.00075 per byte, with a minimum of 50 bytes per transmitted or received satellite data packet
- Cellular coverage – It’s complicated and depends on the region/country. Check the documentation below.
- GNSS – GPS, GLONASS, BeiDou, Galileo, QZSS
- WiFi Module – Silicon Labs WFM200S Wi-Fi Transceiver Module
- Antennas
- MAIN u.FL connector for both cellular and satellite communications
- GPS u.FL connector for GNSS
- Onboard ceramic antenna for WiFi
- Sensor – LIS2DTW accelerometer used to detect motion (and turn off GNSS when stationary).
- Host Interface – I2C, UART, or USB; support 1.8V or 3.3V MCUs
- Security
- Integrated STSAFE Secure Element with hardware crypto
- True hardware random number generator
- Factory-installed ECC P-384 certificate, provisioned at chip manufacture (valid until November 16, 2047)
- Dimensions – 42 x 30mm
While you’d eventually integrate the Notecard for Skylo into your own design, you can quickly get started with compatible NOTECARRIER boards such as the ones shown below.
Packets (“Notes”) transferred by the Notecard can be tagged with time (GPS or Cellular) and location (GPS). The data is securely transmitted to the cloud, and the module is optimized to save power with low idle current consumption.
All instructions to get started, and additional information (e.g., coverage), can be found on the online datasheet. While it’s probably best to get a module and carrier board, you don’t need one to evaluate the cloud platform since a simulator is provided. The datasheet also includes an in-browser terminal. Note that Firefox is not working since it requires WebSerial, so you’d need to use Chrome, Opera, or Edge, or download the Notecard CLI.
It’s not the first time we’ve come across an IoT module with Skylo NTN satellite support, and the Blues Starnote and Quectel CC660D-LS are some earlier examples. The new Notecard for Skylo is unique as it implements 5G NTN satellite, NB-IoT/LTE-M cellular, WiFi, and GNSS connectivity into a single module.
Contrary to most other products introduced at Embedded World 2026, the Notecard for Skylo is available for purchase for $89 on the Blues store, and the Notecarrier-F board is available as a $25 option. The press release may have a few more details.
Thanks to TLS for the tip.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
