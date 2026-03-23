---
title: "Building a Zero-Trust Architecture for Confidential AI Factories"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/building-a-zero-trust-architecture-for-confidential-ai-factories/"
published: "2026-03-23"
fetched: "2026-03-24T07:13:12.092940"
---

AI is moving from experimentation to production. However, most data enterprises need exists outside the public cloud. This includes sensitive information like patient records, market research, and legacy systems containing enterprise knowledge. There’s also a risk of using private data with AI models, and adoption is often slowed or blocked by privacy and trust concerns.
Enterprises building next-generation AI factories—specializing in high-performance infrastructure to manufacture intelligence at scale—must be built on a zero-trust foundation. This security architecture eliminates implicit trust in the underlying host infrastructure by using hardware-enforced Trusted Execution Environments (TEEs) and cryptographic attestation. This post describes the full-stack architecture needed to integrate the zero-trust foundation into AI factories.
On-premise requirements often limit enterprises to building their own models or using open source models for agentic AI workloads. To deliver on the promise of AI, organizations must deploy a diverse range of models—including proprietary models—on infrastructure they operate without exposing sensitive data or model weights to administrators, hypervisors, or host operating systems. On the other hand, model providers require cryptographic guarantees that their IP can’t be extracted, even when deployed outside their own controlled environments.
Confidential computing provides that assurance by addressing the trust dilemma, which requires implicit trust from each persona without actual verification of trust.
The AI factory trust dilemma
The deployment of proprietary frontier models on shared infrastructure creates a three-way trust dilemma among key stakeholders in an AI factory:
- Model owners vs. infrastructure providers: Model owners need to protect their proprietary IP (model weights, algorithmic logic) and can’t trust that the host OS, hypervisor, or root administrator won’t inspect, steal, or extract their model.
- Infrastructure providers vs. model owners/tenants: Infrastructure providers (those running the hardware and Kubernetes cluster) can’t trust that a model owner or tenant’s workload is benign. It may contain malicious code, attempt privilege escalation, or breach host security boundaries.
- Tenants (data owners) vs. model owners and infrastructure providers: Data owners must ensure their sensitive, regulated data remains confidential. They can’t trust that the infrastructure provider won’t view data during execution, or that the model provider won’t misuse or leak the data during inference.
This circular lack of trust stems from the fundamental issue that in traditional computing environments, data isn’t encrypted. This leaves sensitive data and proprietary models exposed in plaintext to the memory and system administrators. Confidential computing solves this by ensuring that data and models remain cryptographically protected throughout the entire lifecycle of execution.
Enabling secure AI factories with Confidential Containers
Confidential computing provides the hardware foundation. Confidential Containers (CoCo) operationalize it for Kubernetes.
CoCo enables Kubernetes pods to run inside hardware-backed TEEs without requiring application rewrites. Instead of sharing the host kernel, each pod is transparently wrapped in a lightweight, hardware-isolated virtual machine (VM) using Kata Containers—preserving cloud-native workflows while enforcing strong isolation boundaries.
For model providers, the biggest risk is the theft of proprietary model weights by the infrastructure owner. CoCo addresses this by removing the host operating system and hypervisor from the trust equation. When a model is deployed, it remains encrypted until the hardware mathematically proves the enclave is secure through a process called remote attestation. Only then does a Key Broker Service (KBS) release the decryption key into the protected memory, ensuring the model is never exposed in plaintext to the host.
Open reference architecture for a zero-trust AI factory
NVIDIA offers a reference architecture for the CoCo software stack. This is a standardized blueprint—developed with components from open source projects such as Kata Containers in collaboration with the Confidential Containers community—for building zero-trust AI factories on bare-metal infrastructure. It defines how to combine hardware and software to securely deploy frontier models without exposing their data or weights to the host environment.
The core pillars of this architecture are:
- Hardware root of trust: Using CPU TEEs paired with NVIDIA confidential GPUs (like NVIDIA Hopper or NVIDIA Blackwell) for hardware-accelerated, memory-encrypted AI workloads.
- Kata Containers runtime: Wrapping standard Kubernetes Pods in lightweight, hardware-isolated Utility VMs (UVMs) instead of sharing the host kernel.
- Hardened micro-quest environment: Using a distro-less, minimal guest OS featuring a chiselled root filesystem and the NVIDIA Runtime Container (NVRC) for a secure init system reduces the attack surface inside the VM.
- Attestation service: Verifying the hardware through cryptographic evidence before releasing sensitive model decryption keys or secrets to the guest. This requires a remote attestation framework, which should include a KBS.
- Confidential workload lifecycle: Facilitating secure pull of encrypted and signed images (containers, models, artifacts) directly into encrypted TEE memory, preventing exposure at rest or in transit. And enabling fine-grained policies to secure the interface between the guest and untrusted infrastructure layers.
- Native Kubernetes and GPU operator integration: Manage this stack using standard Kubernetes primitives and the NVIDIA GPU Operator, for a “lift-and-shift” deployment without rewriting the deployment manifests or the AI applications.
Threat model and trust boundaries
CoCo operates under a strict threat model. The infrastructure layer—including the host operating system, hypervisor, and cloud provider—is treated as untrusted.
Instead of relying on infrastructure administrators to enforce security controls, CoCo shifts the trust boundary to hardware-backed TEEs. AI workloads run inside encrypted virtualized environments where memory contents can’t be inspected by the host, and secrets are released only after the execution environment proves its integrity. It’s important to understand what is protected and what isn’t protected.
What CoCo protects
CoCo provides strong guarantees for confidentiality and integrity during execution, including the following:
- Data and model protection: Memory encryption prevents the host from accessing sensitive data, model weights, or inference payloads while the workload is running.
- Execution integrity: Remote attestation verifies that the workload is running inside a trusted environment with expected software measurements before secrets or model decryption keys are released.
- Secure image and storage handling: Container images are pulled and unpacked inside the encrypted guest environment, ensuring the host infrastructure can’t inspect or tamper with application code or model artifacts.
- Protection from host-level access: Privileged host actions such as memory inspection, disk scraping, or administrative debugging tools can’t expose workload contents.
What CoCo doesn’t protect
Certain risks remain outside the scope of the architecture, such as:
- Application vulnerabilities: Confidential execution ensures verified software runs inside the enclave, but it doesn’t prevent vulnerabilities within the application.
- Availability attacks: The platform guarantees confidentiality and integrity, but an infrastructure operator can disrupt workloads by refusing to schedule or terminating them.
- Non-hardware enclaves: The model relies on hardware-backed TEEs. It doesn’t apply to software-based isolation mechanisms.
- Network and storage security: Network connectivity between applications isn’t covered by the CoCo trust boundary. Applications must establish their own secure channels to prevent exposure of data in transit and use proper, confidential storage mechanisms.
Secure model deployment with composite attestation
This end-to-end workflow is based on the Remote Attestation Procedures (RATS) architecture, enabling secure key release to deploy encrypted models within the TEE:
- Initiation: When the workload needs a secret (like a model decryption key), the Attestation Agent (AA) inside the Kata VM starts an authentication handshake with the external KBS.
- Evidence collection: The AA gathers cryptographic hardware evidence (e.g., CPU quotes or NVIDIA GPU reports) from the TEE and sends it to the KBS.
- Delegated verification: The KBS forwards this evidence to the Attestation Service (AS).
- Validation: The AS evaluates the evidence against security policies and “known-good” measurements provided by the Reference Value Provider Service (RVPS). For specialized hardware, the AS acts as a proxy and delegates validation to external vendor services like NVIDIA Remote Attestation Service (NRAS) or Intel Trust Authority.
- Token issuance: If the environment mathematically proves it’s secure and untampered, the KBS returns an attestation result token and a session ID to the guest’s AA.
- Secure Key Release: The AA uses this token to request the specific secret. The KBS retrieves the secret from its backend (like a key management service) and securely delivers it to the Confidential Data Hub (CDH) inside the guest VM.
- Execution: The CDH exposes the plaintext secret directly to your AI container, allowing the model to be decrypted exclusively inside the protected memory.
Ecosystem partners
NVIDIA ecosystem partners are making zero-trust AI factories a reality, including Red Hat, Intel, Anjuna Security, Fortanix, Edgeless Systems, OPAQUE Systems, Equity Labs, Sovereign AI, Converge.ai, Dell, HPE, Lenovo, Cisco, and Supermicro to advance a production-ready confidential computing and enable enterprises to unlock the value of AI.
Get started
Learn more by referring to the NVIDIA Confidential Computing Reference Architecture.
