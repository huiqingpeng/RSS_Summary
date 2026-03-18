---
title: "Zephyrus: An Agentic Framework for Weather Science"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.04017"
published: "2026-03-18"
fetched: "2026-03-18T17:12:02.475690"
---

Computer Science > Artificial Intelligence
[Submitted on 5 Oct 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Zephyrus: An Agentic Framework for Weather Science
View PDF HTML (experimental)Abstract:Foundation models for weather science are pre-trained on vast amounts of structured numerical data and outperform traditional weather forecasting systems. However, these models lack language-based reasoning capabilities, limiting their utility in interactive scientific workflows. Large language models (LLMs) excel at understanding and generating text but cannot reason about high-dimensional meteorological datasets. We bridge this gap by building the first agentic framework for weather science. Our framework includes a Python code-based environment for agents (ZephyrusWorld) to interact with weather data, featuring tools including a WeatherBench 2 dataset indexer, geolocator for geocoding from natural language, weather forecasting, climate simulation capabilities, and a climatology module for querying precomputed climatological statistics (e.g., means, extremes, and quantiles) across multiple timescales. We design Zephyrus, a multi-turn LLM-based weather agent that iteratively analyzes weather datasets, observes results, and refines its approach through conversational feedback loops. We accompany the agent with a new benchmark, ZephyrusBench, with a scalable data generation pipeline that constructs diverse question-answer pairs across weather-related tasks, from basic lookups to advanced forecasting, extreme event detection, and counterfactual reasoning. Experiments on this benchmark demonstrate the strong performance of Zephyrus agents over text-only baselines, outperforming them by up to 44 percentage points in correctness. However, the hard tasks are still difficult even with frontier LLMs, highlighting the challenging nature of our benchmark and suggesting room for future development. Our codebase and benchmark are available at this https URL.
Submission history
From: Sumanth Varambally [view email][v1] Sun, 5 Oct 2025 03:34:08 UTC (3,022 KB)
[v2] Mon, 16 Mar 2026 19:30:40 UTC (3,076 KB)
Current browse context:
cs.AI
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
