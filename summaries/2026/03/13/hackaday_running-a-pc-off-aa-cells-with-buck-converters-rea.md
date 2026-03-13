---
title: "Running a PC off AA Cells With Buck Converters Really Boosts Performance"
source: "Hackaday"
url: "https://hackaday.com/2026/03/13/running-a-pc-off-aa-cells-with-buck-converters-really-boosts-performance/"
published: "2026-03-13"
summarized: "2026-03-14T07:03:16.341312"
ai_provider: "openai"
---

【是什么 / What it is】
这篇文章介绍了YouTube博主[ScuffedBits]进行的第二次实验：使用64节AA电池（碳性、碱性、镍氢三种类型）通过降压转换器为台式电脑供电。与第一次尝试相比，这次实验采用了更高电压的电池组配置（约25V直流），通过廉价的降压模块转换为12V直流，成功让一台基于Core i3 530的电脑运行了33分钟以上，甚至可以启动系统、运行游戏和基准测试。

This article describes a second experiment by YouTuber [ScuffedBits] using 64 AA batteries (carbon, alkaline, and NiMH types) with buck converters to power a desktop PC. Compared to the first attempt, this experiment used a higher voltage battery configuration (~25V DC), converted to 12V DC through a cheap buck regulator module, successfully running a Core i3 530-based computer for over 33 minutes, including system boot, gaming, and benchmark testing.

---

【为什么重要 / Why it matters】
这个实验验证了高电压+降压转换器方案在低功率直流供电中的优势：通过提高电压降低电流，减少线路损耗和安全隐患，同时展示了镍氢电池在实际高放电场景下的优越性能。这也提醒我们，尽管锂电池技术不断进步，镍氢电池凭借良好的功率密度、安全性和环保特性，在特定应用场景中仍具竞争力， DIY电源设计中的"复古"技术选择往往有其工程合理性。

This experiment validates the advantages of high-voltage + buck converter solutions for low-power DC applications: higher voltage reduces current, minimizing line losses and safety risks, while demonstrating NiMH batteries' superior performance in high-discharge scenarios. It also reminds us that despite lithium-ion advances, NiMH batteries remain competitive in specific applications due to good power density, safety, and environmental friendliness—"retro" technical choices in DIY power design often have solid engineering rationale.

---

【我能用什么 / How I can use it】
对于需要构建便携或备用直流电源的场景，可采用"电池组串联升压+降压稳压"的架构，优先选择镍氢等可充电化学体系以降低长期成本。在电子DIY项目中，可利用常见的降压模块（如LM2596、XL4015等）将不稳定的电池电压转换为稳定的12V/5V输出，同时注意根据负载功率计算合适的电池串联数量，确保输入电压始终高于目标输出电压以维持转换效率。

For portable or backup DC power needs, consider a "battery series-boost + buck regulation" architecture, prioritizing rechargeable chemistries like NiMH for long-term cost savings. In electronics DIY projects, common buck modules (LM2596, XL4015, etc.) can convert unstable battery voltage to stable 12V/5V output—calculate appropriate series cell count based on load power to ensure input voltage remains above target output for conversion efficiency.
