---
title: "The D in DNS Stands for DOOM"
source: "Hackaday"
url: "https://hackaday.com/2026/03/31/the-d-in-dns-stands-for-doom/"
published: "2026-03-31"
fetched: "2026-04-01T07:03:58.670280"
---

As literally everything ought to be able to play DOOM in some fashion, [Adam Rice] recently set out to make the venerable DNS finally play the game after far too many decades of being DOOM-less. You may be wondering how video games and a boring domain records database relate to each other. This is where DNS TXT records come into play, which are essentially fields for arbitrary data with no requirements or limitations on this payload, other than a 2,000 character limit.
Add to this the concept of DNS zones which can contain thousands of records and the inkling of a plan begins to form. Essentially the entire game (in C#) is fetched from TXT records, loaded into memory and run from there. This is in some ways a benign form of how DNS TXT records can be abused by people with less harmless intentions, though [Adam] admits to using the Claude chatbot to help with the code, so YMMV.
The engine and WAD file with the game’s resources are compressed to fit into 1.7 MB along with a 1.2 MB DLL bundle, requiring 1,966 TXT records in Base64 encoding on a Cloudflare Pro DNS zone. With a free Cloudflare account you’d need to split it across multiple zones. With the TXT records synced across the globe, every caching DNS server in the world now has a copy of DOOM on it, for better or worse.
You can find the project source on GitHub if you want to give this a shake yourself.
Thanks to [MrRTFM] for the tip.
