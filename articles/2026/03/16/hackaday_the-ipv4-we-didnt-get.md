---
title: "The IPV4 We Didn’t Get"
source: "Hackaday"
url: "https://hackaday.com/2026/03/16/the-ipv4-we-didnt-get/"
published: "2026-03-16"
fetched: "2026-03-17T07:05:56.341840"
---

If you have ever read science fiction, you’ve probably seen “alternate history” stories. You know, where Europeans didn’t discover the New World until the 19th century, or the ancient Egyptians stumbled upon electricity. Maybe those things happened in an alternate universe. [BillPG] has an alternate history tale for us that imagines IPv6 was shot down and a protocol called IPv4x became prominent instead.
The key idea is that in 1993, the IP-Next-Generation working group could have decided that any solution that would break the existing network wouldn’t work. There is precedent. Stereo records play on mono players and vice versa. Color TV signals play on black and white sets just as well as black and white signals play on color TVs. It would have made perfect sense.
How could this be? The idea was to make everyone who “owns” an IPv4 address the stewards of a 96-bit sub-address block. IPv4x-aware equipment extracts the entire 128-bit address. IPv4-only equipment routes the packet to the controlling IPv4 address. Wasteful? Sure. Most people don’t need 79 octillion addresses. But if everyone has that many, then why not?
The fictional timeline has DNS and DHCP, along with dial-up stacks, changing to accommodate the new addresses. Again, you had to assume some parts of the network were still IPv4-only. DNS would return both addresses, and it was up to you to pick the IPv4x address if you understood it.
Your ISP would probably not offer you the entire extra space. A regional router could handle all traffic for your neighborhood and then direct it to your specific 128-bit address or your pool of addresses, if you have multiple devices. No need for NAT to hide your devices, nor strange router configurations to punch traffic through.
Of course, back in the real world, we have two incompatible systems: IPv4 and IPv6. IPv6 adoption has been slow and painful. We wondered why [BillPG] wrote about this future that never was. Turns out, he’s proposed a gateway that IPv6 hosts can provide to allow access from IPv4-only networks. Pretty sneaky, but we can admire it. If reading all this makes you wonder what happened to IPv5, we wondered that, too.
