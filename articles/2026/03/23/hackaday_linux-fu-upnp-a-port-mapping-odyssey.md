---
title: "Linux Fu: UPNP A Port Mapping Odyssey"
source: "Hackaday"
url: "https://hackaday.com/2026/03/23/linux-fu-upnp-a-port-mapping-odyssey/"
published: "2026-03-23"
fetched: "2026-03-24T07:11:58.908140"
---

If you’ve ever run a game server or used BitTorrent, you probably know that life is easier if your router supports UPnP (Universal Plug and Play). This is a fairly old tech — created by a standards group in 1999 — that allows a program to open an incoming port into your home network. Of course, most routers let you do this manually, but outside of the Hackaday universe, most people don’t know how to log into their routers, much less how to configure an open UDP port.
I recently found myself using a temporary setup where I could not access the router directly, but I needed some open ports. That got me thinking: if a program can open a port using UPnP, why can’t I? Turns out, of course, you can. Maybe.
Caveats
The first thing, of course, is that you need your firewall open, but that’s true no matter how you open up the router. If the firewall is in the router, then you are at the mercy of the router firmware to realize that if UPnP opens something up, it needs to open the firewall, too.
You might think, “Of course it will do that.” However, I’ve found there is a lot of variation in the firmware from different vendors, and if you aren’t in control of the router, it is more likely to have buggy firmware.
The other caveat is that the router needs UPnP enabled; if it isn’t and you have to get into it anyway, you might as well set up port forwarding in the usual way. I was in luck. The router I was behind had UPnP turned on.
In Theory
There are several libraries aimed at working with UPnP and many of them come with simple test clients. I decided to install miniupnpd, which has the upnpc utility. You don’t have to be root to run it. In theory, it should be very simple to use. You can use -l to list all the router’s current UPnP ports. The -a option adds a port, and -d deletes it. There are a few other options, but that covers most of the common use cases.
So, to open external port 2222 to port 22 on 192.168.1.133 you should be able to say:
upnpc -e 'HaD Test' -a 192.168.1.133 22 2222 tcp 3600
The -e option lets us make up a creative title for the mapping. The 3600 is the number of seconds you need the port open. Easy, right? Well, of course not.
Under the Hood
UPnP covers several different areas, including IP assignment and streaming media. However, the part of it we are using is for NAT traversal. Your router identifies as an Internet Gateway Device that other UPnP-aware programs can locate.
Unfortunately, there are two versions of the gateway device specification, and there are many compatibility problems. You are also at the mercy of the vendor’s correct interpretation of the spec.
UPNP has been known to be a security risk. In 2011, a tool appeared that let some UPnP devices map ports when asked from outside your network. Easy to imagine how that could be a bad thing.
UPNP devices advertise services that others can use, and, hopefully, your router advertises that it is a gateway. The advertisement itself doesn’t tell you much. But it does let you fetch an XML document that describes the device.
For example, part of my XML file looks like this:
11urn:schemas-upnp-org:device:InternetGatewayDevice:1OpenWRT routerOpenWRT http://www.openwrt.org/OpenWRT routerOpenWRT router1 http://www.openwrt.org/00000000uuid:00000000-0000-0000-0000-000000000000 urn:schemas-upnp-org:service:Layer3Forwarding: 1urn:upnp-org:serviceId:L3Forwarding1/L3F.xml/ctl/L3F/evt/L3Furn: schemas-upnp-org:device:WANDevice:1WANDeviceMiniUPnPhttp://miniupnp.free.fr/WAN DeviceWAN Device20260105 ...
In Practice
There are a few strange things about the way upnpc works. First, when you do a list, you’ll get an error at the end. Apparently, that’s normal. The program simply asks for entry zero, one, two… until it gets an error (a 713 error).
However, when I tried to add an open port to this particular router, it always failed, giving me an error that implied that the port was already in use. Of course, it wasn’t.
Through experimentation, I figured out that the UPnP service on the router (the one I can’t get into) isn’t running as root. So any port number less than 1,024 is unmappable in either direction. Of course, this may not be a problem for you if you have a sane router. You could argue whether this is a bug or not, but it certainly didn’t give a good error message.
Testing, One, Two…
Just to do a simple test, I issued the following command. (with my firewall off, just for testing):
upnpc -e HADTEST -a 192.168.1.133 8022 8023 tcp 3600
I verified the port opening using the -l option. Then I stood up a really dumb telnet-style server on the local port (8022):
socat readline TCP-LISTEN:8022,reuseaddr,fork
From a machine on another network, I issued a telnet command to my public IP (198.37.197.21):
telnet 198.37.197.21 8023
Of course, I could have used 8022 for both ports, but I wanted it to be clear which argument was which. At this point, typing some things on the remote machine should show right up on the local machine, punching through the firewall.
In case you forgot, you can escape out of Telnet using Control-] and then a “q” will close the program. You can also just terminate the socat program on the local side.
More Than One Way
It is a bummer I couldn’t open up an ssh port using this method, although you can run sshd on a high port and get there that way. But it is better than nothing. Better still would have been to replace the router, but that wasn’t an option in this case.
There are other tools out there if you are interested. NAT-PMP is easy to use from Python, for example. There’s also something called PCP (not the performance co-pilot, which is something else). Many routers don’t support either of these, and we hear that implementations are often buggy, just like UPnP.
For the record, NAT-PMP didn’t give me a better error message, either. So the moral is this: if you can, just punch a hole in your router the old-fashioned way. But if you can’t. Linux almost always gives you another option.
