---
title: "Self-healing CMOS Imager to Withstand Jupiter’s Radiation Belt"
source: "Hackaday"
url: "https://hackaday.com/2026/03/29/self-healing-cmos-imager-to-withstand-jupiters-radiation-belt/"
published: "2026-03-29"
fetched: "2026-03-30T07:04:49.911730"
---

Ionizing radiation damage from electrons, protons and gamma rays will over time damage a CMOS circuit, through e.g. degrading the oxide layer and damaging the lattice structure. For a space-based camera that’s inside a probe orbiting a planet like Jupiter it’s thus a bit of a bummer if this will massively shorted useful observation time before the sensor has been fully degraded. A potential workaround here is by using thermal energy to anneal the damaged part of a CMOS imager.
The first step is to detect damaged pixels by performing a read-out while the sensor is not exposed to light. If a pixel still carries significant current it’s marked as damaged and a high current is passed through it to significantly raise its temperature. For the digital logic part of the circuit a similar approach is used, where the detection of logic errors is cause for a high voltage pulse that should also result in annealing of any damage.
During testing the chip was exposed to the same level of radiation to what it would experience during thirty days in orbit around Jupiter, which rendered the sensor basically unusable with a massive increase in leakage current. After four rounds of annealing the image was almost restored to full health, showing that it is a viable approach.
Naturally, this self-healing method is only intended as another line of defense against ionizing radiation, with radiation shielding and radiation-resistant semiconductor technologies serving as the primary defenses.
