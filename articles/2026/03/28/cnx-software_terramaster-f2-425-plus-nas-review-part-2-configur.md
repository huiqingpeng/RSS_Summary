---
title: "TerraMaster F2-425 Plus NAS review – Part 2: Configuration, benchmarks, and AI-enhanced media storage"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/28/terramaster-f2-425-plus-nas-review-part-2-configuration-benchmarks-and-ai-enhanced-media-storage/"
published: "2026-03-28"
fetched: "2026-03-29T07:00:17.557452"
---

I received the TerraMaster F2-425 Plus 3+2 Hybrid NAS for review last month, and after checking out the hardware in the first part of the review, I’ve finally had time to test the Intel N150 NAS.
After installing two 4TB SATA drives and an M.2 NVMe SSD, I’ll report my experience setting up the system with the TNAS Android app, before running some benchmarks, and testing features like photo backup with AI search capabilities.
Hard drive installation
I already had an old, but little-used, 4TB HGST SATA drive, and I bought a “new” 4TB SATA drive online for a pretty good deal (2979 THB or a little over $90 US). It turns out the HPE MB4000GVY2K drive I got was refurbished, having been manufactured in 2017. However, it’s an enterprise-grade drive, and the TNAS app reports it has been used “only” for 2,517 hours, so I don’t feel too bad about it. Nonetheless, installing the drives in the trays was super easy, and it doesn’t even require any screws, as the SATA drives just clip into the trays.
After that, I could slide the drives into the unit, and that’s it.
In the first part of the review, I also installed a 256 GB Apacer AS2280P4 NVMe SSD. This requires opening the device. It supports up to 3 NVMe 2280 drives.
The plan is to use the two SATA drives for data storage and the NVMe SSD as cache for improved performance.
Initial TerraMaster F2-425 Plus setup with the TNAS mobile app
I connected the F2-425 Plus to a 2.5GbE switch, an HDMI display to monitor the installation, and the provided 12V/3.33A power adapter. Since the NAS features 5GbE ports, I’ll also connect it to an iKOOLCORE R2 Max mini PC with two 10GbE ports for part of the testing. I don’t have 5GbE/10GbE clients, and 2.5GbE networking should be mostly fine for this review since I’ll be using SATA drives instead of NVMe SSDs for data storage.
I installed the TNAS mobile app on my Android smartphone (it’s also available on iOS), and I could immediately see the TNAS device. Note that no registration is required at this stage. Tap the detected device will bring us to the “TNAS initialization starting soon” window. Most people can tap the “Start Now” button at this stage to get started with the initialization. However, people wanting more control should perform the initialization through a web browser by typing the IP address of the NAS.
After a few seconds, we are warned that the data on the hard drives will be erased. We can confirm to continue the TNAS installation. It will take a few minutes, and the TNAS will now show as being “Not configured” instead of “Uninitialized”.
Nothing much happens in the app during the installation, so you may consider monitoring the progress on an HDMI display.
You’ll then be asked to configure the superuser (root) and, optionally, configure a security email. I tried to do that twice, but I never received the email after tapping “Send code”. So I just skipped the email part.
The app will then ask us to create a storage pool and volume. The process starts right after tapping the “Create New” button. Note that I was not asked which file system or RAID configuration to select. The app decided to use the recommended settings: TRAID (TerraMaster RAID, similar to RAID1) and BTRFS file system. You’d need to use the web interface to have more control. The NAS is going through the synchronization stage, which takes a lot of time. It started at about 14h20, and seven hours later (21h20), 85% of the synchronization was done. As I understand it, the NAS can still be used during that time, but performance will be impacted.
So I went to bed, and synchronization was complete when I checked again in the morning. I also noticed SMB was enabled by default, so the NAS can be used normally at this stage. The guest account is disabled by default, and you can connect with the username/password set during initialization.
Benchmarking T2-425 Plus with iozone3
One reader recommended the NAS performance tester for testing SAMBA/NAS performance, and while it does look neat, it’s a Windows utility. I’ll be using an UP Xtreme i11 Edge mini PC running Ubuntu 24.04 as a headless machine connected over SSH, so instead, I’ll go with iozone3.
I mounted the share as follows:
|
1 2 3 |
mkdir nas sudo mount -t cifs //tnas.local/public nas -o user=cnxsoft,vers=3.0,uid=$(id -u),gid=$(id -g),file_mode=0664,dir_mode=0775 cd nas |
First NAS benchmark with the default configuration
I ran iozone3 twice:
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 |
devkit@UPX-i11:~/nas$ sudo iozone -e -I -a -s 1000M -r 4k -r 16k -r 512k -r 1024k -r 16384k -i 0 -i 1 -i 2 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 1024000 4 13532 12779 9968 9952 9938 13452 1024000 16 51545 51681 43192 43505 36133 48762 1024000 512 109226 105306 226981 227797 222911 103757 1024000 1024 108894 109036 248008 246911 240753 110935 1024000 16384 108491 111459 279615 279611 272220 113421 devkit@UPX-i11:~/nas$ sudo iozone -e -I -a -s 1000M -r 4k -r 16k -r 512k -r 1024k -r 16384k -i 0 -i 1 -i 2 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 1024000 4 13957 13921 9959 9953 9942 13392 1024000 16 47494 46413 36131 35931 43550 45690 1024000 512 111619 109462 229434 230178 224205 108378 1024000 1024 108191 113373 250590 250532 243034 111295 1024000 16384 111192 112473 279637 279584 272327 113240 iozone test complete. |
This allows us to test random I/O and sequential performance for small and larger read/writes. Both results are similar, and we got 279 MB/s sequential read speed and 111 MB/s sequential write speed. The sequential speed is close to the 2.5GbE limit.
The idea was to now use the SSD for caching. However, I noticed this was not possible since the storage pool includes both the two HDDs and the SSD.
So I had to remove the SSD from the storage pool. How to do that? Delete the volume, delete the pool, and re-create it in the web interface using only the two SATA drives. Yes, that’s also meant I had to go through the long synchronization cycle again before testing further. It took 15 hours this time around, and I received a notification email at 3 am once complete.
Enabling Hyper Cache
But at least I can now enable Hyper Cache on the SSD. The “Create now” button in the “Hyper Cache” section used to be grayed out when the SSD was part of the storage pool, but I can now click it.
We are first asked to select the volume to cache. We only have Volume 1, so we’ll select that one.
We can now select the SSD(s). We only have one, so we have to default to “Single Disk”. People using 2 or more SSDs can configure these in RAID1 mode for caching when the more aggressive caching mode is selected. More on that below.
We are now asked to enter the admin password, and this is followed by a warning recommending that the user use a heatsink on the SSD(s) used for caching. That’s already the case here, so we are all good.
The next step requires the user to select the Cache mode.
Two cache modes are available.
- Balanced Mode: This mode provides preloaded read cache acceleration. The data will be written to the SSD cache and the disk at the same time; the data writing speed will be reduced to a certain extent, but the reading speed can be improved. Balanced mode can avoid the risk of data loss due to SSD failure or power failure; In this mode, the cache speed can be increased by using 2 SSDs to form a RAID 0 array. Balanced mode is suitable for users who do not have high requirements for write cache performance but high requirements for read cache performance.
- Read-Write Mode: This mode provides both read and write cache acceleration. The data will be written to the SSD cache first, and then written to the disk later.
The disadvantage of the read-write mode is that it is not safe enough, and the data may be lost once the SSD fails or unexpectedly loses power; if you need to improve the read-write mode security, you can use multiple SSDs to form a RAID 1 or RAID 5 array to provide redundancy for the cache SSD, which not only increases the cache capacity, but also avoids the risk of data loss caused by SSD. The read-write mode is suitable for users who have high requirements for cache read and write performance.
I went with Read-Write mode for maximum performance, but the user can change that to Balance mode later on. Changing the mode would require deleting the SSD from the Hyper Cache and restarting the configuration wizard, but it only takes a minute or two, contrary to the synchronization process for a TRAID volume.
We can now check the settings summary before clicking the Confirm button and completing Hyper Cache configuration.
Benchmarks with Hyper Cache
Now that Hyper Cache is active, we can test the NAS performance again:
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 |
devkit@UPX-i11:~/nas$ sudo iozone -e -I -a -s 1000M -r 4k -r 16k -r 512k -r 1024k -r 16384k -i 0 -i 1 -i 2 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 1024000 4 10602 10634 12394 12316 12367 10367 1024000 16 45987 45974 50823 51692 51032 43376 1024000 512 182182 162276 231201 229940 223977 186587 1024000 1024 195477 162025 248498 247597 244371 176801 1024000 16384 199274 197573 276073 278447 253211 207863 devkit@UPX-i11:~/nas$ sudo iozone -e -I -a -s 1000M -r 4k -r 16k -r 512k -r 1024k -r 16384k -i 0 -i 1 -i 2 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 1024000 4 10700 10646 12553 12547 12410 10682 1024000 16 44174 46111 51368 51125 51095 44123 1024000 512 207391 171709 232894 231049 221896 193709 1024000 1024 176331 191974 248067 246811 222067 211697 1024000 16384 212672 245361 279075 279201 262259 175627 |
Let’s compare some of the results using 2x HDD + 1x SSD in a storage pool against 2x HDD + SSD cache.
| 2x HDD + SSD pool | 2x HDD pool + SSD cache | |
|---|---|---|
| Sequential read (16M) | 279 MB/s | 277 MB/s |
| Sequential write (16M) | 110 MB/s | 206 MB/s |
| Random read (4K) | 9.9 MB/s | 12.4 MB/s |
| Random write (4K) | 13.4 MB/s | 10.5 MB/s |
It helps a lot with sequential writes, but the benefits are limited/inexistent for other workloads. I would have thought random I/Os would benefit the most here, but maybe the CIFS protocol introduces overheads with random I/Os.
Sequential reads are mainly limited by the 2.5Gbps Ethernet bandwidth, but I understand the F2-425 Plus supports link aggregation, so I’ll connect the second RJ45 port to the same switch and run iozone3 on both the UP Xtreme i11 Edge and a laptop connected to an RTL8169BG 2.5GbE to USB 3.0 dongle.
First, I had to configure Link Aggregation/Bond in the Network->Interface section of the web dashboard.
We can see that the two LAN ports are connected as expected. We can now click on the “Create Bond” icon to select the Bond mode for link aggregation. I went with “Adaptive load balancing”.
After clicking Next, we get a summary of the bond, and we can click Next again to complete the setup.
We can now see a single Bond 1 with an IP address using two physical interfaces.
I repeated the test on the UP Xtreme i11 Edge and…
|
1 2 3 4 |
devkit@UPX-i11:~/nas$ sudo iozone -e -I -a -s 10000M -r 16384k -i 0 -i 1 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 10240000 16384 152470 85458 144782 193194 |
.. my laptop in a separate directory on the SAMBA share:
|
1 2 3 4 5 6 |
jaufranc@CNX-LAPTOP-5:~/nas/testdir$ sudo iozone -e -I -a -s 10000M -r 16384k -i 0 -i 1 random random bkwd record stride kB reclen write rewrite read reread read write read rewrite read fwrite frewrite fread freread 10240000 16384 173275 102417 105138 149325 iozone test complete. |
The combined read speed is about 249 MB/s, and the combined write speed is around 325 MB/s. The latter is greater than what’s possible over a single 2.5GbE connection, so link aggregation helps when multiple clients are involved.
That’s an average performance for a 10GB file. I also took a screenshot of the Resource Monitor with Disk I/O showing up to 500 MB/s and Network I/O up to 900 MB/s. The latter corresponds to about 7.2 Gbps, which makes no sense on a dual 2.5Gbps Ethernet bond, so don’t always believe the data reported by the Resource Monitor…
The TerraMaster F2-425 Plus supports 5GbE networking, so I also connected it to an iKOOLCORE R2 Max system with two 10GbE ports and two 2.5GbE ports.
The QWRT image on the mini PC ships without CIFS and NFS file systems, so due to time limitations, I tested raw network performance with iperf3:
- Download – R2 Max to TNAS
|
1 2 3 4 5 6 7 8 9 10 |
root@QWRT:~# iperf3 -t 60 -c 192.168.4.142 -i 10 Connecting to host 192.168.4.142, port 5201 [ 5] local 192.168.4.1 port 58572 connected to 192.168.4.142 port 5201 [ ID] Interval Transfer Bitrate Retr Cwnd [ 5] 0.00-10.01 sec 5.49 GBytes 4.71 Gbits/sec 0 1.28 MBytes [ 5] 10.01-20.01 sec 5.48 GBytes 4.71 Gbits/sec 0 1.28 MBytes [ 5] 20.01-30.01 sec 5.48 GBytes 4.71 Gbits/sec 0 1.90 MBytes [ 5] 30.01-40.01 sec 5.47 GBytes 4.70 Gbits/sec 0 1.90 MBytes [ 5] 40.01-50.01 sec 5.48 GBytes 4.71 Gbits/sec 0 1.90 MBytes [ 5] 50.01-60.01 sec 5.48 GBytes 4.71 Gbits/sec 0 1.90 MBytes |
- Upload – TNAS to R2 Max
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 |
root@QWRT:~# iperf3 -t 60 -c 192.168.4.142 -i 10 -R Connecting to host 192.168.4.142, port 5201 Reverse mode, remote host 192.168.4.142 is sending [ 5] local 192.168.4.1 port 57928 connected to 192.168.4.142 port 5201 [ ID] Interval Transfer Bitrate [ 5] 0.00-10.01 sec 5.49 GBytes 4.71 Gbits/sec [ 5] 10.01-20.01 sec 5.48 GBytes 4.71 Gbits/sec [ 5] 20.01-30.01 sec 5.48 GBytes 4.71 Gbits/sec [ 5] 30.01-40.01 sec 5.48 GBytes 4.71 Gbits/sec [ 5] 40.01-50.01 sec 5.48 GBytes 4.71 Gbits/sec [ 5] 50.01-60.01 sec 5.48 GBytes 4.71 Gbits/sec - - - - - - - - - - - - - - - - - - - - - - - - - [ ID] Interval Transfer Bitrate Retr [ 5] 0.00-60.06 sec 32.9 GBytes 4.70 Gbits/sec 1 sender [ 5] 0.00-60.01 sec 32.9 GBytes 4.71 Gbits/sec receiver iperf Done. |
- Full-duplex (bidirectional)
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 |
root@QWRT:~# iperf3 -t 60 -c 192.168.4.142 -i 10 --bidir Connecting to host 192.168.4.142, port 5201 [ 5] local 192.168.4.1 port 53300 connected to 192.168.4.142 port 5201 [ 7] local 192.168.4.1 port 53312 connected to 192.168.4.142 port 5201 [ ID][Role] Interval Transfer Bitrate Retr Cwnd [ 5][TX-C] 0.00-10.01 sec 5.46 GBytes 4.68 Gbits/sec 0 2.43 MBytes [ 7][RX-C] 0.00-10.01 sec 5.47 GBytes 4.70 Gbits/sec [ 5][TX-C] 10.01-20.01 sec 5.47 GBytes 4.70 Gbits/sec 0 3.33 MBytes [ 7][RX-C] 10.01-20.01 sec 5.47 GBytes 4.70 Gbits/sec [ 5][TX-C] 20.01-30.01 sec 5.47 GBytes 4.70 Gbits/sec 0 3.33 MBytes [ 7][RX-C] 20.01-30.01 sec 5.47 GBytes 4.70 Gbits/sec [ 5][TX-C] 30.01-40.01 sec 5.47 GBytes 4.70 Gbits/sec 0 3.33 MBytes [ 7][RX-C] 30.01-40.01 sec 5.47 GBytes 4.70 Gbits/sec [ 5][TX-C] 40.01-50.01 sec 5.47 GBytes 4.70 Gbits/sec 0 3.33 MBytes [ 7][RX-C] 40.01-50.01 sec 5.47 GBytes 4.70 Gbits/sec [ 5][TX-C] 50.01-60.01 sec 5.47 GBytes 4.70 Gbits/sec 0 3.33 MBytes [ 7][RX-C] 50.01-60.01 sec 5.47 GBytes 4.70 Gbits/sec - - - - - - - - - - - - - - - - - - - - - - - - - [ ID][Role] Interval Transfer Bitrate Retr [ 5][TX-C] 0.00-60.01 sec 32.8 GBytes 4.70 Gbits/sec 0 sender [ 5][TX-C] 0.00-60.06 sec 32.8 GBytes 4.69 Gbits/sec receiver [ 7][RX-C] 0.00-60.01 sec 32.8 GBytes 4.70 Gbits/sec 0 sender [ 7][RX-C] 0.00-60.06 sec 32.8 GBytes 4.70 Gbits/sec receiver iperf Done. |
This part works great. I also quickly checked link aggregation with two 5GbE connected and it also worked, but I don’t have the hardware to test performance for that one.
I did check rsync performance, but SSH encryption limits the performance to around 160 MB/s when transferring a 2GB test file:
|
1 2 3 4 5 6 7 8 9 |
root@QWRT:~# rsync -av --progress -e "ssh -p 9222" --no-compress /tmp/testfile cnxsoft@192.168.4.101:/Volume1/test1 cnxsoft@192.168.4.101's password: sending incremental file list testfile 2,147,483,648 100% 161.66MB/s 0:00:12 (xfr#1, to-chk=0/1) sent 2,148,008,034 bytes received 35 bytes 116,108,544.27 bytes/sec total size is 2,147,483,648 speedup is 1.00 |
Multimedia file synchronization and AI search
One advantage of recent NAS is their media backup and AI file search capabilities that could potentially replace online services like Google Photos. So I enabled Album Backup in the TNAS app. Note that I also had to log in again to the F2-425 Plus since the TNAS app views it as a different device after link aggregation/bonding is enabled.
I have close to 5000 photos on my phone, so it took a while. I also noticed that when the phone is sleeping, backup will stop. So I enabled “Allow background activity”, and waited until the morning. But the backup had stopped. It appears it will only work if the phone is active (display on), whether I use the TNAS app in the foreground or not.
I eventually decided to leave the TNAS app running in the foreground to complete the backup. But I eventually realized the backup does happen in the background even if I don’t use the app, as long as my phone is active (display on). At that point, I also decided to enable “Smart Photo Management”.
As the app was installing, I decided to go to the Media Index, and I was told to enable Media Indexing to use the feature… which I did.
At first, I noticed many thumbnails were missing, but that’s because thumbnail generation was in progress. I could only confirm that after checking the web dashboard. The TNAS Mobile app is great to use on the go (or on the bed), but the web dashboard is what you want for maximum options and details…
Anyway, I just had to be patient, and all thumbnails were eventually generated. The Personal Space in the Media Index section allows the user to browse photos and sort them by name, time, and size, but the built-in search function is all but useless. That’s probably why there’s a separate “Smart Photo Management” we’ve just installed. You’ll also want to enable People and/or Scene AI recognition if you want to make the search useful.
It will run a process in the background to perform AI recognition on all your photos. If you go to the People section, you can add names to recognized persons and merge duplicates. The number under each person shows the number of photos for a given person.
The Scene section will sort the image with terms like Sea, River, Beach, Selfie, and so on. It’s not perfect, but it does a good enough job to help people quickly find relevant images.
The thumbnail on the Beach section above looks bad (since it’s not a beach at all), but clicking on Beach confirms most of the photos are indeed beach-related. The River section is not quite as good, with many roads listed as rivers…
I was less impressed by the search function. First, it’s case sensitive. So search for “river” won’t return any results, but “River” will. It makes no sense here, so hopefully the company will fix that. I also have a few photos with boats, but searching for “Boat” or “boat” didn’t return anything, and I eventually found out my canoe photos are classified as “Ship”. The search function would benefit from AI enhancements to better manage synonyms. If you have many photos, videos, or files and pay for Google Photos/Drive, it can be a replacement, but not a perfect one. Note that the backed-up photos and videos are all private in your “Personal Space” and won’t show in the SAMBA share at all. There’s also a “Public Space” if you need to provide access to guests.
TerraMaster F2-F425 Plus remote access
So far, we’ve done everything in the LAN. But users may want to back up their photos when on holiday or even back up important files while working on the go. TerraMaster provides remote access through TNAS.online. We haven’t used any online accounts so far, but that part requires a TerraMaster account to which you can assign your TNAS ID, provided in the TOS 6.0 interface.
The web interface reports that you can use remote access with TNAS PC for Windows or Mac, or TNAS Mobile for Android or iOS.
No Linux in that list, but actually going to the download section, I can also see a TNAS PC for Linux, which I installed on my Ubuntu 24.04 laptop.
You’ll need your TNAS ID and local username/password to log in to the NAS. I initially did that in the local network. The connection method reads “Local Connection”.
I then switched to another LAN, and had to log in again, and this time it showed “TRT connection”.
Most icons simply redirect to links with https://
After installation, we can access the TerraSync link and a”My File” folder with a TerraSync folder.
At this point, we can go back to the TNAS PC app and access the TerraSync Servers section to add a server using the TNAS ID (abcdef), but that part didn’t work for me, as the program complained that the TOS version was too low. It requires TOS 6.0.770 or greater. Just a little problem, my F2-425 Plus already runs TOS 6.0.794…
When trying the full tnas-id.tnas2.link in the Server address field, the program reports a failure to connect instead, so I’m pretty sure the TNAS ID method is the right way to go. It looks like the TNAS PC for Linux may be a little buggy. Another method to sync data from my laptop would be to set up an rsync server. I haven’t done it yet due to time constraints.
What I did try was to connect to the NAS remotely through a data connection from my smartphone’s cellular data connection. We need to add the NAS manually, and while we’re told to enter the TNAS ID or URL domain, the first method does not work, and I had to type https://tnas.online/
When we browse photos with the app or web dashboard with remote access, it will show lower resolution photos to speed up downloads, but the user can also tap/click to download the full resolution image.
Conclusion
The TerraMaster F2-425 Plus has a solid hardware design, and the software works well enough that I’ll probably keep using it at home for my storage needs.
It can serve the needs of a range of users with a dual 3.5-inch SATA bay for traditional hard drives and three NVMe SSD slots for users requiring higher performance. The SSD(s) can also be used as a cache for the hard drives to significantly speed up write speed. I ended up using two 4TB SATA hard drives in TRAID (RAID1) configuration and one 256GB NVMe SSD for “Hyper Cache”, and the system performed adequately (up to about 300MB/s read/write over SAMBA) using 2.5GbE networking and link aggregation of the two RJ45 ports. Note the F2-425 Plus features two 5GbE ports, but I only have the proper setup for 2.5GbE networking, and the higher speed is best suited for NVMe storage.
I also tried the media storage capability, such as automatic photo/video backup and the AI search function. It’s not quite as smooth as using an online service like Google Photos, but it mostly does the job by synchronizing your phone’s media files with the NAS automatically. AI search is not enabled by default for privacy reasons, but the user can enable People and Scene AI recognition in the settings. The main weak point is the search function. It works, but it’s case-sensitive, and it does not handle synonyms at all. For example, “Ship” will return photos, but “ship”, “Boat”, “Canoe”, or other similar terms will not return any photos.
Remote access can also be enabled relatively easily, and I could access the NAS from outside the LAN using both my phone and computer. However, when I wanted to enable TerraSync to sync some of my laptop’s files with the NAS, the TNAS PC for Linux program failed to work properly. Your experience may differ on Windows or macOS. I’ll probably use a different method (rsync) if I want to sync data between my laptop and the NAS, either locally or over the Internet.
I’d like to thank TerraMaster for sending the F2-425 Plus NAS for review and sponsoring one of the 4TB drives for testing. The 2-bay hybrid NAS is currently sold on Amazon for $399.99. That price looks to be a time-limited promotion until March 31, after which it might go back to the $499.99 price tag. It’s also available on the TerraMaster store for the same price, and you can also try to use the coupon code “CNXSOFT” to get an additional 10% discount.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
