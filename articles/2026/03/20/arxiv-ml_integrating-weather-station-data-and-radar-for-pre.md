---
title: "Integrating Weather Station Data and Radar for Precipitation Nowcasting: SmaAt-fUsion and SmaAt-Krige-GNet"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.16116"
published: "2026-03-20"
fetched: "2026-03-20T14:05:35.288716"
---

Computer Science > Machine Learning
[Submitted on 22 Feb 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Integrating Weather Station Data and Radar for Precipitation Nowcasting: SmaAt-fUsion and SmaAt-Krige-GNet
View PDF HTML (experimental)Abstract:Short-term precipitation nowcasting is essential for flood management, transportation, energy system operations, and emergency response. However, many existing models fail to fully exploit the extensive atmospheric information available, relying primarily on precipitation data alone. This study examines whether integrating multi variable weather-station measurements with radar can enhance nowcasting skill and introduces two complementary architectures that integrate multi variable station data with radar images. The SmaAt-fUsion model extends the SmaAt-UNet framework by incorporating weather station data through a convolutional layer, integrating it into the bottleneck of the network; The SmaAt-Krige-GNet model combines precipitation maps with weather station data processed using Kriging, a geo-statistical interpolation method, to generate variable-specific maps. These maps are then utilized in a dual-encoder architecture based on SmaAt-GNet, allowing multi-level data integration. Experimental evaluations were conducted using four years (2016--2019) of weather station and precipitation radar data from the Netherlands. Results demonstrate that SmaAt-Krige-GNet outperforms the standard SmaAt-UNet, which relies solely on precipitation radar data, in low precipitation scenarios, while SmaAt-fUsion surpasses SmaAt-UNet in both low and high precipitation scenarios. This highlights the potential of incorporating discrete weather station data to enhance the performance of deep learning-based weather nowcasting models.
Submission history
From: Siamak Mehrkanoon [view email][v1] Sat, 22 Feb 2025 06:46:04 UTC (6,429 KB)
[v2] Wed, 3 Dec 2025 08:02:12 UTC (5,957 KB)
[v3] Thu, 19 Mar 2026 10:37:36 UTC (5,873 KB)
Current browse context:
cs.LG
Change to browse by:
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
