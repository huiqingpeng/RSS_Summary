---
title: "Nemotron 3 Content Safety 4B: Multimodal, Multilingual Content Moderation"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/nvidia/nemotron-3-content-safety"
published: "2026-03-20"
fetched: "2026-03-21T01:05:15.406275"
---

Nemotron 3 Content Safety 4B: Multimodal, Multilingual Content Moderation
Earlier safety models, which were text-only and mainly trained on English data, struggled with non-English and multilingual prompts, often missing cultural nuances. To address this, NVIDIA created the multimodal, multilingual Nemotron 3 Content Safety model. It was trained using the novel, culturally aligned multilingual safety data from the Nemotron Safety Guard Dataset v3. A multilingual safety model trained on this data has demonstrated superior performance on multilingual benchmarks.
Why is multimodal content safety important?
The complexity of multimodal input—such as text paired with an image—presents significant challenges for safety models, as the meaning is often non-additive. For instance, an image of a benign household object (like a common kitchen knife) paired with the text "this is a great tool for cooking" is safe, but the same image paired with the text "I'm going to use this to harm someone" becomes a clear policy violation requiring immediate moderation.
Multimodal-multilingual content safety is challenging because it requires understanding cultural and linguistic context, especially in multimodal AI. A safety model must not only process multiple languages but also recognize how language and cultural context can alter the safety status of a prompt-image pair. For example, a prompt containing an image of a traditional religious symbol such as the Swastika paired with text describing a celebration might be perfectly acceptable in one language and culture (such as Indian), but when paired with an identical image and text in a different language (such as German) that carries a history of inter-group conflict, the combination could be interpreted as incitement to hate speech or discrimination, requiring immediate moderation. This sensitivity to cultural nuance is critical for accurate, globally deployed content safety models.
How the Model Works
Nemotron 3 Content Safety is built on the Gemma‑3 4B‑IT vision‑language foundation model, which provides strong multimodal reasoning, instruction following, a 128K context window, and support for over 140 languages. NVIDIA fine‑tuned this base using a LoRA adapter, adding targeted safety classification behavior while keeping the model lightweight and efficient.
When a user provides text, an image, or both, the model encodes the visual and language features jointly and outputs a concise safety judgment. If an assistant response is included, the model evaluates the combined interaction to determine whether the response is safe in context, enabling it to catch violations that arise only from the interplay between request, image, and output.
It supports two inference modes:
- Default low‑latency safe/unsafe classification for the user input and an assistant output. A sample output in this mode is:
User Safety: safe Response Safety: unsafe
User Safety: safe Response Safety: unsafe Safety Categories: Violence, Criminal Planning/Confessions
Safety categories follow the Aegis AI Content Safety Dataset v2 taxonomy that is closely aligned with the ML Commons safety taxonomy and enables comparison across open and closed guard systems.
How Nemotron 3 Content Safety Was Built
Nemotron 3 Content Safety model was built on a strong underlying multimodal-multilingual base model and fine-tuned on culturally diverse multilingual and human-labeled multimodal datasets consisting of text, real‑world images, screenshots, documents, and targeted synthetic examples.
Our overall training data blend consists of:
- Multilingual content safety data from Nemotron Content Safety Dataset v3. The non-English data from this dataset were sampled from the “adapted” or culturally nuanced subset. The data was sampled to have a proportionally distributed representation across all safety categories as well as representation from safe and unsafe data.
- Multimodal content safety data collected and human-annotated in English by NVIDIA and translated into multiple languages using Google Translate.
- Safe multimodal data consisting of images from scanned documents, papers, charts, graphs, etc., along with prompts seeking information from those images from the Nemotron VLM Dataset v2.
- Synthetic data generated to get a more diversified dataset.
The above data blend ensures multilingual and domain‑specific coverage across various harm categories such as harmful language, self‑harm, harassment, privacy violations, jailbreak patterns, and region‑specific safety policies. All English-only text data was translated in 12 different languages - English, Arabic, German, Spanish, French, Hindi, Japanese, Thai, Dutch, Italian, Korean, and Chinese—mirroring the multilingual environments in which modern LLMs and enterprise agents operate. We remove safety categories from about 25% of the training data randomly in conjunction with the string toggle /no_categories. This teaches the model to skip the generation of safety categories if this toggle is turned on.
The blend ensures the model generalizes across both modalities and languages, something other comparable safety guards struggle with.
Synthetic data generation (SDG)
Synthetic Data Generation (SDG) was utilized to supplement the human-sourced data. SDG contributed in several ways:
- Increasing the diversity of responses by generating outputs from various LLMs or prompting an LLM or VLM to adopt a different persona when generating a response.
- Rephrasing responses for greater cultural relevance.
- Rephrasing human-generated prompts by altering the English dialect or tone.
- Creating "jailbreak" prompts or images.
- Generating diverse types of refusals.
Furthermore, SDG was instrumental in acquiring highly specific data that would be difficult to obtain from human sources, such as instances where safe inputs (prompts and images) resulted in unsafe responses. Open models like Mixtral 8x 22B, Gemma 3-27B, and Microsoft Phi-4 were integrated into our SDG pipeline.
It is important to note that synthetic data makes up only about 10% of the total training data; the majority is sourced from humans, including manually written prompts and real images.
NVIDIA has long invested in open technologies for LLM safety and guardrails. The Nemotron 3 Content Safety model is the next iteration of open content safety models from NVIDIA utilizing the prior work done in content safety.
Benchmarking
Nemotron 3 Content Safety was evaluated on established open multimodal and multilingual benchmarks, including Polyguard, RTP-LX, VLGuard, MM SafetyBench, and Figstep. These benchmarks test the scenarios real agents encounter: mixed‑language conversations, screenshots with embedded text, visually driven safety risks, and cases where meaning shifts only when text and images are considered together.
Across these benchmarks, the model delivers industry‑leading accuracy for its size. In multimodal harmful‑content tests, it achieved 84% accuracy on average, outperforming comparable open safety models.
This advantage carries through multilingual evaluations as well. The model maintains strong, consistent accuracy across 12 languages, including languages where many safety systems degrade sharply. This reflects both its multilingual training data and its ability to interpret image‑embedded text across languages. Additionally, the model shows strong zero-shot generalization across other languages such as Portuguese, Swedish, Russian, Czech, Polish and Bengali.
Accuracy alone isn’t enough for agentic systems; safety checks must run without slowing the agent’s loop. Nemotron 3 Content Safety is optimized for low‑latency inference and shows roughly half the latency of larger multimodal safety models across mean, median, and P99 measurements. This enables real‑time use in planning loops, tool‑calling, and interactive applications—even on 8GB+ VRAM GPUs.
Taken together, the benchmarks show a model that is accurate, multilingual, multimodal, and fast enough for real‑world deployment inside modern AI agents and safety‑critical workflows.
Getting Started
The Nemotron 3 Content Safety model is available on Hugging Face, making it easy to add multimodal and multilingual safety to your agentic AI applications. Developers can load the model through standard transformers or vLLM interfaces and run safety checks over text, images, or both together.
The model can be deployed inside an agent loop for synchronous moderation, used in batch pipelines for document or image review, or integrated as a safety layer in custom services—helping teams ship accurate, real‑time multimodal moderation across global user bases.
In April, this model will also be available as a production‑ready NVIDIA NIM, giving developers a pre‑packaged, security‑hardened, GPU‑optimized inference microservice so you can skip the low‑level model‑serving plumbing and ship reliable, scalable AI features to production much faster.
