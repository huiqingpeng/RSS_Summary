---
title: "Select the right hardware for your local LLM deployment with this online guide"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/30/select-the-right-hardware-for-your-local-llm-deployment-with-this-online-guide/"
published: "2026-03-30"
fetched: "2026-03-31T07:00:47.115235"
---

When it comes to deploying local LLMs, many people may think that spending more money will deliver more performance, but it’s far from reality. That’s why Sipeed created the “AI Agent Local LLM Inference Device Deployment Guide” hosted on the llmdev.guide website.
The website lists common hardware with price, performance (tokens/s), power consumption, and more for various LLMs. If we take Qwen3.5 9B as an example, we can see that $4K+ hardware like NVIDIA DGX Spark or Apple Mac Studio M3 delivers about the same TPS as a machine equipped with a $260 Intel Arc B580 12GB GPU.
If money is no object and you’d like the best performance, the NVIDIA GTX 5090 32GB makes the most sense. I reckon the price comparison is imperfect because some data points reflect the price of a complete system, while others only list the price of a graphics card. However, for Qwen 122B-A10B, the NVIDIA DGX Spark offers the best price/performance compared to an Apple Mac Studio M3 Ultra 256GB. There are fewer options here because of the large memory required to run the model.
You can select from a range of options for the X and Y Axes, and the bubble size with parameters from device specifications (memory bandwidth/capacity, claimed TOPS…), LLM output and prefill, and ratios (Perf/watt, Perf/dollars…).
The website relies on Qwen 3.5 models for benchmarking:
- Qwen3.5-9B – Required (Small device baseline)
- Qwen3.5-27B – Required (Mid-range device baseline)
- Qwen3.5-35B-A3B (MoE) – Optional (MoE performance reference)
- Qwen3.5-122B-A10B (MoE) – Optional (Large memory device reference)
- Qwen3.5-397B-A17B (MoE) – Optional (Flagship device reference)
Sadly, there’s no option to filter by price. Instead, we can select a logarithmic scale to better see the price/performance of entry-level options. [Update: You can also draw a box with your mouse to zoom in instead]
Alternatively, we can switch to the list view and sort the results by price
You can get more details about each device, including specs and test results, by clicking on the list or bubble in the chart.
Note some results as estimated, and for instance, the Raspberry Pi 5 16GB’s Qwen 3.5 9B data was extrapolated from Llama 7B results.
The list of hardware can be expanded since the project accepts user submissions. If you want to submit new hardware, you’ll need to deploy the benchmark and follow the instructions. Sadly, the system does not gather data automatically, so you’d have to fill in all information after copying a template in the devices folder, then run at least Qwen 3.5 9B with a long query, and take a photo of your board. If they want more submissions, they should probably automate part of the process like sbc-bench.sh script does, or use a wizard script.
I had started to do it for the UP Xtreme ARL AI Dev Kit, but since all data needs to be entered manually, I’ll delay and submit the information during a weekend when I may have more time to play around. I’m still glad this resource exists, and hope it can be further improved.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
