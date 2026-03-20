---
title: "Enabling MediaTek M7902 WiFi and Bluetooth drivers on Ubuntu 24.04 the easy way"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/"
published: "2026-03-20"
fetched: "2026-03-20T16:03:07.227065"
---

Last month, we noted that Mediatek MT7902 WiFi 6E and Bluetooth 5.x chipset finally got drivers in mainline Linux, and should be part of the Linux 7.0 release.
MT7902 wireless modules are used in many Windows laptops, but users have been asking for the Linux drivers for almost two years now. One method is to wait for the drivers to find their way into your distribution, but “hmtheyboy154” didn’t feel like waiting and backported the drivers to Linux 6.6 to 6.19. Since I own one of those laptops, namely the ASUS Vivobook 16, I gave it a try on Ubuntu 24.04, but it should work on other Linux distributions as well.
Note that this method only works with the PCIe driver, so if you own an SDIO module, you’d need to work out another solution. My Ubuntu 24.04 laptop is indeed using an MT7902 PCIe module (AW-XB552NF):
|
1 2 |
jaufranc@CNX-LAPTOP-5:~$ lspci | grep 7902 0000:02:00.0 Network controller: MEDIATEK Corp. Device 7902 |
I could install the driver in four steps:
|
1 2 3 4 |
git clone https://github.com/hmtheboy154/mt7902 cd mt7902/ make -j8 sudo make install |
You can optionally install the firmware, although it might already be part of your distribution:
|
1 |
sudo make install_fw |
After that, you could reboot your laptop, but I used modprobe instead:
|
1 |
sudo modprobe mt7902e |
I could then enable WiFi on Ubuntu 24.04 and connect to my access point.
The kernel log should look something like that:
|
1 2 3 4 5 6 7 8 9 10 11 12 |
[1014428.026033] wlo1: deauthenticating from 3c:cd:57:f5:af:91 by local choice (Reason: 3=DEAUTH_LEAVING) [1014439.871042] mt7902e 0000:02:00.0: ASIC revision: 79020000 [1014439.966746] mt7902e 0000:02:00.0: HW/SW Version: 0x8a108a10, Build Time: 20251212032046a [1014439.988460] mt7902e 0000:02:00.0: WM Firmware Version: ____000000, Build Time: 20251212032127 [1014440.940270] mt7902e 0000:02:00.0 wlo1: renamed from wlan0 [1014443.452779] wlo1: authenticate with 3c:cd:57:f5:af:91 (local address=10:68:38:3a:0d:da) [1014443.452797] wlo1: send auth to 3c:cd:57:f5:af:91 (try 1/3) [1014443.467182] wlo1: authenticated [1014443.468008] wlo1: associate with 3c:cd:57:f5:af:91 (try 1/3) [1014443.507278] wlo1: RX AssocResp from 3c:cd:57:f5:af:91 (capab=0x511 status=0 aid=3) [1014443.543479] wlo1: associated [1014443.545773] wlo1: Limiting TX power to 27 (30 - 3) dBm as advertised by 3c:cd:57:f5:af:91 |
I still did a quick iperf3 test with 5 GHz WiFi, about 2 meters from a Xiaomi Mi Router AX6000.
- Download
1234567891011121314151617jaufranc@CNX-LAPTOP-5:~$ iperf3 -t 60 -c 192.168.31.12 -i 10 -RConnecting to host 192.168.31.12, port 5201Reverse mode, remote host 192.168.31.12 is sending[ 5] local 192.168.31.152 port 41870 connected to 192.168.31.12 port 5201[ ID] Interval Transfer Bitrate[ 5] 0.00-10.01 sec 528 MBytes 443 Mbits/sec[ 5] 10.01-20.01 sec 530 MBytes 444 Mbits/sec[ 5] 20.01-30.01 sec 477 MBytes 400 Mbits/sec[ 5] 30.01-40.01 sec 484 MBytes 406 Mbits/sec[ 5] 40.01-50.01 sec 432 MBytes 362 Mbits/sec[ 5] 50.01-60.01 sec 493 MBytes 414 Mbits/sec- - - - - - - - - - - - - - - - - - - - - - - - -[ ID] Interval Transfer Bitrate Retr[ 5] 0.00-60.01 sec 2.88 GBytes 412 Mbits/sec 23 sender[ 5] 0.00-60.01 sec 2.88 GBytes 412 Mbits/sec receiveriperf Done. - Upload
12345678910111213141516jaufranc@CNX-LAPTOP-5:~$ iperf3 -t 60 -c 192.168.31.12 -i 10Connecting to host 192.168.31.12, port 5201[ 5] local 192.168.31.152 port 35586 connected to 192.168.31.12 port 5201[ ID] Interval Transfer Bitrate Retr Cwnd[ 5] 0.00-10.01 sec 433 MBytes 363 Mbits/sec 0 1.09 MBytes[ 5] 10.01-20.01 sec 547 MBytes 459 Mbits/sec 0 2.43 MBytes[ 5] 20.01-30.01 sec 568 MBytes 477 Mbits/sec 0 2.43 MBytes[ 5] 30.01-40.01 sec 567 MBytes 476 Mbits/sec 0 2.43 MBytes[ 5] 40.01-50.01 sec 566 MBytes 475 Mbits/sec 0 2.43 MBytes[ 5] 50.01-60.03 sec 550 MBytes 460 Mbits/sec 0 2.43 MBytes- - - - - - - - - - - - - - - - - - - - - - - - -[ ID] Interval Transfer Bitrate Retr[ 5] 0.00-60.03 sec 3.16 GBytes 452 Mbits/sec 0 sender[ 5] 0.00-60.04 sec 3.16 GBytes 452 Mbits/sec receiveriperf Done.
About 400-450 Mbps in either direction, which should be fine with a link speed of 600 Mbps, plus my ISP only supports 300 Mbps uploads/downloads.
I also tried Bluetooth, but it didn’t work for me at first, as I couldn’t enable it in the settings. I eventually noticed it just requires a different branch on the same GitHub repo:
|
1 2 3 4 5 6 7 8 |
git clone https://github.com/hmtheboy154/mt7902 -b bluetooth_backport btusb_mt7902 cd btusb_mt7902/ make -j8 sudo make install sudo make install_fw sudo rmmod btusb suydo rmmod btmtk sudo modprobe btusb_mt7902 |
I could then enable Bluetooth, pair my smartphone to the laptop, and transfer a file from my Android phone to the laptop.
Note that the btusb and btmtk modules conflict with btusb_mt7902, so I had to remove them, or I would get the error:
|
1 2 |
jaufranc@CNX-LAPTOP-5:~/btusb_mt7902$ sudo modprobe btusb_mt7902 modprobe: ERROR: could not insert 'btusb_mt7902': Exec format error |
To do that permanently, create the file /etc/modprobe.d/blacklist_btusb.conf with:
|
1 |
blacklist btusb btmtk |
It took a long while to get WiFi and Bluetooth support on Linux for MT7902 modules, but it’s now easy enough to install on Ubuntu 24.04 without waiting for the official release.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
