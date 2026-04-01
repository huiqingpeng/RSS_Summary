---
title: "WheatForce: Learning From CPU Architecture Mistakes"
source: "Hackaday"
url: "https://hackaday.com/2026/04/01/wheatforce-learning-from-cpu-architecture-mistakes/"
published: "2026-04-01"
fetched: "2026-04-02T07:07:46.462263"
---

Nothing ever made is truly perfect and indeed, CPU architectures like x86, RISC-V, ARM, and PowerPC all have their own upsides and downsides. Today, I aim to make an architecture that learns from all these mistakes and improves architecture design for everyone.
I’ve consulted with many people opinionated on the matter, both from a software perspective, and from a hardware perspective. I have taken all their feedback in mind while creating this initial draft of the WheatForce architecture (PDF). It is inspired by pieces from many architectures: segmentation inspired by x86, hash table-like paging from PowerPC, dynamic endianness control from RISC-V and PowerPC, and more. Let’s look into each feature in a little bit more detail.
Segmentation
Segmentation is a powerful virtual-memory feature that is tragically underused today. I believe this is due to limited flexibility, so I have added an improvement above the model that x86 had used: every single register can now use its own segment selector. With this added flexibility, one can surely make better use of the address translation powers of segmentation with minimal extra overhead.
Hash Table-Like Paging
PowerPC’s hash table-like paging makes its paging vastly superior to the likes of x86, RISC-V and ARM by decreasing the number of required cache line fetches drastically. Much like a true hash table, the keys (or input addresses) are hashed and then used as an index into the table. From there, that row of the table is searched for a cell with a matching virtual address, which can be accelerated greatly due to superior cache locality of the entries in this row.
Dynamic Endianness Control
RISC-V and PowerPC both have some real potential for better compatibility with their dynamic endianness control. However, both these architectures can only change the endiannes from a privileged context. To make this more flexible, WheatForce can change the data endianness at any time with a simple instruction. Now, user software can directly interoperate between big-endian and little-endian data structures, eliminating the need for a costly byte-swap sequence that would need many instructions. Finally, you can have your cake and eat it to!
Conclusion
WheatForce has observed the mistakes of all architectures before it, and integrates parts of all its predecessors. You can read the full specification on GitHub. After you’ve read it, do let me know what you think of it.
