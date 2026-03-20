---
title: "Studying a Battle Born LFP Battery’s Death Under Controlled Conditions"
source: "Hackaday"
url: "https://hackaday.com/2026/03/19/studying-a-battle-born-lfp-batterys-death-under-controlled-conditions/"
published: "2026-03-20"
fetched: "2026-03-20T12:03:02.255817"
---

There has been quite a bit of news recently about the Battle Born LiFePO4 (LFP) batteries and how they are dying in droves if not outright melting their plastic enclosures. Although the subsequent autopsies show molten plastic spacers on the bus bars and discolored metal in addition to very loose wiring, it can be educational to see exactly what is happening during repeated charge-discharge cycles at a fraction of the battery’s rated current. Thus [Will Prowse] recently sacrificed another Battle Born 75 Ah LFP battery to the Engineering QA Gods.
This time around the battery was hooked up to test equipment to fully graph out the charging and discharging voltage and current as it was put through its paces. To keep the battery as happy as possible it was charged and discharged at a mere 49A, well below its rated 100A.
Despite this, even after a mere 14 cycles the battery’s BMS would repeatedly disconnect the battery, as recorded by the instruments. Clearly something wasn’t happy inside the battery at this point, but the decision was made to push it a little bit harder while still staying well below the rated current.
This led to the observed failure mode where the BMS disconnects the battery so frequently that practically no current is flowing any more. Incidentally this is why you need to properly load test a battery to see whether it’s still good. In this failure mode there is still voltage on the terminals, but trying to pass any level of current leads to the rapid disconnecting by the BMS, even while as in this case the plastic spacer on the bus bar melts a little bit more.
Despite these very rapid disconnects and observed thermal issues, the BMS never puts the battery into any kind of safe mode as other LFP batteries do, leading to the melting plastic and other issues that have now been repeatedly observed. The discoloration of the battery terminals that originally started the investigation thus appears to be a result of higher charge currents and correspondingly higher temperatures.
Worryingly, Battle Born recently put out a statement – addressed in the video – in which they completely disavow these findings and insist that there is no issue at all with these LFP batteries. Naturally, if you still have any Battle Born LFP installed, you really want to test them properly, or ideally replace them with a less sketchy alternative until some kind of recall is issued.
