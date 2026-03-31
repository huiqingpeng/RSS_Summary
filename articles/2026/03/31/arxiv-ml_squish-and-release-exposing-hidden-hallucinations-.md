---
title: "Squish and Release: Exposing Hidden Hallucinations by Making Them Surface as Safety Signals"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26829"
published: "2026-03-31"
fetched: "2026-04-01T07:19:30.598509"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Squish and Release: Exposing Hidden Hallucinations by Making Them Surface as Safety Signals
View PDF HTML (experimental)Abstract:Language models detect false premises when asked directly but absorb them under conversational pressure, producing authoritative professional output built on errors they already identified. This failure - order-gap hallucination - is invisible to output inspection because the error migrates into the activation space of the safety circuit, suppressed but not erased. We introduce Squish and Release (S&R), an activation-patching architecture with two components: a fixed detector body (layers 24-31, the localized safety evaluation circuit) and a swappable detector core (an activation vector controlling perception direction). A safety core shifts the model from compliance toward detection; an absorb core reverses it. We evaluate on OLMo-2 7B using the Order-Gap Benchmark - 500 chains across 500 domains, all manually graded. Key findings: cascade collapse is near-total (99.8% compliance at O5); the detector body is binary and localized (layers 24-31 shift 93.6%, layers 0-23 contribute zero, p<10^-189); a synthetically engineered core releases 76.6% of collapsed chains; detection is the more stable attractor (83% restore vs 58% suppress); and epistemic specificity is confirmed (false-premise core releases 45.4%, true-premise core releases 0.0%). The contribution is the framework - body/core architecture, benchmark, and core engineering methodology - which is model-agnostic by design.
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
