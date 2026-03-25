---
title: "How Centralized Radar Processing on NVIDIA DRIVE Enables Safer, Smarter Level 4 Autonomy"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy/"
published: "2026-03-25"
fetched: "2026-03-26T07:04:13.126138"
---

In the current state of automotive radar, machine learning engineers can’t work with camera-equivalent raw RGB images. Instead, they work with the output of radar constant false alarm rate (CFAR), which is similar to computer vision (CV) edge detections. The communications and compute architectures haven’t kept pace with trends in AI and the needs of Level 4 autonomy, despite radar being a staple of vehicle‑level sensing for years.
The real 3D/4D “image” signal is instead processed inside the edge device. The radar outputs objects, or in some cases point clouds, which is similar to a camera outputting a classical CV Canny edge‑detection image.
Centralized radar processing on NVIDIA DRIVE changes this model: Raw analog‑to‑digital converter (ADC) data moves into a centralized compute platform. From there, a software-defined pipeline accelerated by dedicated NVIDIA Programmable Vision Accelerator (PVA) hardware handles everything from raw ADC samples to point clouds, with the GPU reserved for AI usage at any stage in the data flow. In such a paradigm, machine learning AI systems aren’t constrained to edge detections, instead they can utilize the full fidelity radar image, offering ~100x increase in available bits of information.
By removing the high-power digital signal processor/microcontroller unit (DSP/MCU) inside edge compute radar, centralized radar returns to its radiofrequency (RF) roots with a streamlined printed circuit board (PCB). This design cuts unit costs by over 30% and reduces volume by approximately 20%, achieving an ultra-slim form factor. Leveraging the superior energy efficiency of central domain controllers, overall system power consumption drops by about 20%. This innovation not only reshapes hardware design but also aligns perfectly with global green energy trends.
In this blog, we explain how centralized radar processing works on DRIVE, covering:
- Why the standard radar model limits what higher levels of autonomy, especially L4 stack, can do with radar data
- How raw ADC data is ingested and moved into DRIVE memory
- How the PVA handles radar signal processing without consuming CPU or GPU
For this analysis, NVIDIA collaborated with ChengTech, the first raw radar partner joining the DRIVE platform, to validate centralized compute radar processing on DRIVE with production‑grade hardware.
At GTC 2026 last week, NVIDIA and ChengTech demonstrated this pipeline running in real time on DRIVE AGX Thor using production ChengTech radar units.
How centralized radar processing expands radar perception
Most production automotive radars use edge processing architecture. Each sensor unit integrates its own system on chip (SoC) or field‑programmable gate array (FPGA), runs a fixed signal‑processing chain on board, and outputs a sparse point cloud to the central advanced driver assistance system electronic control unit (ADAS ECU). This keeps integration straightforward and limits the bandwidth required between sensor and compute platform.
The tradeoffs, however, are noteworthy:
- Point clouds send only peak detections, and carry ~100x less data than the raw ADC samples produced by the radar frontend. For example, the long-range radar in our configuration produces 6 MB of raw ADC per frame versus 0.064 MB as a point cloud. Centralized architectures that ingest raw or lightly processed radar can leverage more of the underlying signal statistics to provide perception gains.
- The radar duty cycle in edge processing is generally below 50% (the percentage of time the radar is transmitting), which typically means lower frame rates such as ~20 frames per second (FPS) and/or reduced power on target. That’s workable for classic ADAS triggers, but it leaves temporal resolution on the table for large, time-aware models.
- Tight memory and bandwidth constraints of an edge‑radar ECU mean it must discard intermediate frequency‑domain products such as range fast Fourier transform (range‑FFT) cubes, Doppler‑FFT cubes, and angle‑FFT maps, even though these are precisely the signal views that recent learning‑based radar models and signal‑level fusion methods would most like to access, as shown in Raw High‑Definition Radar for Multi‑Task Learning (CVPR 2022) and T‑FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals (ICCV Workshops 2023).
- The radar signal-processing pipeline is fixed on edge hardware, subject to tight thermal and compute limits. Centralized processing allows the OEM or system integrator to enable deeper networks, higher input resolution, and multi‑sensor joint models that would be impractical on a small radar SoC.
L4 stacks are increasingly adopting large models and vision-language-action (VLA) architectures that learn directly from raw sensor data rather than from post-processed outputs. These systems benefit from dense, low-level signals across all sensor modalities, the same way vision models benefit from raw camera frames rather than compressed features. For radar, that means rethinking where and how processing happens.
Centralized compute radar on NVIDIA DRIVE
Centralized radar processing addresses these limitations by relocating the signal processing chain from the sensor to the DRIVE platform. The RF front-end and antennas remain on the sensor hardware, but instead of running a fixed embedded pipeline, the units stream raw ADC samples into DRIVE DRAM over a high-bandwidth link. All stages of radar signal processing run on DRIVE’s dedicated hardware PVA, where developers control the full pipeline.
Three components make this work together:
1) Sensors configured for raw ADC output
2) A driver stack that ingests and synchronizes raw data into DRIVE memory
3) A PVA-based compute library that handles all radar DSP
Together, these pieces make radar a centrally managed, accelerator-backed modality on DRIVE, aligned with how cameras and lidar are already integrated in modern L4 architectures.
Moving raw ADC data into DRIVE memory
The first step is getting raw ADC data off the sensor and into central memory reliably and at scale. In our configuration, five sensors are deployed across the vehicle:
- One ChengTech 8T8R front radar
- Four ChengTech 4T4R corner radars
All five units are configured to output raw ADC data instead of embedded-processed point clouds. The aggregate raw data rate is approximately 540 MB/s across the array, compared to 4.8 MB/s for an equivalent point-cloud-based radar belt.
The ingestion stack handles this through platform-level radar drivers that:
- Configure sensors for raw-output modes
- Stream ADC frames into DRIVE DRAM at the required throughput
- Present radar frames through a consistent, hardware-agnostic API
- Share a hardware synchronization signal with camera capture so radar and image frames are aligned for multi-modal fusion and training
From the application’s perspective, radar data arrives as timestamped, synchronized buffers in DRIVE memory, ready for the signal processing stage.
Running radar signal processing on PVA
Once raw ADC buffers are in memory, the signal processing chain runs entirely on PVA, leaving the GPU free for downstream AI. The pipeline covers the standard stages of radar DSP:
- Range-FFT along the fast-time axis to produce a range profile per chirp
- Doppler-FFT along the slow-time axis to estimate radial velocity per range bin
The PVA is designed for exactly this class of workload. Figure 3, below, illustrates the high-level architecture of PVA in DRIVE AGX Thor. At its core, the PVA engine is an advanced very long instruction word (VLIW), single instruction multiple data (SIMD) digital signal processor (DSP). It combines vector processing units (VPUs), a dedicated DMA engine, and on-chip local memory (VMEM) to deliver sustained, high-throughput FFT performance with deterministic memory access behavior.
PVA provides high performance with low power consumption and can run asynchronously alongside the CPU, GPU, and other accelerators on the DRIVE platform as part of a heterogeneous compute pipeline. In a five-radar setup, running the full radar library on PVA instead of on the GPU can significantly reduce GPU utilization and free GPU capacity for perception and planning workloads.
To support customizable pipelines, PVA Solutions offers a set of highly optimized, commonly used radar operators. This allows developers to assemble and customize pipelines without having to implement every kernel from scratch. In addition, the NVIDIA Programmable Vision Accelerator Software Development Kit (PVA SDK) is available for developers who want to build their own proprietary secret sauce.
In our configuration, the PVA processes raw data from all five radar units at 30 frames per second. All radar DSP work stays on the PVA, minimizing CPU and GPU usage and leaving those resources available for perception networks, planning modules, and other workloads. The PVA uses reserved bandwidth in the memory subsystem.
Intermediate outputs at each stage are written back to DRAM and remain accessible to the rest of the stack. This means:
- Range-Doppler cubes and angle-FFT heatmaps can be visualized or logged for analysis.
- Perception models can consume pre-point-cloud representations directly.
- Multi-radar fusion can operate at the signal level before final detection, improving noise rejection and target resolution across the sensor array.
The range‑Doppler map in Figure 4, above, exposes dense spectral structure that traditional edge‑processed radars never export. In Figure 5, below, the peaks of this range-Doppler map are extracted, angle finding is performed, producing a sparse point cloud.
Exposing radar signal data to perception and physical AI
Centralizing radar on DRIVE does more than remove per-sensor SoCs or FPGAs. It augments what is visible to the perception and AI systems running on the platform.
With intermediate radar data in DRAM, several patterns become practical:
- Recent work such as Raw High‑Definition Radar for Multi‑Task Learning (CVPR 2022) and T‑FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals (ICCV Workshops 2023) trains neural networks on raw ADC signals or range/Doppler/angle‑FFT representations instead of only on sparse point clouds, enabling richer radar perception.
- Designing early fusion models that combine radar and camera features using synchronized, raw or pre-point-cloud data.
- Implementing coherent fusion across multiple radar units at the signal level to improve coverage, suppress interference, and handle adverse conditions.
For L4 stacks that already treat cameras and lidar as first-class raw modalities, centralized radar closes the gap. Radar can participate in VLA-style training workflows and other large-model approaches at the same level of data fidelity as other sensors, using the same centralized, software-defined infrastructure that DRIVE already provides.
Centralized compute radar as the future of L4 perception
Centralized radar processing on DRIVE exists to fix a simple limitation: today’s standard radars give L4 stacks a sparse, scattered view of a much richer signal. By pulling radar into DRIVE as a software-defined, accelerator-backed modality, you get the full radar signal in DRAM, processed on dedicated hardware instead of the GPU, and aligned with cameras and lidar for models to learn from.
Built on this compute and software foundation, NVIDIA DRIVE Hyperion reference architecture can integrate radar into the same centralized, software-defined pipeline as cameras and lidar, giving OEMs a production-oriented blueprint for centralized radar.
Getting started
To start evaluating this approach, work with your radar supplier to enable raw-output modes and collaborate with your perception team on richer radar-based models and fusion.
To move toward production, engage with supported radar vendors and other NVIDIA DRIVE ecosystem partners, and contact your NVIDIA representative for access to PVA SDK and PVA Solutions.
Acknowledgements
Thanks to Mark Vojkovich, Mehmet Umut Demircin, Michael Chen, Balaji Holur, Sean Pieper, Mladen Radovic, Nicolas Droux, Kalle Jokiniemi, Ximing Chen, Romain Ygnace, Sharon Heruti, Jagadeesh Sankaran, Zoran Nikolic, Ching Hung, Yan Yin, Qian Zhan, Dian Luo, Rengui Zhuo (ChengTech), Feng Deng (ChengTech), Mo Poorsartep, Cassie Dai, and Wonsik Han for their contributions.
