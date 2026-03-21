---
title: "ESP32: When Is A P4 A P4, But Not The P4 You Thought It Was"
source: "Hackaday"
url: "https://hackaday.com/2026/03/21/esp32-when-is-a-p4-a-p4-but-not-the-p4-you-thought-it-was/"
published: "2026-03-21"
fetched: "2026-03-22T07:02:27.221538"
---

We’re used to electronic parts of the same type staying predictably the same, sometimes over many years. An early Z80 from the mid 1970s can be exchanged with one from the end of production a few years ago, for example. This week, we’ve had DMs from several readers who’ve found that this is not always the case, and the culprit is surprising. Espressif has released a new revision of their P4 application processor, and though it’s ostensibly the same, there are a couple of changes that have been catching people out.
The changes lie in both hardware and software, in that there’s a pin that’s changed from NC to a power rail, a few extra passives are needed, and firmware must be compiled separately for either revision. The problem is that they are being sold as the same device and appear in some places under the same SKU! This is leading to uncertainty as to which P4 revision is in stock at wholesalers. We’ve been told about boards designed for the old revision being assembled with the new one, a situation difficult to rework your way out of. Designers are also left uncertain as to which firmware build is needed for boards assembled in remote factories.
The ESP32-P4 is an impressive part for its price, and we’re sure that we’ll be seeing plenty of projects using this new revision over the coming years. We’re surprised that it doesn’t have a different enough part number and that the wholesalers have seemingly been caught napping by the change. We’re told that some of the well-known Chinese assembly houses are now carrying the two chips as separate SKUs, but that’s scant consolation for a designer with a pile of boards carrying the wrong part. If you’re working with the P4, watch out, make sure your board is designed for the latest revision, and ask your supplier to check which chips you’ll get.
If the P4 is new to you, we’ve already seen a few projects using it.
