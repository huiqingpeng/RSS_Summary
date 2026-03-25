---
title: "Electric Motorcycles Don’t Have To Be Security Nightmares, But This One Was"
source: "Hackaday"
url: "https://hackaday.com/2026/03/25/electric-motorcycles-dont-have-to-be-security-nightmares-but-this-one-was/"
published: "2026-03-25"
fetched: "2026-03-26T07:03:17.671925"
---

Once upon a time, they told us we wouldn’t download a car, and they were wrong. Later, Zero Motorcycles stated in their FAQ that you cannot hack an electric motorcycle, a statement which [Persephone Karnstein] and collaborator [Mitchell Marasch] evidently took issue with. Not only can you hack an electric motorcycle, it is — in [Persephone]’s words — a security nightmare.
You should absolutely go over to [Persephone]’s website and check out the whole write-up, which is adapted from a talk given at BSides Seattle 2026. There’s simply way more detail than we can get into here. Everything from “what horridly toxic solvents would I need to unpot this PCB?” to the scripts used in de-compiling and understanding code, it’s all there, and in a lively and readable style to boot. Even if you have no interest in security, or electric motorcycles, you should check it out.
The upshot is that not only were Zero Motorcycles wrong when they said their electric motorcycles could not be hacked, they were hilariously wrong. The problem isn’t the motorcycle alone: it has an app that talks to the electronics on the bike, which take over-the-air (OTA) updates. What about the code linked to the VIN alluded to in that screenshot? Well, it turns out you just need a code structured like a VIN, not an actual number. Oops. By the end of it, [Persephone] and [Mitchell] have taken absolute control of the bike’s firmware, an so have them full control over all its systems.
Why cut the brake lines when you can perform an OTA update that will do the same thing invisibly? And don’t think you can just reset the bike to factory settings to fix it: they thought of this, and the purely-conceptual, never-deployed malware has enough access to prevent that. Or they could just set the battery on fire. That was an option, too, because the battery management system gets OTA updates as well.
To be clear, we don’t have any problem with a motorcycle that’s dependent on electronics to operate. After all, we’ve seen many projects that would meet that definition over the years. But the difference is none of those projects fumbled the execution this badly. Even this 3 kW unicycle, which has a computer for balance control, doesn’t see the need to expose itself. It’s horribly unsafe in very different ways.
