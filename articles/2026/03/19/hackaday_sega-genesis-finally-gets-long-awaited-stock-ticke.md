---
title: "Sega Genesis Finally Gets Long-Awaited Stock Ticker App 37 Years After Launch"
source: "Hackaday"
url: "https://hackaday.com/2026/03/19/sega-genesis-finally-gets-long-awaited-stock-ticker-app-37-years-after-launch/"
published: "2026-03-19"
fetched: "2026-03-20T00:02:54.434611"
---

Until now, if you were seated at your Sega Genesis and wanted to check your stock portfolio, you were out of luck. You had to get a smartphone, or a computer, or maybe even a television to look up stock prices and understand your financial position. Thankfully, though, Sega’s neglect of its hero platform has finally been corrected. [Mike Wolak] has given the 16-bit console the real-time stock ticker it so desperately needed.
The build runs on a MegaWiFi cartridge, which uses an ESP8266 or ESP32 microcontroller to add WiFi communication to the Sega Genesis (or Mega Drive). [Mike] wrote a custom program for the platform that would query the Finnhub HTTPS API and display live stock prices via the Genesis’s Video Display Processor. It does so via a clean console-like interface that would be familiar to users of other 16-bit machines from this era, though seeing so much textual output would have been uncommon.
By default, the stock ticker is set to show prices for major tech stocks, but you can set it up to display any major symbol available in the Finnhub data stream. You can configure up to eight custom stocks and input your holdings, and the software will calculate and display your net worth in real time.
All the files are available for those eager to monitor their portfolios on a Sega, as the financial gods intended. [Mike] notes it took a little work to get this project over the line, particularly as the ESP32-C3 doesn’t support HTTPs with stock firmware. A few other hacks were needed to keep the Genesis updating the screen during HTTP queries, too.
If you have a concentrated portfolio and a spare Sega Genesis, this could be a fun retro way to keep an eye on your holdings. Alternatively, you might prefer to go the classic paper tape route.
