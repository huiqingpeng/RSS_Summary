---
title: "Form Follows Function: Recursive Stem Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15641"
published: "2026-03-18"
fetched: "2026-03-18T16:05:02.780136"
---

Computer Science > Artificial Intelligence
[Submitted on 3 Mar 2026]
Title:Form Follows Function: Recursive Stem Model
View PDFAbstract:Recursive reasoning models such as Hierarchical Reasoning Model (HRM) and Tiny Recursive Model (TRM) show that small, weight-shared networks can solve compute-heavy and NP puzzles by iteratively refining latent states, but their training typically relies on deep supervision and/or long unrolls that increase wall-clock cost and can bias the model toward greedy intermediate behavior. We introduce Recursive Stem Model (RSM), a recursive reasoning approach that keeps the TRM-style backbone while changing the training contract so the network learns a stable, depth-agnostic transition operator. RSM fully detaches the hidden-state history during training, treats early iterations as detached "warm-up" steps, and applies loss only at the final step. We further grow the outer recursion depth $H$ and inner compute depth $L$ independently and use a stochastic outer-transition scheme (stochastic depth over $H$) to mitigate instability when increasing depth. This yields two key capabilities: (i) $>20\times$ faster training than TRM while improving accuracy ($\approx 5\times$ reduction in error rate), and (ii) test-time scaling where inference can run for arbitrarily many refinement steps ($\sim 20,000 H_{\text{test}} \gg 20 H_{\text{train}}$), enabling additional "thinking" without retraining. On Sudoku-Extreme, RSM reaches 97.5% exact accuracy with test-time compute (within ~1 hour of training on a single A100), and on Maze-Hard ($30 \times 30$) it reaches ~80% exact accuracy in ~40 minutes using attention-based instantiation. Finally, because RSM implements an iterative settling process, convergence behavior provides a simple, architecture-native reliability signal: non-settling trajectories warn that the model has not reached a viable solution and can be a guard against hallucination, while stable fixed points can be paired with domain verifiers for practical correctness checks.
Current browse context:
cs.AI
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
