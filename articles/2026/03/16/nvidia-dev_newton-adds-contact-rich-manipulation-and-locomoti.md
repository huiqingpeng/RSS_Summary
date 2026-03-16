---
title: "Newton Adds Contact-Rich Manipulation and Locomotion Capabilities for Industrial Robotics"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/"
published: "2026-03-16"
fetched: "2026-03-17T07:08:07.456059"
---

Physics forms the foundation of robotic simulation, enabling realistic modeling of motion and interaction. For tasks like locomotion and manipulation, simulators must handle complex dynamics such as contact forces and deformable objects. While most engines trade off speed for realism, Newton—a GPU-accelerated, open source simulator—is designed to do both.
Newton 1.0 GA, announced at NVIDIA GTC 2026, is delivering an accelerated, production-ready foundation for dexterous manipulation and locomotion tasks. As an extensible physics engine built on NVIDIA Warp and OpenUSD, robots can learn how to handle complex tasks with greater precision, speed, and extensibility while using frameworks such as NVIDIA Isaac Lab and NVIDIA Isaac Sim.
Newton is a modular framework that brings together multiple solvers and simulation components behind a unified architecture. Rather than being tied to a single scene format, it supports a broad runtime data model that spans common robotics descriptions such as MJCF, URDF, and OpenUSD, making it easier to connect existing robot assets and workflows. Teams can mix and match collision detection, contact models, sensors, control, and solver backends—rigid-body and deformable solvers as well as custom solvers—while keeping a consistent simulation stack for robot learning and development.
Highlights of this release include:
- Stable API: Newton API provides a stable, unified interface for a wide range of capabilities in modeling, solving, controlling, and sensing in the simulation.
- Versatile rigid-body solvers: Newton ships with several rigid-body solvers. MuJoCo and Kamino have the most advanced and complementary capabilities:
- Kamino, developed by Disney Research, handles complex mechanisms such as robotic hands and legged systems with closed-loop linkages and passive actuation. It enables a new class of simulation capabilities, giving mechanical designers the freedom to design systems without worrying about simulatability, while paving the way for scalable reinforcement learning.
- MuJoCo 3.5 (MJWarp) builds on the stability and accuracy the robotics community already trusts in MuJoCo, developed by Google DeepMind, now extended with GPU-scale throughput for thousands of parallel training environments. New optimizations enable MuJoCo Warp to speed up MJX by 252x for locomotion, and 475x for manipulation tasks on the NVIDIA RTX PRO 6000 Blackwell Series.
- Rich deformable simulation: Powered by the Vertex Block Descent (VBD) solver, Newton handles linear deformables (cables), thin deformables (cloth), and volumetric deformables (rubber parts), covering common materials found in real industrial settings. Also, the Implicit Material Point Method (iMPM) handles particle simulation (granular material) applicable to rough terrain locomotion scenarios. The VBD and MPM solvers can be coupled with MuJoCo Warp explicitly to support deformable manipulation and locomotion scenarios with robotic systems.
- Collision library: A flexible and fast collision detection pipeline enables selection of the right broadphase and narrowphase detection approaches based on scene complexity. The pipeline is reusable and can accelerate custom solver development. The library includes advanced contact generation and modeling:
- Signed distance field (SDF)-based collision captures complex geometries directly from CAD-exported meshes, eliminating the need for mesh approximation methods. This is critical for tight-tolerance tasks such as connector insertion or in-hand manipulation.
- Hydroelastic contacts, inspired by this Drake contact model, use a continuous pressure distribution across finite-area contact patches rather than a set of contact points. This provides higher-fidelity and more robust object interaction required for tactile sensing and manipulation policies, ultimately achieving better sim-to-real transfer.
- OpenUSD and Isaac integration: With OpenUSD as a common data layer, Newton integrates natively with NVIDIA Isaac Sim 6.0 and Isaac Lab 3.0 early access releases, enabling faster workflows from robot description to trained policy and evaluation pipelines across reinforcement and imitation learning workflows.
- Tiled camera sensor: A Warp-based tiled camera sensor supports high-throughput simplified rendering with channels for RGB, depth, albedo, surface normals, and instance segmentation. Designed to scale vision-based RL policies, it enables end-to-end perceptive training pipelines to run on the NVIDIA DGX platform. The rendering backend is ray-tracing-based and supports multiple scene representations, including triangle meshes and Gaussian splats.
Newton is a Linux Foundation project founded by NVIDIA, Google DeepMind, and Disney Research. Lightwheel, a leader in simulation infrastructure for physical AI, has joined forces with Newton to advance solver calibration, define the SimReady standard, and develop the next generation of physically grounded SimReady assets. Toyota Research Institute (TRI), developer of the Drake physics engine, is also partnering with Newton to advance solver development and contact modeling capabilities.
The next section walks through how these capabilities come together in locomotion and manipulation workflows.
Simulating complex mechanisms with Kamino
The Kamino solver handles complex and intricate closed-chain mechanisms, such as robots with kinematics that include parallel linkage mechanisms. This enables the simulation of mechanisms like multi-link walking robots, where kinematics can include several closed loops in each leg. An example is Dr. Legs, a closed-chain robotic leg mechanism available in the Newton asset repository, which demonstrates how Kamino handles articulated structures with multiple closed loops.
Newton workflows follow a consistent pattern: build or import a model, initialize the state, apply controls (such as joint targets or forces), and step a solver such as Kamino to advance the physics, with results visualized through the viewer.
import newton
# Import the articulation model from USD
builder = newton.ModelBuilder()
# Register attributes to be parsed specific to Kamino
newton.solvers.SolverKamino.register_custom_attributes(builder)
# Import USD asset
builder.add_usd("robot.usd")
# Finalize the model (upload to GPU)
model = builder.finalize()
# Create Kamino solver
solver = newton.solvers.SolverKamino(model)
# Create state and control objects
state_0 = model.state()
state_1 = model.state()
control = model.control()
contacts = model.contacts()
# Simulation loop
for i in range(num_steps):
state_0.clear_forces()
model.collide(state_0, contacts)
# Forward dynamics
solver.step(state_0, state_1,
control, contacts, sim_dt)
# Swap states
state_0, state_1 = state_1, state_0
Manipulation workflow with Newton and Isaac Lab
NVIDIA Isaac Lab is an open source framework for robot learning. Researchers and developers can define simulation environments, set up reinforcement learning (RL) and imitation learning pipelines, and train policies at GPU scale. Users define a scene (robots, objects, terrain), an MDP (observations, actions, rewards, terminations), and a simulation backend. Newton integrates with Isaac Lab as a new physics and camera-sensor backend, further expanding Isaac Lab’s capabilities.
In an Isaac Lab RL workflow, everything above the physics layer—the task definition, PPO training loop, observation and reward functions—stays identical. Only the simulation backend changes. This means developers can author an environment once and validate it across different physics engines, building confidence in policy robustness before real-world deployment.
Together, Newton and Isaac Lab can build an RL pipeline for training a Franka robot to pick up a cube object. Once the scene is configured, configure the physics settings. The following example shows how Isaac Lab is using a three-layer physics configuration for the Franka robot cube manipulation environment.
from isaaclab.sim import SimulationCfg
from isaaclab_newton.physics import NewtonCfg, MJWarpSolverCfg
# Configure Newton MJWarp simulation for the Franka Cube Env
FrankaCubeEnvCfg.solver_cfg = MJWarpSolverCfg(
solver="newton",
integrator="implicitfast",
njmax=2000,
nconmax=1000,
impratio=1000.0,
cone="elliptic",
update_data_interval=2,
iterations=20,
ls_iterations=100,
ls_parallel=True,
)
FrankaCubeEnvCfg.newton_cfg = NewtonCfg(
solver_cfg=FrankaCubeEnvCfg.solver_cfg,
num_substeps=2,
debug_mode=False,
)
FrankaCubeEnvCfg.sim = SimulationCfg(
dt=1 / 120,
render_interval=FrankaCubeEnvCfg.decimation,
physics=FrankaCubeEnvCfg.newton_cfg,
)
All other steps, such as applying actions, getting rewards, and resetting the environment, remain the same.
How Newton is being used in industrial applications
The following two examples show how Newton’s capabilities come together in production robotics workflows. One focuses on rigid-body precision assembly and the other on dexterous manipulation of deformable materials.
GPU rack assembly automation
Skild AI is training reinforcement learning policies for GPU rack assembly for their industrial end-users, one of the most demanding contact-rich tasks in electronics manufacturing. Connector insertion, board placement, and fastening require stable collision and contact, reliable force feedback, and full-fidelity geometric representation that most simulators cannot provide at training scale.
Skild is using Isaac Lab with the Newton backend for their electronics assembly automation tasks. In their workflows, the SDF-based collision detection and hydroelastic contact modeling are used to bypass MuJoCo Warp’s native collision and contact pipeline, enabling higher contact fidelity. Shapes are configured with precomputed SDFs built from the original CAD geometry, enabling Newton to operate on non-convex tri-mesh models that accurately represent the geometry of assembly components.
SDF collision is useful for rigid, non-compliant interactions with complex geometry, enabling precise contact queries against connectors, boards, and other tightly-toleranced parts.
For richer contact dynamics, hydroelastic modeling introduces compliance that produces distributed pressure contacts rather than point-contact approximations. This creates larger contact areas that capture frictional behavior, including torsional friction effects that can arise during complex object manipulation sequences. Together, the SDF geometry representation and hydroelastic contact model provide the fidelity required to train policies that can reliably transfer to real industrial assembly systems.
The following snippet shows how SDF collisions and hydroelastic contacts are configured:
import newton
from newton.geometry import HydroelasticSDF
# --- 1. Shape configuration: enable hydroelastic contact ---
shape_cfg = newton.ModelBuilder.ShapeConfig(
mu=1.0, # friction coefficient
gap=0.01, # contact detection margin [m]
ke=5.0e4, # elastic contact stiffness (MJWarp fallback)
kd=5.0e2, # contact damping
kh=1.0e11, # hydroelastic stiffness [Pa/m] — controls
# pressure vs. penetration across the contact patch
)
# --- 2. Build SDF on each collision mesh ---
# Precompute a sparse signed-distance field so Newton can find
# sub-voxel contact surfaces via marching cubes at runtime.
for mesh in assembly_meshes:
mesh.build_sdf(
max_resolution=128, # SDF grid resolution
narrow_band_range=(-0.01, 0.01), # ±10 mm band around surface
margin=shape_cfg.gap,
)
# --- 3. Mark shapes as hydroelastic ---
# When both shapes in a colliding pair carry this flag, Newton
# routes them through the SDF-hydroelastic pipeline instead of
# MJWarp's native point-contact solver.
for shape_idx in range(builder.shape_count):
builder.shape_flags[shape_idx] |= newton.ShapeFlags.HYDROELASTIC
# --- 4. Create the collision pipeline with hydroelastic config ---
collision_pipeline = newton.CollisionPipeline(
model,
reduce_contacts=True, # contact-reduction for stable solving
broad_phase="explicit", # precomputed shape pairs (few shapes)
sdf_hydroelastic_config=HydroelasticSDF.Config(
output_contact_surface=False, # skip surface mesh export
),
)
# --- 5. Simulation loop (unchanged from standard Newton) ---
# The solver receives distributed contact patches transparently.
collision_pipeline.collide(state, contacts)
solver.step(state_0, state_1, control, contacts, dt)
Cable manipulation for refrigerator assembly
Samsung will use Newton for physically-grounded synthetic data generation (SDG) used for training their vision-language-action (VLA) models.
Lightwheel is applying Newton to generate SimReady assets for Newton with proper tuning based on real-world measurements and verification. This enables a variety of complex industrial assembly tasks, including cable manipulation tasks in Samsung manufacturing workflows. Cables are among the hardest objects to simulate reliably, they exhibit complex 1D deformable behavior, self-collision, and force-dependent shape changes that canonical solvers cannot capture accurately.
Samsung and Lightwheel’s work illustrates how Newton’s deformable simulation stack, spanning cables through volumetric solids, enables synthetic data generation and policy training on the full range of materials found in real electronics assembly lines.
Newton’s VBD solver enables simulating linear deformables such as cables. Two-way coupling with rigid-body solvers like MuJoCo Warp enables robot motion to physically interact with cable deformation during simulation. Combined with Newton’s stable collision and high-fidelity contact modeling, this setup enables simulation of tasks such as inserting a refrigerator water-hose connector into its housing. The snippet shows how VBD and MuJoCo Warp are coupled.
import warp as wp
import newton
from newton.solvers import SolverMuJoCo, SolverVBD
# --- Universe A: MuJoCo rigid-body robot ---
robot_model = robot_builder.finalize()
mj_solver = SolverMuJoCo(
robot_model,
solver="newton",
integrator="implicitfast",
cone="elliptic",
iterations=20,
ls_iterations=10,
ls_parallel=True,
impratio=1000.0,
)
robot_state_0 = robot_model.state()
robot_state_1 = robot_model.state()
control = robot_model.control()
mj_collision_pipeline = newton.CollisionPipeline(
robot_model,
reduce_contacts=True,
broad_phase="explicit",
)
mj_contacts = mj_collision_pipeline.contacts()
# --- Universe B: VBD deformable cable ---
cable_builder = newton.ModelBuilder()
cable_builder.add_rod(
positions=cable_points, # polyline vertices [m]
quaternions=cable_quats, # parallel-transport frames
radius=0.003, # cable cross-section radius [m]
stretch_stiffness=1e12, # EA [N]
bend_stiffness=3.0, # EI [N*m^2]
stretch_damping=1e-3,
bend_damping=1.0,
)
# --- Proxy bodies: robot links mirrored into VBD ---
for body_id in proxy_body_ids:
# Effective mass: reflects the inertia of the full articulated
# chain when applicable, optionally scaled for coupling stability.
proxy_id = cable_builder.add_body(
xform=robot_state_0.body_q[body_id],
mass=effective_mass[body_id],
)
for shape in shapes_on_body(robot_model, body_id):
cable_builder.add_shape(body=proxy_id, **shape)
robot_to_vbd[body_id] = proxy_id
cable_model = cable_builder.finalize()
vbd_solver = SolverVBD(
cable_model,
iterations=10,
)
vbd_state_0 = cable_model.state()
vbd_state_1 = cable_model.state()
vbd_control = cable_model.control()
vbd_collision_pipeline = newton.CollisionPipeline(cable_model)
vbd_contacts = vbd_collision_pipeline.contacts()
proxy_forces = wp.zeros(robot_model.body_count, dtype=wp.spatial_vector)
coupling_forces_cache = wp.zeros_like(proxy_forces)
@wp.kernel
def sync_proxy_state(
robot_ids: wp.array(dtype=int),
proxy_ids: wp.array(dtype=int),
src_body_q: wp.array(dtype=wp.transform),
src_body_qd: wp.array(dtype=wp.spatial_vector),
dst_body_q: wp.array(dtype=wp.transform),
dst_body_qd: wp.array(dtype=wp.spatial_vector),
proxy_forces: wp.array(dtype=wp.spatial_vector),
body_inv_mass: wp.array(dtype=float),
body_inv_inertia: wp.array(dtype=wp.mat33),
gravity: wp.vec3,
dt: float,
):
i = wp.tid()
rid = robot_ids[i]
pid = proxy_ids[i]
# Copy pose and velocity from robot to proxy
dst_body_q[pid] = src_body_q[rid]
qd = src_body_qd[rid]
# Undo coupling forces + gravity on proxy velocity
f = proxy_forces[rid]
delta_v = dt * body_inv_mass[pid] * wp.spatial_top(f)
r = wp.transform_get_rotation(dst_body_q[pid])
delta_w = dt * wp.quat_rotate(r, body_inv_inertia[pid] * wp.quat_rotate_inv(r, wp.spatial_bottom(f)))
qd = qd - wp.spatial_vector(delta_v + dt * body_inv_mass[pid] * gravity, delta_w)
dst_body_qd[pid] = qd
# --- Coupled step (staggered, one-step lag) ---
# Step 1 -- Apply lagged VBD-to-MuJoCo wrenches
robot_state_0.clear_forces()
coupling_forces_cache.assign(proxy_forces)
robot_state_0.body_f.assign(robot_state_0.body_f + coupling_forces_cache)
# Step 2 -- Advance MuJoCo (rigid-body robot)
mj_collision_pipeline.collide(robot_state_0, mj_contacts)
mj_solver.step(robot_state_0, robot_state_1, control, mj_contacts, dt)
robot_state_0, robot_state_1 = robot_state_1, robot_state_0
# Step 3 + 4 -- Sync proxy poses/velocities and undo coupling forces (single kernel)
wp.launch(
sync_proxy_state,
dim=len(proxy_body_ids),
inputs=[
robot_ids_wp, proxy_ids_wp,
robot_state_0.body_q, robot_state_0.body_qd,
vbd_state_0.body_q, vbd_state_0.body_qd,
coupling_forces_cache,
cable_model.body_inv_mass, cable_model.body_inv_inertia,
gravity, dt,
],
)
# Step 5 -- Advance VBD (cable deformation + cable-proxy contacts)
vbd_collision_pipeline.collide(vbd_state_0, vbd_contacts)
vbd_solver.step(vbd_state_0, vbd_state_1, vbd_control, vbd_contacts, dt)
# Step 6 -- Harvest contact wrenches from proxy bodies (applied at next step)
proxy_forces = harvest_proxy_wrenches(vbd_solver, vbd_state_1, vbd_contacts, dt)
vbd_state_0, vbd_state_1 = vbd_state_1, vbd_state_0
Samsung and Lightwheel’s work shows how Newton’s deformable simulation stack enables synthetic data generation and policy training on the full range of materials found in real electronics assembly lines.
How to get started with Newton
Newton is free to use, modify, and extend. To get started:
- Explore the newton-physics/newton GitHub repo for standalone Newton examples and documentation.
- Try the dexterous manipulation and locomotion workflows on isaac-sim/IsaacLab GitHub.
If you’re attending NVIDIA GTC 2026, check out the following sessions:
- Disney’s Robotic Characters: From the Screen to Reality via Physical AI
- An Introduction to Newton Physics Engine for Robotics
- Accelerate Robot Learning with NVIDIA Isaac Lab and Newton
- Build Robot-Ready Assets for Physically Accurate Simulations With Lightwheel
- How to use NVIDIA Warp to Build GPU-Accelerated Computational Physics Simulations
Stay up to date by subscribing to our newsletter and following NVIDIA Robotics on LinkedIn, Instagram, X, and Facebook. Explore NVIDIA documentation and YouTube channels, and join the NVIDIA Developer Robotics forum. To start your robotics journey, enroll in our free NVIDIA Robotics Fundamentals courses today.
Get started with NVIDIA Isaac libraries and AI models for developing physical AI systems.
Watch the NVIDIA GTC 2026 keynote with NVIDIA founder and CEO Jensen Huang and explore more physical AI, robotics, and vision AI GTC sessions.
