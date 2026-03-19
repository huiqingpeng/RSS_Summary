---
title: "ToolRegistry: A Protocol-Agnostic Tool Management Library for Function-Calling LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.10593"
published: "2026-03-19"
fetched: "2026-03-19T14:16:33.318570"
---

Computer Science > Software Engineering
[Submitted on 11 Jul 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:ToolRegistry: A Protocol-Agnostic Tool Management Library for Function-Calling LLMs
View PDF HTML (experimental)Abstract:Large Language Model (LLM) applications are increasingly relying on external tools to extend their capabilities beyond text generation. However, current tool integration approaches suffer from fragmentation, protocol limitations, and implementation complexity, leading to substantial development overhead. This paper presents ToolRegistry, a protocol-agnostic tool management system that has evolved from a single library into a modular three-package ecosystem: a core registry for tool management and execution, a server package providing protocol adapters (MCP, OpenAPI) and routing, and a hub package offering curated, production-tested tool implementations. Beyond the original contributions of unified registration, automated schema generation, and dual-mode concurrent execution, the ecosystem now includes an independent MCP client supporting four transport mechanisms, a web-based admin panel for runtime management, an event system for change propagation, and fine-grained tool lifecycle control. Our evaluation demonstrates that ToolRegistry achieves 60-80% reduction in tool integration code, up to 3.1x performance improvements through concurrent execution, and broad compatibility with OpenAI function calling standards. Real-world case studies show significant improvements in development efficiency and code maintainability across diverse integration scenarios. ToolRegistry is open-source and available at this https URL, with comprehensive documentation at this https URL.
Submission history
From: Peng Ding [view email][v1] Fri, 11 Jul 2025 20:23:23 UTC (138 KB)
[v2] Wed, 18 Mar 2026 14:23:55 UTC (163 KB)
Current browse context:
cs.SE
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
