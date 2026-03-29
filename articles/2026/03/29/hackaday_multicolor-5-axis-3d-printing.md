---
title: "Multicolor 5-Axis 3D Printing"
source: "Hackaday"
url: "https://hackaday.com/2026/03/29/multicolor-5-axis-3d-printing/"
published: "2026-03-29"
fetched: "2026-03-30T07:05:09.862734"
---

Usually, when we see non-planar 3D printers, they’re rather rudimentary prototypes, intended more as development frames than as workhorse machines. [multipoleguy]’s Archer five-axis printer, on the other hand, breaks this trend with automatic four-hotend toolchanging, a CoreXY motion system, and print results as good-looking as any Voron’s.
The print bed rests on three ball joints, two on one side and one in the center of the opposite side. Each joint can be raised and lowered on an independent rail, which allows the bed to be tilted on two axes. The dimensions of the extruders’ motion system limit how much the bed can be angled when the extruder is close to the bed, but it can reach sharp angles further out.
The biggest difficulty with non-planar printing is developing a slicer; [multipoleguy] is working on a slicer (MaxiSlicer), but it’s still in development. It looks as though it’s already working rather well, to the point that [multipoleguy] has been optimizing purge settings for tool changes. It seems that when a toolhead is docked, the temperature inside the melt chamber rises above the normal temperature in use, which causes stringing. To compensate for this, the firmware runs a more extensive purge when a hotend’s been sitting for a longer time. The results speak for themselves: a full three-color double helix, involving 830 tool changes, could be printed with as little as six grams of purge waste.
As three-axis 3D printers become consumer products, hackers have kept looking for further improvements to make, which perhaps explains the number of non-planar printing projects appearing recently, including a few five-axis machines. Alternatively, some have experimented with non-planar print ironing.
