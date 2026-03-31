---
title: "On Token's Dilemma: Dynamic MoE with Drift-Aware Token Assignment for Continual Learning of Large Vision Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27481"
published: "2026-03-31"
fetched: "2026-04-01T07:24:49.964572"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:On Token's Dilemma: Dynamic MoE with Drift-Aware Token Assignment for Continual Learning of Large Vision Language Models
View PDF HTML (experimental)Abstract:Multimodal Continual Instruction Tuning aims to continually enhance Large Vision Language Models (LVLMs) by learning from new data without forgetting previously acquired knowledge. Mixture of Experts (MoE) architectures naturally facilitate this by incrementally adding new experts and expanding routers while keeping the existing ones frozen. However, despite expert isolation, MoE-based continual learners still suffer from forgetting due to routing-drift: old-task tokens become mistakenly attracted to newly added experts, degrading performance on prior tasks. We analyze the failure mode at the token level and reveal the token's dilemma: ambiguous and old tokens in new-task data offer minimal learning benefit yet induce forgetting when routed to new experts, due to their ambiguous routing assignment during training. Motivated by this, we propose LLaVA-DyMoE, a dynamic MoE framework that incrementally expands the MoE with drift-aware token assignment. We characterize token types via their routing score distributions and apply targeted regularization. Specifically, a token-level assignment guidance steers ambiguous and old tokens away from new experts to preserve established routing patterns and alleviate routing-drift, while complementary routing score regularizations enforce expert-group separation and promote new-expert specialization. Extensive experiments demonstrate that our LLaVA-DyMoE effectively mitigates routing-drift-induced forgetting, achieving over a 7% gain in mean final accuracy and a 12% reduction in forgetting compared to baselines. The project page is this https URL.
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
