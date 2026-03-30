---
title: "Using a Scientific Satellite for Passive Radar"
source: "Hackaday"
url: "https://hackaday.com/2026/03/30/using-a-scientific-satellite-for-passive-radar/"
published: "2026-03-30"
fetched: "2026-03-31T07:04:46.047643"
---

The basic principle of radar systems is simple enough: send a radio signal out, and measure the time it takes for a reflection to return. Given the abundant sources of RF signals – television signals, radio stations, cellular carriers, even Wi-Fi – that surround most of us, it’s not even necessary to transmit your own signal. This is the premise of passive radar, which uses passive RF illumination to form an image. The RF signal doesn’t even need to come from a terrestrial source, as [Jean Michel Friedt] demonstrated with a passive radar illuminated by the NISAR radar-imaging satellite (pre-print paper).
NISAR is a synthetic-aperture radar satellite jointly built by NASA and ISRO, and it completes a pass over the world every twelve days. It uses an L-band chirp radar signal, which can be picked up with GNSS antennas. One antenna points up towards the satellite, and has a ground plane blocking the signal from directly reaching the second antenna, which picks up reflections from the landscape under observation. Since the satellite would illuminate the scene for less than a minute, [Jean-Michel] had to predict the moment of peak intensity, and achieved an accuracy of about three seconds.
The signals themselves were recorded with an SDR and a Raspberry Pi. High-end, high-resolution SDRs such as the Ettus B210 gave the best results, but an inexpensive homebuilt MAX2771-based SDR also produced recognizable images. This setup won’t be providing any particularly detailed images, but it did accurately show the contours of the local geography – quite a good result for such a simple setup.
If you’re more interested in tracking aircraft than surveying landscapes, check out this ADS-B-synchronized passive radar system. Although passive radar doesn’t require a transmitter license, that doesn’t mean it’s free from legal issues, as the KrakenSDR team can testify.
