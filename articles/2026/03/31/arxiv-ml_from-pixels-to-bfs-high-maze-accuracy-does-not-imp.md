---
title: "From Pixels to BFS: High Maze Accuracy Does Not Imply Visual Planning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26839"
published: "2026-03-31"
fetched: "2026-04-01T07:19:43.336719"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:From Pixels to BFS: High Maze Accuracy Does Not Imply Visual Planning
View PDF HTML (experimental)Abstract:How do multimodal models solve visual spatial tasks -- through genuine planning, or through brute-force search in token space? We introduce \textsc{MazeBench}, a benchmark of 110 procedurally generated maze images across nine controlled groups, and evaluate 16 model configurations from OpenAI, Anthropic, Google, and Alibaba. GPT-5.4 solves 91\% and Gemini 3.1 Pro 79\%, but these scores are misleading: models typically translate images into text grids and then enumerate paths step by step, consuming 1,710--22,818 tokens per solve for a task humans do quickly. Without added reasoning budgets, all configurations score only 2--12\%; on 20$\times$20 ultra-hard mazes, they hit token limits and fail. Qualitative traces reveal a common two-stage strategy: image-to-grid translation followed by token-level search, effectively BFS in prose. A text-grid ablation shows Claude Sonnet 4.6 rising from 6\% on images to 80\% when given the correct grid, isolating weak visual extraction from downstream search. When explicitly instructed not to construct a grid or perform graph search, models still revert to the same enumeration strategy. \textsc{MazeBench} therefore shows that high accuracy on visual planning tasks does not imply human-like spatial understanding.
Submission history
From: Alberto Gonzalo Rodriguez Salgado [view email][v1] Fri, 27 Mar 2026 08:10:05 UTC (4,287 KB)
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
