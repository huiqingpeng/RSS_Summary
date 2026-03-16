---
title: "Design, Simulate, and Scale AI Factory Infrastructure with NVIDIA DSX Air"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/design-simulate-and-scale-ai-factory-infrastructure-with-nvidia-dsx-air/"
published: "2026-03-16"
fetched: "2026-03-17T07:08:41.075362"
---

Building AI factories is complex and requires efficient integration across compute, networking, security, and storage systems. To achieve rapid Time to AI and strong ROI, the new NVIDIA DSX Air is enabling organizations to simulate their entire AI factory infrastructure in the cloud—covering compute, networking, storage, and security.
Being able to design, test, and optimize systems before deploying hardware enables every layer of the AI factory to function as a unified, optimized system, preventing major delays or performance issues related to integration or misconfiguration challenges. DSX Air also enables continuous testing and validation of provisioning, automation, and security policies to streamline ongoing operations.
This post shows how users can benefit from NVIDIA DSX Air through accelerated deployment timelines and simplified, full-stack cluster management.
How DSX Air enables AI factory simulation
To make AI factory simulation useful and practical for end users, DSX Air adds the following enhancements.
Guaranteed capacity
Subscription options provide guaranteed capacity without resource limits, enabling large-scale, long-lived simulations from pre-provisioning to decommission.
Unified account setup
Integrated with NVIDIA GPU Cloud, organizations and teams can manage access and resources through an NVIDIA Cloud Account (NCA). Users can join by signing up through the NGC portal, receiving an entitlement from NVIDIA, or being invited by an account owner. Individual organizations serve single users with access, while enterprises—activated through subscriptions such as DSX Air—support multiple users, team structures, and role-based access controls for efficient collaboration and resource sharing.
Simulation checkpoints
With checkpoints, users can save snapshots of their simulation state to pause and resume work without losing configuration changes or data. DSX Air automatically creates a checkpoint when a simulation stops, and users can view, manage, or relaunch from any saved checkpoint. Important checkpoints can be marked as favorites to prevent automatic deletion when storage limits are reached, ensuring critical simulation states are preserved. This capability streamlines iterative testing, configuration management, and operational continuity within AI infrastructure simulations.
Simulation history
The history feature provides a detailed event log that tracks events through a simulation’s lifecycle. It records key information, such as timestamps, event types, actors, and descriptions—covering actions like simulation creation, state changes, checkpoint operations, user activities, and errors. Users can filter entries by keyword to quickly pinpoint specific events, making it easier to understand system behavior and troubleshoot issues efficiently.
Ecosystem enhancements
Ecosystem partners can bring their software images into the Air platform for deep integration and interoperability with server, storage, and router OEMs, as well as ISVs focused on orchestration, security, and operations. With this, organizations can build and validate joint solutions that combine NVIDIA infrastructure with partner offerings, ensuring seamless day-one interoperability across GPUs, NVIDIA NVLink, Ethernet switches, SuperNICs, DPUs, and complementary ISV tools.
DSX Air use cases for the full lifecycle of the AI factory
By simulating complete compute fabrics built with NVIDIA Spectrum-X Ethernet and NVLink technologies, organizations can accelerate the design, validation, and deployment of AI infrastructure. This reduces integration risks and compresses deployment cycles. Teams can automate provisioning, test software-defined configurations, and evaluate change impact without physical hardware dependencies. These pre-production validations enhance AIOps efficiency and ensure system integrity throughout the deployment lifecycle.
For next-generation infrastructure, DSX Air supports simulation of NVIDIA Spectrum-6 Ethernet switches and NVLink switches for deploying AI factories built with the NVIDIA Vera Rubin platform.
CI/CD integration and DevOps enablement
Through its Python SDK and REST APIs, DSX Air supports integration with modern DevOps toolchains. This enables simulations to be instantiated programmatically within CI/CD pipelines for continuous verification of software and configuration updates. Integration with Git and artifact repositories also enables automated deployment testing, ensuring resilient software delivery, optimized resource utilization, and uninterrupted AI factory operations.
Get started
DSX Air provides a secure, on-demand environment for technical training and upskilling. The platform includes guided demos for skill-building with NVIDIA offerings like Cumulus Linux, NVIDIA Run:ai, Base, and Command Manager.
Teams can also replicate production environments through shared simulations, for experiential learning in a safe, isolated workspace. This approach reduces dependency on dedicated hardware labs while fostering operational proficiency and innovation.
Sign up for a free trial of NVIDIA DSX Air using the DSX Air User Guide. Read how the NVIDIA partner ecosystem is working together to build solutions spanning the full data center infrastructure stack.
