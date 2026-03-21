---
title: "Slug Algorithm for On-GPU Rendering of Fonts with Bézier Curves now in Public Domain"
source: "Hackaday"
url: "https://hackaday.com/2026/03/20/slug-algorithm-for-on-gpu-rendering-of-fonts-with-bezier-curves-now-in-public-domain/"
published: "2026-03-21"
fetched: "2026-03-21T11:14:20.967901"
---

The Slug Algorithm has been around for a decade now, mostly quietly rendering fonts and later entire GUIs using Bézier curves directly on the GPU for games and other types of software, but due to its proprietary nature it didn’t see much adoption outside of commercial settings. This has now changed with its author, [Eric Lengyel], releasing it to the public domain without any limitations.
Originally [Eric] had received a software patent in 2019 for the algorithm that would have prevented anyone else from implementing it until the patent’s expiration in 2038. Since 2016 [Eric] and his business have however had in his eyes sufficient benefit from the patent, making it unnecessary to hold on to it any longer and retain such exclusivity.
To help anyone with implementing their own version of the algorithm, there is a GitHub repository containing reference shader implementations with plenty of inline comments that should help anyone with some shader experience get started.
Although pretty niche in the eyes of the average person, the benefits of using on-GPU rendering of elements like fonts are obvious in terms of rendering optimization. With this change open source rendering engines for games and more can finally also use it as well.
Thanks to [Footleg] for the tip.
