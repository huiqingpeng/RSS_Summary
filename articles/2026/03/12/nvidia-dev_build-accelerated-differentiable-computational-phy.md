---
title: "Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/"
published: "2026-03-12"
fetched: "2026-03-13T07:04:19.912836"
---

Computer-Aided Engineering (CAE) is shifting from human-driven workflows toward AI-driven ones, including physics foundation models that generalize across geometries and operating conditions. Unlike LLMs, these models depend on large volumes of high-fidelity, physics-compliant data.
Recent scaling-law work on computational fluid dynamics (CFD) surrogates indicates that simulation-generated training data is often the limiting cost in practice. This pushes requirements onto the simulator, which must be GPU-native, fast, and able to plug directly into ML workflows.
NVIDIA Warp is a framework for accelerated simulation, data generation, and spatial computing that bridges CUDA and Python. Warp enables developers to write high-performance kernels as regular Python functions that are JIT-compiled into efficient code for execution on the GPU. Unlike the tensor-based frameworks, in which developers express computation as operations on entire N-dimensional arrays, developers author flexible kernels in the Warp framework that execute simultaneously across all elements of a computational grid.
Simulation kernels are often expressed on computational grids and rely on data-dependent control flow like conditionals, early-outs, and selective updates that vary per element. In tensor frameworks, these patterns require composing Boolean masks that quickly become unwieldy and can waste computation on irrelevant elements. In a Warp kernel, each thread can branch, skip, or exit independently, expressing this logic naturally without masking workarounds.
Furthermore, as this post will show, solvers written in Warp can be easily made differentiable through the Warp native support for automatic differentiation. They are straightforward to integrate with optimization or training workflows while remaining interoperable with frameworks like PyTorch, JAX, and NumPy for use cases spanning simulation, robotics, perception, and geometry processing.
This post walks you through how to build a 2D Navier–Stokes solver entirely in Warp. It explains how the Warp programming model maps onto a PDE solver. Then, it differentiates through the simulation to solve an optimal perturbation problem end-to-end. It closes with industrial case studies showcasing what Warp can enable in production workflows. For more information, see the 2D Navier–Stokes solver example and 2D Navier-Stokes optimal perturbation example on the NVIDIA/warp GitHub repo.
How to write a 2D Navier–Stokes solver using Warp
To keep the focus on Warp rather than on numerical methods, a textbook example of 2D decaying turbulence is used here, described by the vorticity-streamfunction formulation of the incompressible Navier-Stokes equations. The vorticity \(\omega\) evolves according to the transport equation:
\(\frac{\partial \omega}{\partial t} + \frac{\partial \psi}{\partial y}\frac{\partial \omega}{\partial x} – \frac{\partial \psi}{\partial x}\frac{\partial \omega}{\partial y} = \frac{1}{\text{Re}}\nabla^2 \omega \tag{1}\)
and the streamfunction \(\psi\) is recovered from vorticity through the Poisson equation:
\(\nabla^2 \psi = -\omega \tag{2}\)
With periodic boundary conditions, the equation above reduces to an algebraic equation in Fourier space bypassing the need for iterative solvers:
\(\hat{\psi}_{m,n} = \frac{\hat{\omega}_{m,n}}{k_x^2 + k_y^2} \tag{3}\)
where \((k_x, k_y)\) is the wavenumber pair in the Fourier space. The solver makes use of the Fast Fourier Transform (FFT) algorithm to efficiently transform \(\omega\) and \(\psi\) to Fourier space and vice versa.
Each timestep has two subcomponents (Figure 1). First, the vorticity transport equation is discretized on an \(N \times N\) grid over an \(L \times L\) square domain. The solution is marched forward in time by \(\Delta t\) using a third-order strong stability-preserving Runge-Kutta (RK3) scheme to obtain \(\omega(t+\Delta t)\). Second, the Poisson equation is solved in the Fourier space to obtain the updated \(\psi(t+\Delta t)\).
Thus, the forward solver has two building blocks that will be described in the subsequent sections:
- Warp kernel for the discretization and time marching
- FFT-based Poisson solver
Building block 1: Finite-difference discretization and time marching
The advection and diffusion terms in the vorticity transport equation are approximated with second-order central finite differences shown in Figure 2. Higher-order discretization could also be used, but the central second-order scheme is chosen for simplicity.
The following rk3_update()
kernel computes the diffusion and the advection terms and performs a single RK3 substep update. The step()
function calls this kernel three times per timestep, once for each RK3 stage, with different coefficients (coeff0
, coeff1
, coeff2
) for each stage.
@wp.kernel
def rk3_update(
n: int, h: float, re: float, dt: float,
coeff0: float, coeff1: float, coeff2: float,
omega_0: wp.array2d(dtype=float),
omega_1: wp.array2d(dtype=float),
psi: wp.array2d(dtype=float),
omega_out: wp.array2d(dtype=float)
):
"""Perform a single substep of SSP-RK3."""
i, j = wp.tid()
left = cyclic_index(i - 1, n)
right = cyclic_index(i + 1, n)
top = cyclic_index(j + 1, n)
down = cyclic_index(j - 1, n)
inv_h2 = 1.0 / (h * h)
laplacian = (
omega_1[right, j] + omega_1[left, j] + omega_1[i, top] + omega_1[i, down] - 4.0 * omega_1[i,j]
) * inv_h2
inv_2h = 1.0 / (2.0 * h)
j1 = ((omega_1[right, j] - omega_1[left, j]) * inv_2h) * ((psi[i, top] - psi[i, down]) * inv_2h)
j2 = ((omega_1[i, top] - omega_1[i, down]) * inv_2h) * ((psi[right, j] - psi[left, j]) * inv_2h)
rhs = (1.0 / re) * laplacian + j2 - j1
omega_out[i, j] = coeff0 * omega_0[i, j] + coeff1 * omega_1[i, j] + coeff2 * dt * rhs
The rk3_update()
kernel follows the single-instruction, multiple-threads (SIMT) paradigm where each thread maps to one grid point on the computational domain, and all \(N \times N\) points are updated simultaneously with a single wp.launch()
call.
wp.launch(rk3_update,
dim=(self.n, self.n), # one thread per grid point
inputs=[self.n, self.h, self.re, self.dt,
stage_coeff[0], stage_coeff[1], stage_coeff[2],
self.omega_0,
self.omega_1,
self.psi,
],
outputs=[self.omega_tmp]
)
Building block 2: FFT Poisson solver
Warp tile-based primitives enable solving the Poisson equation in Fourier space. The key operations are wp.tile_fft()
and wp.tile_ifft()
, which perform the forward and inverse FFT, respectively, on a single row loaded into a tile. A full 2D FFT on an \(N \times N\) array is then decomposed into three steps: row-wise FFT -> transpose -> row-wise FFT. The schematic in Figure 4 explains how fft_tiled()
and ifft_tiled()
compute the forward and inverse FFT under the hood.
@wp.kernel
def fft_tiled(x: wp.array2d(dtype=wp.vec2f), y: wp.array2d(dtype=wp.vec2f)):
"""Row-wise FFT using tile primitives."""
i, _, _ = wp.tid()
a = wp.tile_load(x, shape=(1, N_GRID), offset=(i, 0))
wp.tile_fft(a)
wp.tile_store(y, a, offset=(i, 0))
@wp.kernel
def ifft_tiled(x: wp.array2d(dtype=wp.vec2f), y: wp.array2d(dtype=wp.vec2f)):
"""Row-wise inverse FFT using tile primitives."""
i, _, _ = wp.tid()
a = wp.tile_load(x, shape=(1, N_GRID), offset=(i, 0))
wp.tile_ifft(a)
wp.tile_store(y, a, offset=(i, 0))
tile_fft
on an NxN grid. Each block loads one row into a register tile, computes the FFT cooperatively, and stores the result back to global memoryA 2D FFT also requires a transpose between the row-wise passes. This can use either the SIMT or tile paradigm (through wp.tile_transpose
). For simplicity, the SIMT version is shown below:
@wp.kernel
def transpose(x: wp.array2d(dtype=wp.vec2f), y: wp.array2d(dtype=wp.vec2f)):
i, j = wp.tid()
y[i, j] = x[j, i]
Composing these three kernels, fft_tiled
-> transpose
-> fft_tiled
, together gives a full 2D forward FFT. The inverse follows the same pattern with ifft_tiled
.
Putting the building blocks together
The step()
function in the example relies on a few other helper kernels that are not discussed in detail here. For the definitions of those kernels, see the 2D Navier–Stokes solver example on the NVIDIA/warp GitHub repo. With all the building blocks in place, a single step()
call advances the simulation by one timestep. The self._solve_poisson()
method in the example code abstracts away the \(\omega(t+\Delta t) \xrightarrow{\text{FFT}} \hat{\omega} \xrightarrow{\text{Eq.\,3}} \hat{\psi} \xrightarrow{\text{IFFT}} \psi(t+\Delta t)\) pipeline for modularity.
def step(self) -> None:
"""Advance simulation by one timestep using SSP-RK3."""
for stage_coeff in self.rk3_coeffs:
wp.launch(
rk3_update,
dim=(self.n, self.n),
inputs=[
self.n, self.h, self.re, self.dt,
stage_coeff[0], stage_coeff[1], stage_coeff[2],
self.omega_0,
self.omega_1,
self.psi,
],
outputs=[self.omega_tmp],
)
# Swap buffers for next RK3 substep
self.omega_1, self.omega_tmp = self.omega_tmp, self.omega_1
# Update streamfunction for next timestep
self._solve_poisson()
# Copy updated vorticity to self.omega_0 for the next timestep
wp.copy(self.omega_0, self.omega_1)
Running the solver produces the decaying turbulence field shown in Figure 5. On the GPU, the step()
function is captured into a CUDA Graph through wp.ScopedCapture
and replayed with wp.capture_launch()
for all subsequent frames, eliminating per-launch overhead.
Differentiating through the solver
Now that the working solver has been built, the next question is how to make it differentiable.
Automatic differentiation (AD) computes exact derivatives of a program by applying the chain rule to each elementary operation in the computational graph. Unlike finite differences, AD avoids step-size tuning and yields gradients accurate to machine precision. The key advantage of AD for PDE solvers is scaling: with a complex simulation on a large grid, each forward solve is already expensive, so methods like finite differences require \(O(n)\) full solves to get gradients with regard to \(n\) inputs.
Reverse-mode AD computes all \(\partial \mathcal{L}/\partial x_i\) in roughly one forward pass plus one backward pass, making gradient-based optimization practical at production resolution. This is the same idea as backpropagation in neural nets, and it is why both deep learning and large-scale physics optimization can handle millions of degrees of freedom.
The Warp automatic differentiation system generates two versions of a program at compile time for a differentiable simulation:
- Forward version: The code that takes physical inputs (initial conditions, discretized governing laws, and so on) and computes the simulation output (fields, derived quantities) as well as intermediate arrays needed for the adjoint version.
- Adjoint version: An automatically generated counterpart to the forward simulation that can take sensitivities of a chosen quantity of interest with respect to the simulation outputs and propagate them all the way back to the inputs. This backward propagation reuses intermediate arrays from the forward execution to apply the chain rule of differentiation across the entire solver, yielding the simulation adjoint without constructing large symbolic expressions.
Developers write the forward physics and Warp handles the gradient computation. Any wp.array
that should be differentiable is allocated with requires_grad=True
, which tells Warp to allocate a companion array for adjoint storage. The resulting adjoints can be used standalone (as in this example) or interoperated with PyTorch or JAX for end-to-end optimization, including training ML models. Currently, Warp supports reverse-mode AD only.
To illustrate, the optimal perturbation problem outlined in Prediction and Control of Two-Dimensional Decaying Turbulence Using Generative Adversarial Networks is tackled here. In turbulent flows, small perturbations to the initial conditions can amplify over time and significantly alter the trajectory of the flow. Identifying which perturbations grow the fastest is a stepping stone toward flow control and toward understanding which structures in the flow are dynamically significant. Concretely, the initial vorticity perturbation \(\Delta\omega\) is sought, which maximizes the divergence between perturbed and unperturbed trajectories at a lead time \(\tau\).
Let \(F^{\tau}\) denote the forward solver applied for \(\tau\) time units. The unperturbed trajectory is \(Y^{*} = F^{\tau}(\omega_0)\) and the perturbed trajectory is \(\tilde{Y} = F^{\tau}(\omega_0 + \Delta\omega)\). The mean squared error (MSE)
\(\mathrm{MSE} = -\frac{1}{N^2}\left\| Y^* – \tilde{Y} \right\|_2^2 \tag{4}\)
is minimized, where the negative sign turns maximization of trajectory divergence into a minimization problem. To constrain the optimization, \(\mathrm{rms}(\Delta\omega) \leq 0.2 \times \mathrm{rms}(\omega_0)\), that is, the perturbation RMS must not exceed 20% of the RMS of the initial vorticity field \(\omega_0\).
For more details, see the 2D Navier-Stokes optimal perturbation example on the NVIDIA/warp GitHub repo. The following sections focus on the three key changes in the forward solver that would make it differentiable.
No in-place modifications
wp.Tape()
records kernel launches in the forward pass and replays them in reverse to compute gradients. That only works if the intermediate values needed by the backward pass are still available, so arrays cannot be freely overwritten in place. This is the key difference from the nondifferentiable solver. In the forward-only version, two arrays could be switched, omega_0
and omega_1
, at the end of each timestep:
wp.copy(omega_0, omega_1)
For the differentiable solver, the RHS computation and the RK3 update need to be split into separate kernels that write to separate arrays. Thus a single RK3 update becomes the following. Note that omega_1
values cannot be copied to omega_0
at the end of each timestep as before.
omega_out[i, j] = coeff0 * omega_0[i, j] + coeff1 * omega_in[i, j] + coeff2 * dt * rhs[i, j]
In Warp, all the intermediate arrays need to be explicitly defined by the user. This requires pre-allocating separate arrays for every RK substep at every timestep, which is the generally dominant GPU memory cost of any differentiable solver.
self.omega_timestep = [wp.zeros((n, n), dtype=wp.float32, requires_grad=True) for _ in range(T + 1)]
# Intermediate arrays for each RK3 substep for each timestep
self.omega_stage = []
self.psi_stage = []
self.rhs_stage = []
self.fft_arrays = []
for _ in range(T):
s_omega, s_psi, s_rhs, s_fft = [], [], [], []
for _ in range(3):
s_omega.append(wp.zeros((n, n), dtype=wp.float32, requires_grad=True))
s_psi.append(wp.zeros((n, n), dtype=wp.float32, requires_grad=True))
s_rhs.append(wp.zeros((n, n), dtype=wp.float32, requires_grad=True))
s_fft.append({"omega_complex": wp.zeros((n, n), dtype=wp.vec2f, requires_grad=True),
# ... plus 4 FFT scratch arrays, each (n, n) vec2f
})
self.omega_stage.append(s_omega)
self.psi_stage.append(s_psi)
self.rhs_stage.append(s_rhs)
self.fft_arrays.append(s_fft)
Storing Warp arrays for every intermediate state scales linearly with the number of timesteps, which becomes prohibitive in long runs. One common approach is gradient checkpointing, saving only selected states, then recomputing the missing segments using the forward solver during the backward pass. This method trades extra forward compute for a much smaller memory footprint. For an example showing how to implement gradient checkpointing in Warp, see the fluid checkpoint example on the NVIDIA/warp GitHub repo.
Recording gradients with wp.Tape()
With the pre-allocated arrays in place, recording and differentiating the forward pass is straightforward:
with wp.Tape() as tape:
forward() # wp.launch calls that take omega from t0 to t0 + lead t and calculate MSE
tape.backward(loss) # Automatic differentiation to get derivatives of loss w.r.t Warp arrays
The wp.Tape()
context records every wp.launch()
call into a computational graph. tape.backward(loss)
traverses that graph in reverse, computing the derivatives of loss
with respect to the Warp arrays. Here the focus is the gradients of loss
with respect to \(\Delta{\omega}\), which can be obtained through delta_omega.grad
.
Optimization loop
The following code block shows one optimization step. The forward()
function is run on the perturbed initial vorticity to produce the final field and loss (MSE versus the unperturbed run). The tape records the kernel launches during this pass. tape.backward(loss)
then backpropagates through the recorded graph to compute gradients with regard to the perturbation, and optimizer.step()
updates the perturbation to reduce the loss. Finally, tape.zero()
clears accumulated gradients before the next iteration.
with wp.Tape() as tape:
forward() # Loss is computed inside forward() function
tape.backward(loss)
optimizer.step([delta_omega.grad.flatten()])
tape.zero()
After 1,000 iterations, the optimizer discovers a structured perturbation \(\Delta\omega\) that amplifies trajectory divergence, driving the MSE from near-zero to ~250. The perturbation field obtained from the solver-in-the-loop optimization qualitatively resembles the one reported in Prediction and Control of Two-Dimensional Decaying Turbulence Using Generative Adversarial Networks.
To learn more, the NVIDIA/warp GitHub repo includes additional differentiable-solver examples beyond CFD. See also a growing list of research publications that leverage Warp.
Warp in practice: Case studies of AI-driven industrial workflows
In real AI workflows, simulation and geometry sit inside larger systems (surrogate models, RL, design optimization, and so on). PyTorch and JAX handle training and tensor ops, but the simulation layer adds staged timestepping, stencil updates, and big spatial queries. Warp targets that kernel-heavy layer: you control execution, fuse kernels to cut memory traffic and launches, and use CUDA Graphs to reduce repeated dispatch. It also interoperates zero-copy with PyTorch and JAX tensors.
Autodesk XLB
Autodesk Research built XLB, a differentiable Lattice Boltzmann solver in Python with both Warp and JAX backends, enabling a direct comparison on the same formulation and hardware. On a ~134-million-cell lid-driven cavity benchmark, Warp ran about 8x faster than JAX on a single 40 GB NVIDIA A100 Tensor Core GPU, roughly matching the throughput that JAX needed eight A100 Tensor Core GPUs to reach. At larger sizes, Warp used ~2.5x–3x less memory and completed the largest case, on which JAX ran out of memory on the same GPU.
To learn more, see Autodesk Research Brings Warp Speed to Computational Fluid Dynamics on NVIDIA GH200.
Google DeepMind MuJoCo
Google DeepMind has recently released MuJoCo Warp (MJWarp), a Warp-based backend for large-scale multibody dynamics. The Warp backend reaches up to 252x (locomotion) and 475x (manipulation) speedups over JAX on comparable hardware. MJWarp gets there by exploiting sparse matrix operations and speculative execution to more precisely dispatch compute, while remaining plug-compatible with JAX training.
To learn more, see the MuJoCo Warp release announcement.
C-Infinity AutoAssembler
The C-Infinity AutoAssembler ASI Engine shows the value of Warp in AI-driven industrial workflows beyond physics simulation. It converts full-fidelity CAD assemblies into motion constraints for AI planning by computing contact, interference, and clearance directly from raw geometry. Current CAD systems do not support these critical queries, which are required to construct manufacturing process plans, evaluate design changes, and generate execution instructions.
The AutoAssembler ASI engine enables building a manufacturing compiler, transforming engineering CAD data directly to assembly instructions for either human or robot consumption. The technology is implemented using Warp kernels optimized for large scale processing to build spatial intelligence.
On an NVIDIA L4 Tensor Core GPU, the Warp GPU backend achieved a speedup of up to 669x over optimized CPU baselines (based on state of the art libraries including FCL plus Embree). The technology is already in use within enterprise manufacturing workflows at top OEMs.
To learn more, see AutoAssembler ASI: Accelerated Spatial Intelligence, C-Infinity.
Get started with Warp for computational physics applications
Warp enables you to write physics and geometry as GPU kernels in Python, without forcing everything into tensor-based frameworks. In CFD, timestepping and differentiable solves map cleanly to kernels, keeping the structure of the physics intact.
This model already shows up in industrial AI workflows, including the Autodesk differentiable CFD solver, the Google DeepMind multibody dynamics work, and the C-Infinity spatial reasoning engine. With zero-copy interop to PyTorch and JAX, Warp plugs into ML pipelines while preserving the control flow these workloads need, with measured gains in performance, memory, and scalability.
To get started with Warp for computational physics applications, check out these resources:
- Introduction to NVIDIA Warp notebook
- 2D Navier–Stokes solver example
- 2D Navier-Stokes optimal perturbation example
- NVIDIA Warp documentation
To learn more, join the NVIDIA GTC 2026 session, How to Use NVIDIA Warp to Build GPU-Accelerated Computational Physics Simulations [DLIT81837]. Watch the GTC keynote with NVIDIA founder and CEO Jensen Huang and explore more physical AI, robotics, and vision AI GTC sessions.
Acknowledgments
Thanks to Felix Meyer for contributing to this post and project.
