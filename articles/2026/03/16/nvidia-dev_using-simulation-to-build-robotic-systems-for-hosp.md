---
title: "Using Simulation to Build Robotic Systems for Hospital Automation"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/using-simulation-to-build-robotic-systems-for-hospital-automation/"
published: "2026-03-16"
fetched: "2026-03-17T07:06:22.845005"
---

Healthcare faces a structural demand–capacity crisis: a projected global shortfall of ~10 million clinicians by 2030, billions of diagnostic exams annually with significant unmet demand, hundreds of millions of procedures with large access gaps, and costly operating room (OR) inefficiencies measured in tens of dollars per minute.
The future hospital must therefore be automation-enabled—where robotics extends clinician capacity, increases procedural throughput, reduces variability, and democratizes access to high-quality care. Imagine autonomous imaging robots navigating patient anatomy to provide X-rays for the unserved billions, while in the OR, ‘Surgical Subtask Automation’ handles repetitive suturing so surgeons can focus on critical decisions. Beyond the bedside, service robots recapture wasted minutes by autonomously delivering supplies, saving nurses miles of walking.
The data gap and real-world limits
The core bottleneck is data. Hospitals are heterogeneous, chaotic, and high-stakes environments—every facility has different layouts, workflows, equipment, patient populations, and policies. Commissioning fleets of robots across diverse hospitals to capture exhaustive real-world data is economically and operationally infeasible. Even if it were possible, real-world data capturing every edge case—crowded hallways, emergency interruptions, rare complications, human-robot interactions under stress—simply doesn’t exist. Testing every scenario in live clinical settings is both unsafe and impractical.
The solution is simulation, digital twinning, and synthetic data generation.
Simulation and synthetic data generation are therefore not optional—they are foundational. Virtual hospital environments allow robots to experience thousands of navigation patterns, workflow variations, task permutations, and human interaction scenarios safely and at scale before deployment. High-fidelity simulation enables stress testing, long-horizon policy learning, rare-event exposure, and closed-loop training that would be impossible to achieve in the real world alone. This approach accelerates development, reduces clinical risk, and provides the data substrate required for reliable, intelligent automation across complex hospital systems.
Project Rheo introduces a different approach.
How developers can use the Project Rheo blueprint to train AI systems
Instead of teaching robots inside hospitals, developers can now train hospitals—in simulation—before automation ever arrives.
This guide walks through how developers can use the Project Rheo blueprint to build their first smart hospital digital twin and begin training Physical AI systems.
Project Rheo, a blueprint for a smart hospital automation and Physical AI development, combines:
- Physical agents: loco-manipulation and manipulation policies (for example, surgical tray pick-and-place, case cart pushing, bimanual tool handling) driven by NVIDIA Isaac
GR00T
vision-language-action (VLA) models and/or reinforcement learning (RL) post-training. - Digital agents: monitoring and assistance agents powered by surgical foundation models (for example, an agent driven by vision language model (VLM) that observes a live camera stream and suggests actions).
- Digital twin and SimReady assets: an OR simulation built with NVIDIA Isaac Sim / Isaac Lab, used to safely iterate on tasks, data, and policies.
Rheo supports two complementary simulation tracks, each optimized for a different part of the workflow:
- Isaac Lab-Arena track: rapid environment composition and iteration for OR-scale tasks (for example loco-manipulation), where you want to swap scenes, objects, embodiments, and evaluation runners with minimal friction.
- Isaac Lab track: task-centric, manager-based environments that pair naturally with curriculum design and large-scale RL post-training for precision manipulation.
In the following section, the “digital hospital” is built using the Isaac Lab-Arena composition model: choose named assets, select an embodiment, attach a task, and run.
Step 1: Create your digital hospital
Compose a scene + task into an Isaac Lab-Arena environment
One of the core features of the Rheo blueprint is the rapid composition of new environments and tasks using the Isaac Lab-Arena
model.
This allows developers to quickly define a clinical scenario by combining existing assets, a robot embodiment, and a task definition.
The following Python code block demonstrates how to define a locomotion-manipulation task—specifically, having the Unitree G1 robot pick up a surgical tray and place it onto a cart—within a pre-operative room scene.
from isaaclab_arena.environments.isaaclab_arena_environment import IsaacLabArenaEnvironment
from isaaclab_arena.scene.scene import Scene
from sim.tasks.g1_tray_pick_and_place_task import G1TrayPickPlaceTask
# 1. Define the scene components (USD assets)
background = asset_registry.get_asset_by_name("pre_op")()
pick_up_object = asset_registry.get_asset_by_name("surgical_tray")()
destination_cart = asset_registry.get_asset_by_name("cart")()
# 2. Define the robot embodiment
embodiment = asset_registry.get_asset_by_name("g1_wbc_joint")(enable_cameras=True)
# 3. Compose the Scene
scene = Scene(assets=[background, pick_up_object, destination_cart])
# 4. Create the Environment by combining the Embodiment, Scene, and Task
env = IsaacLabArenaEnvironment(
name="g1_locomanip_tray_pick_and_place",
embodiment=embodiment,
scene=scene,
task=G1TrayPickPlaceTask(pick_up_object, destination_cart, background, episode_length_s=30.0),
teleop_device=None,
)
Precision manipulation through Isaac Lab
For precision, multi-stage bimanual manipulation such as Assemble Trocar, Rheo uses a focused Isaac Lab track where the OR twin is defined explicitly as a scene configuration: robot, cameras, USD scene, objects, and lighting.
@configclass
class AssembleTrocarSceneCfg(InteractiveSceneCfg):
"""Scene configuration for the assemble_trocar task."""
robot: ArticulationCfg = G1RobotPresets.g1_29dof_dex3_base_fix(...)
front_camera = CameraPresets.g1_front_camera(...)
left_wrist_camera = CameraPresets.left_dex3_wrist_camera(...)
right_wrist_camera = CameraPresets.right_dex3_wrist_camera(...)
scene = AssetBaseCfg(..., spawn=UsdFileCfg(usd_path="..."))
trocar_1 = RigidObjectCfg(..., spawn=UsdFileCfg(usd_path="..."), init_state=...)
trocar_2 = RigidObjectCfg(..., spawn=UsdFileCfg(usd_path="..."), init_state=...)
tray = ArticulationCfg(..., spawn=UsdFileCfg(usd_path="..."), init_state=..., actuators={})
light = AssetBaseCfg(..., spawn=sim_utils.DomeLightCfg(...))
Evaluating Trocar assembly in Isaac lab
Step 2: Capture expert experience
Rheo captures this experience as demonstrations in simulation, using devices appropriate to each task.
Record demonstrations for loco-manipulation (Meta Quest)
For tasks like surgical tray pick-and-place and case cart pushing:
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/record_demos_localmanip.py \
--dataset_file /datasets/demo.hdf5 \
--num_demos 1 \
--num_success_steps 50 \
--enable_pinocchio \
--enable_cameras \
--xr \
--teleop_device motion_controllers \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_pink
Key design point: the same runner that records data is also aligned with later synthetic generation (--mimic
), reducing format drift.
Record demonstrations for precision bimanual manipulation (Meta Quest)
For the Assemble Trocar task (GR00T N1.5 fine-tuning / RL post-training track):
./workflows/rheo/docker/run_docker.sh -g1.5 \
python scripts/sim/record_demos_assemble_trocar.py \
--task Isaac-Assemble-Trocar-G129-Dex3-Teleop \
--teleop_device motion_controllers \
--enable_pinocchio \
--enable_cameras \
--num_demos 1 \
--xr
Step 3: Multiply experience with synthetic data
Once you have a small set of successful demonstrations, the fastest way to improve coverage is to systematically diversify.
Rheo supports simulation-driven synthetic data generation for loco-manipulation tasks using Isaac Lab Mimic / SkillGen-style pipelines.
3a) Replay demos (sanity check)
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/replay_demos.py \
--dataset_file /datasets/demo.hdf5 \
--enable_cameras \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_pink
3b) Annotate demos (prepare for generation)
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/annotate_demos.py \
--input_file /datasets/demo.hdf5 \
--output_file /datasets/demo_annotated.hdf5 \
--enable_cameras \
--mimic \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_pink
3c) Generate a larger synthetic dataset
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/generate_dataset.py \
--enable_cameras \
--mimic \
--num_steps 150 \
--headless \
--input_file /datasets/demo_annotated.hdf5 \
--output_file /datasets/demo_generated.hdf5 \
--generation_num_trials 10 \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_pink
If you annotate multiple sources, you can merge them:
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/merge_demos.py \
--input /datasets/demo_annotated*.hdf5 \
--output /datasets/demo_merged.hdf5
3d) Convert to LeRobot format (for downstream training tooling)
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/utils/convert_hdf5_to_lerobot.py \
--config scripts/config/g1_locomanip_dataset_config.yaml
Cross-Scene Generalization with Generative Transfer
Isaac for Healthcare v0.5 includes a tutorial that references Cosmos Transfer 2.5 + guided generation to augment training data. In the included benchmark snapshot for Surgical Tray Pick-and-Place (success rate across four scenes), the Cosmos-augmented model improves robustness in shifted scenes:
| Model | Scene 1 | Scene 2 | Scene 3 | Scene 4 |
| Base model | 0.64 | 0.31 | 0.00 | 0.00 |
| Cosmos-augmented model | 0.60 | 0.49 | 0.37 | 0.30 |
The practical takeaway: domain shift is the key-enabler to train a robot in hospital environments, which has a different pattern of lighting, clutter, room geometry, etc. Synthetic diversification lets you stress these shifts earlier, when iteration is cheap.
Step 4: Train physical AI policies
Rheo supports two complementary training paths:
- Supervised fine-tuning (SFT) of GR00T models on curated datasets
- Online RL post-training (proximal policy optimization via RL infrastructure, or PPO via RLinf) to push hard precision stages over the line
4a) GR00T fine-tuning (entry point: launch_finetune.py
)
For fine-tuning on custom embodiments, the GR00T documentation uses gr00t/experiment/launch_finetune.py
as the entry point (see Fine-tune on Custom Embodiments (“NEW_EMBODIMENT”).
export NUM_GPUS=1
CUDA_VISIBLE_DEVICES=0 python \
gr00t/experiment/launch_finetune.py \
--base-model-path nvidia/GR00T-N1.6-3B \
--dataset-path <your-lerobot-v2-dataset> \
--embodiment-tag NEW_EMBODIMENT \
--modality-config-path <your-modality-config>.py \
--num-gpus $NUM_GPUS \
--output-dir <output-dir> \
--save-steps 2000 \
--max-steps 2000
Rheo provides task-specific modality definitions:
- Locomotion / loco-manipulation:
custom_g1_locomanip_modality_config.py (a --modality-config-path
module that registers aNEW_EMBODIMENT
modality config withego_view
video plus G1 state/action keys, including navigation commands). - Manipulation (Assemble Trocar):
gr00t_config.py
(definesUnitreeG1SimDataConfig
—video/state/action keys and transforms for the trocar dataset—used by the trocar fine-tuning and RL post-training workflow).
4b) Online RL post-training (PPO via RLinf) for precision stages
For Assemble Trocar, Rheo provides a turnkey launcher:
bash /workspaces/workflows/rheo/scripts/sim/rl/train_gr00t_assemble_trocar.sh train \
--model_path /models/<your_gr00t_checkpoint>
You can scale parallel environments or downshift for memory:
# scale up/down environments
bash /workspaces/workflows/rheo/scripts/sim/rl/train_gr00t_assemble_trocar.sh train \
--model_path /models/<your_gr00t_checkpoint> \
env.train.total_num_envs=32 env.eval.total_num_envs=4
# low-memory configuration
bash /workspaces/workflows/rheo/scripts/sim/rl/train_gr00t_assemble_trocar.sh train \
--model_path /models/<your_gr00t_checkpoint> \
env.train.total_num_envs=8 actor.micro_batch_size=2
Rheo’s RL tutorial decomposes Assemble Trocar into four stages (lift → align → insert → place) and reports large gains on later, harder stages after curriculum RL post-training:
| Model | Stage 1 | Stage 1+2 | Stage 1+2+3 | Stage 1+2+3+4 |
| Base model (SFT) | 83% | 72% | 32% | 29% |
| RL post-train Stage 1 | 100% | – | – | – |
| RL post-train Stage 2 | – | 92% | – | – |
| RL post-train Stage 3 | – | – | 85% | – |
| RL post-train Stage 4 | – | – | – | 82% |
Step 5: Validate before deployment
5a) Task-level evaluation (examples)
Assemble Trocar evaluation (GR00T N1.5, with optional RL checkpoint behavior patching):
./workflows/rheo/docker/run_docker.sh -g1.5 \
python -u -m sim.examples.eval_assemble_trocar \
--enable_cameras \
--task Isaac-Assemble-Trocar-G129-Dex3-Joint \
--model_path /models/GR00T-N1.5-RL-Rheo-AssembleTrocar \
--rl_ckpt \
--num_episodes 10 \
--max_steps 500
Surgical tray pick-and-place evaluation (GR00T closed loop):
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/examples/policy_runner.py \
--policy_type gr00t_closedloop \
--policy_config_yaml_path scripts/config/g1_gr00t_closedloop_pick_and_place_config.yaml \
--num_steps 15000 \
--enable_cameras \
--success_hold_steps 150 \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_joint
Case cart pushing evaluation:
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/examples/policy_runner.py \
--policy_type gr00t_closedloop \
--policy_config_yaml_path scripts/config/g1_gr00t_closedloop_push_cart_config.yaml \
--num_steps 20000 \
--enable_cameras \
--success_hold_steps 45 \
g1_locomanip_push_cart \
--object cart \
--embodiment g1_wbc_joint
5b) End-to-end integration smoke test (WebRTC + trigger API)
As a system-level check, Rheo provides a runner that (1) streams camera observations over WebRTC and (2) exposes a trigger endpoint so an external orchestrator can decide when to execute actions.
./workflows/rheo/docker/run_docker.sh -g1.6 \
python scripts/sim/examples/triggered_policy_runner.py \
--enable_cameras \
--webrtc_cam \
--webrtc_host 0.0.0.0 \
--webrtc_port 8080 \
--webrtc_fps 30 \
--trigger_port 8081 \
--trigger_host 0.0.0.0 \
g1_locomanip_tray_pick_and_place \
--object surgical_tray \
--embodiment g1_wbc_joint
To attach a VLM-based digital agent UI to this stream:
./tools/env_setup/install_vlm_surgical_agent_fx.sh
Then open http://127.0.0.1:8050
and connect the UI livestream to the WebRTC server (for example http://localhost:8080
).
Get started
To begin building with Project Rheo:
- Stand up an Isaac Sim environment
- Import or reconstruct a hospital space
- Record one expert workflow
- Generate synthetic variations
- Train a simple policy in Isaac Lab
- Run validation scenarios
Start small. One room. One task. One robot.
The workflow scales naturally from there.
Healthcare robotics is moving beyond static devices to autonomous, learning systems. Project Rheo transforms hospitals into continuous training environments, enabling systems to learn and adapt before they ever interact with a patient.
It’s time to build. Start architecting your next-generation medical AI with the Project Rheo blueprint today.
Featured image credit/PeritasAi
