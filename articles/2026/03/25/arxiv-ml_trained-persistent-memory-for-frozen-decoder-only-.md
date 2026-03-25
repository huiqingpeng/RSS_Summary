---
title: "Trained Persistent Memory for Frozen Decoder-Only LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22329"
published: "2026-03-25"
fetched: "2026-03-26T07:11:52.703758"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Trained Persistent Memory for Frozen Decoder-Only LLMs
View PDF HTML (experimental)Abstract:Decoder-only language models are stateless: hidden representations are discarded after every forward pass and nothing persists across sessions. Jeong (2026a) showed that trained memory adapters give a frozen encoder-decoder backbone persistent latent-space memory, building on the lateral-memory framework of Jeong (2026b,c). Here we ask whether the same principle transfers to the decoder-only setting, where no cross-attention pathway exists and memory must enter through self-attention alone. We adapt six methods -- prefix, parallel cross-attention, KV extension, Hebbian memory, context-gated branch, and slot-based sparse write -- to a frozen GPT-2, training only a small adapter $\theta_{mem}$. The write rule is shared; only the read injection changes from decoder cross-attention to self-attention KV prefix or parallel branch. On LoCoMo we find a striking inductive-bias dichotomy: at $1\times$ capacity, three methods with strong architectural priors -- cross-attention (M.2), Hebbian (M.4), and slot write (M.6) -- achieve retained-memory scores of $7-18\%$ and knowledge gains $\Delta K$ of $7-10$, while the other three fail ($< 0.4\%$). At $10\times$ capacity all six converge, showing the gap is architectural, not fundamental. Together with the encoder-decoder results of Jeong (2026a) and the brain-inspired modules of Jeong (2026b,c), these findings establish persistent latent-space memory as a general paradigm spanning major transformer families.
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
