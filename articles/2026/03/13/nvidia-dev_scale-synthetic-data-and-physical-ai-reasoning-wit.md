---
title: "Scale Synthetic Data and Physical AI Reasoning with NVIDIA Cosmos World Foundation Models"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/"
published: "2026-03-13"
fetched: "2026-03-14T07:04:04.346349"
---

The next generation of AI-driven robots like humanoids and autonomous vehicles depends on high-fidelity, physics-aware training data. Without diverse and representative datasets, these systems don’t get proper training and face testing risks due to poor generalization, limited exposure to real-world variations, and unpredictable behavior in edge cases. Collecting massive real-world datasets for training is expensive, time-intensive, and often constrained by possibilities.
NVIDIA Cosmos addresses this challenge by accelerating world foundation model (WFM) development. At the core of its platform, Cosmos WFMs speed up synthetic data generation and act as a foundation for post-training, to develop downstream domain or task-specific physical AI models to solve these challenges. This post explores the latest Cosmos WFMs, their key capabilities that advance physical AI, and how to use them.
Cosmos world foundation model updates:
NVIDIA Cosmos world foundation models have continued to evolve rapidly, with significant advancements that further accelerate synthetic data generation and physical AI development. One year after their introduction, key updates include:
- Cosmos Transfer 2.5—Faster and more scalable data augmentation from simulation and 3D spatial inputs, enabling greater diversity across environments, lighting conditions, and scene variations.
- Cosmos Predict 2.5—Enhanced long-tail scenario generation for sequences up to 30 seconds, delivering up to 10x higher accuracy when post-trained on proprietary or domain-specific data. Supports multiview outputs, custom camera layouts, and alternate policy outputs such as action simulation.
- Cosmos Reason 2—Advanced physical AI reasoning with improved spatiotemporal understanding and timestamp precision. Adds object detection with 2D/3D point localization and bounding box coordinates, along with reasoning explanations and labels. Expanded long-context support up to 256K input tokens.
Cosmos Transfer for photorealistic videos grounded in physics
Cosmos Transfer generates high-fidelity world scenes from structural inputs, ensuring precise spatial alignment and scene composition.
Employing the ControlNet architecture, Cosmos Transfer preserves pretrained knowledge, enabling structured, consistent outputs. It utilizes spatiotemporal control maps to dynamically align synthetic and real-world representations, enabling fine-grained control over scene composition, object placement, and motion dynamics.
Inputs:
- Structured visual or geometric data: segmentation maps, depth maps, edge maps, human motion keypoints, LiDAR scans, trajectories, HD maps, and 3D bounding boxes.
- Ground truth annotations: high-fidelity references for precise alignment.
Output: Photorealistic video sequences with controlled layout, object placement, and motion.
Figure 1. On the left, a virtual simulation or ‘ground truth’ created in NVIDIA Omniverse. On the right, photoreal transformation using Cosmos Transfer
Key capabilities:
- Generate scalable, photorealistic synthetic data that aligns with real-world physics.
- Control object interactions and scene composition through structured multimodal inputs.
Using Cosmos Transfer for controllable synthetic data
With generative AI APIs and SDKs, NVIDIA Omniverse accelerates physical AI simulation. Developers use NVIDIA Omniverse, built on OpenUSD, to create 3D scenes that accurately simulate real-world environments for training and testing robots and autonomous vehicles. These simulations serve as ground truth video inputs for Cosmos Transfer, combined with annotations and text instructions. Cosmos Transfer enhances photorealism while varying environment, lighting, and visual conditions to generate scalable, diverse world states.
This workflow accelerates the creation of high-quality training datasets, ensuring AI agents generalize effectively from simulation to real-world deployment.
Cosmos Transfer enhances robotics development by enabling realistic lighting, colors, and textures in the Isaac GR00T Blueprint for synthetic manipulation motion generation and Omniverse Blueprint for Autonomous Vehicle Simulation for varying environmental and weather conditions for training. This photorealistic data is crucial for post-training policy models, ensuring smooth simulation-to-reality transfer and supporting model training for perception AI and specialized robot models like GR00T N1.
How to run the new Cosmos Transfer 2.5:
- To run inference on new Cosmos Transfer 2.5, follow the inference guide.
- To post-train on proprietary or domain data, follow the post-training guide.
- Explore NVIDIA Cosmos Cookbook for step-by-step workflows and technical recipes from Cosmos users.
Cosmos Predict for generating future world states
Cosmos Predict WFM is designed to model future world states as video from multimodal inputs, including text, video, and start-end frame sequences. It is built using transformer-based architectures that enhance temporal consistency and frame interpolation.
Key capabilities:
- Generates realistic world states directly from text prompts.
- Predict next states based on video sequences by predicting missing frames or extending motion.
- Multiframe generation between a starting and ending image, creating a complete, smooth sequence.
Cosmos Predict WFM provides a strong foundation for training downstream world models in robotics and autonomous vehicles. You can post-train these models to generate actions instead of video for policy modeling or adapt it for visual-language understanding to create custom perception AI models.
How to run the new Cosmos Predict 2.5:
- To run inference on new Cosmos Predict 2.5, follow the inference guide.
- To post-train on proprietary or domain data, follow the post-training guide.
- Explore the NVIDIA Cosmos Cookbook for step-by-step workflows and technical recipes from Cosmos users.
Cosmos Reason to perceive, reason, and respond intelligently
Cosmos Reason is a fully customizable multimodal AI reasoning model that is purpose-built to understand motion, object interactions, and space-time relationships. Using chain-of-thought (CoT) reasoning, the model interprets visual input, predicts outcomes based on the given prompt, and rewards the optimal decision. Unlike text-based LLMs, it grounds reasoning in real-world physics, generating clear, context-aware responses in natural language.
Input: Video observations and a text-based query or instruction.
Output: Text response generated through long-horizon CoT reasoning.
Key capabilities:
- Knows how objects move, interact, and change over time.
- Predicts and rewards the next best action based on input observation.
- Continuously refines decision-making.
- Purpose-built for post-training to build perception AI and embodied AI models.
Training pipeline
Cosmos Reason is trained in three stages, enhancing its ability to reason, predict, and respond to decisions in real-world scenarios.
- Pretraining: Uses a Vision Transformer (ViT) to process video frames into structured embeddings, aligning them with text for a shared understanding of objects, actions, and spatial relationships.
- Supervised fine-tuning (SFT): Specializes the model in physical reasoning across two key levels. General fine-tuning enhances language grounding and multimodal perception using diverse video-text datasets, while more training on physical AI data sharpens the model’s ability to reason about real-world interactions. It learns object behaviors like how objects can be used in the real world, action sequences, determining how multi-step tasks unfold, and spatial feasibility to distinguish realistic from impossible placements.
Reinforcement learning (RL): The model evaluates different reasoning paths and updates itself only when a better decision emerges through trial and reward feedback. Instead of relying on human-labeled data, it uses rule-based rewards:
- Entity recognition: Rewarding accurate identification of objects and their properties.
- Spatial constraints: Penalizing physically impossible placements while reinforcing realistic object positioning.
- Temporal reasoning: Encouraging correct sequence prediction based on cause-effect relationships.
How to run the new Cosmos Reason 2:
- To run inference on new Cosmos Reason 2, follow the inference guide.
- To post-train on proprietary or domain data, follow the post-training guide.
- Explore the NVIDIA Cosmos Cookbook for step-by-step workflows and technical recipes from Cosmos users.
Get started
- Visit our Cosmos Cookbook for step-by-step workflows, technical recipes, and concrete examples for building, adapting, and deploying Cosmos WFMs.
- Explore new open Cosmos models and datasets on Hugging Face and GitHub or try models on build.nvidia.com.
- Be part of the community and join our Cosmos Discord channel.
- Already using Cosmos? Learn more about how to contribute.
- Watch the GTC keynote from NVIDIA founder and CEO Jensen Huang and explore Cosmos sessions.
Updated on March 13, 2026, with advancements to NVIDIA Cosmos world foundation models.
