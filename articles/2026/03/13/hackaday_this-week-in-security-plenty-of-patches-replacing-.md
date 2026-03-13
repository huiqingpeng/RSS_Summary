---
title: "This Week in Security: Plenty of Patches, Replacing Old Gear, and Phrack Calls for Papers"
source: "Hackaday"
url: "https://hackaday.com/2026/03/13/this-week-in-security-plenty-of-patches-replacing-old-gear-and-phrack-calls-for-papers/"
published: "2026-03-13"
fetched: "2026-03-14T07:03:16.916266"
---

When Friday the Thirteenth and Patch Tuesday happen on the same week, we’re surely in for a good time.
Anyone who maintains any sort of Microsoft ecosystem knows by now to brace for impact come Patch Tuesday; March brings the usual batch of “interesting” issues, including:
- Two high-risk Microsoft Office vulnerabilities (CVE-2026-26110 and CVE-2026-26113), both of which allow execution of arbitrary code with no user interaction other than opening a hostile file. Vulnerabilities like these are especially dangerous in environments where transferring Office documents is considered normal, such as (unsurprisingly) offices, but also for home users who may not be savvy enough to avoid opening hostile files. Arbitrary code execution allows the attacker to run essentially any commands the user would be able to run themselves, typically leveraging it to install remote access or keyboard logging malware.
- Excel gets a different vulnerability, CVE-2026-26144, which allows leaking of data through a cross-site scripting vulnerability. Coupled with CoPilot Agent, this can be used to leak contents of spreadsheets, again with no direct user interaction.
On the server and container side, this month includes a fairly typical collection of patches for SQL Server, and vulnerabilities in the Microsoft-hosted device pricing and payment orchestrator services, which have been automatically patched by Microsoft.
When it’s Time to Replace Old Gear
We all love getting every ounce of usability from our old gear, but sometimes enough is enough – at least with the stock firmware. The FBI has issued a warning about decommissioning end-of-life routers made by several large companies, with eleven Linksys and one Cisco branded routers being specifically called out for vulnerabilities under active exploitation.
A notice such as this that an exploit is under active exploitation means that a theoretical vulnerability has been commoditized into specific attacks, typically used against all devices accessible from the Internet. It’s generally safe to assume that at this point, if a vulnerable device is exposed to the Internet, it’s been compromised.
The FBI notice doesn’t call out the specific vulnerabilities used, however there’s a wide variety to pick from:
- CVE-2025-60690 is a simple buffer overflow allowing code execution from parameters passed to the web UI.
- CVE-2025-60692 is a buffer overflow allowing arbitrary code execution from the local network via control of entries in
/proc/net/arp
– unlikely to be used for a remote compromise, but still amusing. - CVE-2025-60694 and CVE-2025-60693 are both additional stack overflow and code execution from web bugs, which sets a real pattern for the quality of the webserver in the stock firmware.
- CVE-2025-60689, CVE-2025-60691 and CVE-2025-34037 however appear to be the most likely culprits, both allowing arbitrary execution on the router without authentication, with CVE-2025-34037 rated a full 10/10 on the vulnerability scale and explicitly mentioning being used to deploy worm firmware.
Once an attacker is inside your router, the possible havoc they might cause is extensive:
- Redirecting requests to malicious or fake websites by taking control of the DNS or rewriting requests at other layers.
- Exposing systems on your private network – such as less secured IoT devices or other local devices with weak internal passwords – to the attackers.
- Using your Internet connection to perform other attacks or pivots. Installing proxies on home equipment is a common method used for international attackers to appear as a normal home user in a target country.
- Reselling your Internet access. Ever wonder how “free” VPN apps are able to offer access in random countries? Often an international VPN is just an infected home user!
- Adding you to a botnet. Some of the largest distributed denial of service (DDoS) attacks have been carried out not by systems with huge bandwidth, but by tens of thousands (or more) of comrpomised small home routers, cameras, and other IoT type devices acting together.
If you have a Linksys E1200, E2500, E1000, E4200, E1500, E3000, E3200, E1550, WRT320N, WRT160N, WRT310N, or a Cisco M10 router still in use, the time is now to finally upgrade it – or at least explore the options of third-party firmware like OpenWRT. Unfortunately, many of these devices are so old that even OpenWRT may have difficulty running well on them, but all the more reason to update to something a little newer!
State-level Exploits in the Wild
In a pattern which should be familiar to anyone who had to deal with the leak of the Eternal Blue exploit as part of a dump of tools from the NSA which later evolved into the Wannacry and NotPetya global ransomware campaigns, another government-backed exploit toolkit has been captured and converted to a more generic criminal exploit.
Google Threat Intelligence documents the “Coruna” exploit kit, a rare public example of an attack against iPhones from iOS 13 to iOS 17.2.1. Often we see “advanced attack methods” or “targeted specific attacks” in release notes; rarely do we get further insight into the actual attacks!
Evolving from a government-backed tool to a financial crimeware exploit deployed widely to steal cryptocurrencies is interesting on its own, but perhaps the most fascinating aspect is the insight into how difficult modern exploits can be. Coruna combines 23 exploits into 5 chained attacks to be able to actually execute code from a web page. The final payload of the exposed version doesn’t deliver a spy payload, but instead focuses on cryptocurrency: searching for QR codes on disk to discover wallet addresses and saved recovery keys, wallet recovery phrases, and mentions of bank accounts, and leveraging those to steal cryptocurrency.
In true Google fashion, they’ve published indicators of compromise (IOCs) to inspect if a device has been attacked and a map of the control domains. Additional work deobfuscating the attacks and payloads can be found on GitHub here.
More Government Warnings
The US Government Cyber Defense Agency (CISA) has added additional warnings to the Known Exploited Vulnerabilities database (KEV) database. The KEV attempts to distill the torrent of security issues assigned a CVE into the most actionable vulnerabilities which have been observed being used in the wild. CISA advises not only federal and government agencies, but offers guidance for businesses of all sizes.
Many vulnerabilities on the KEV already have fixes. Paradoxically, this can sometimes make a vulnerability higher risk. Attackers have two advantages: a patch to reverse engineer to discover the exact mechanisms to trigger the flaw, and a motivation to use any exploits on a massive scale, knowing that the window of opportunity is about to close. Most of these vulnerabilities will likely be of interest mostly to readers who are in the enterprise space, but the first one regarding Android is a good reminder to everyone that the KEV isn’t just for giant companies.
As for the latest known exploited issues:
- CVE-2026-21385 sounds very boring – an integer overflow in Qualcomm graphics drivers – except that those chipsets and drivers are found in a huge percentage of Android phones, tablets, set-top boxes, and likely more than a few smart TVs. This fix is bundled into the March Android security release and may prove critical. Remember to keep your devices up to date!
- CVE-2026-22719 is a patched vulnerability in VMWare enterprise software (Aria Operations, specifically); if you need to care about enterprise-scale VMWare, you’ll care about this one!
- CVE-2021-22054 resurfaces from 2021, again in VMWare enterprise consoles. The number of unpatched systems exposing a vulnerability from 2021 must be quite scary.
- CVE-2025-26399 is a vulnerability in SolarWinds help desk sofware, which is a return of a bug not fully fixed in CVE-2024-28988. Which is, itself, the return of a bug not fully fixed in CVE-2024-28986. Look, bug fixing can be hard.
- CVE-2026-1603 is an authentication bypass in Ivanti Endpoint Manager which allows access to stored credential secrets. Ivanti is an endpoint and device management system, used for monitoring, patching, upgrading, and controlling access on corporate device fleets.
Phrack Calls for Papers
The venerable Phrack has an open call for papers to be contributed to the summer issue. Released since 1985, Phrack has been a font of telecom and computer security hackery, including the critical “Smashing the Stack for Fun and Profit”, one of the first explanations of the now-ubiquitous buffer overflow and stack smashing attack.
If you think you’ve got something to contribute, or just want to check out their awesome retro demo scene loading page and some back issues, head over to the Phrack website.
