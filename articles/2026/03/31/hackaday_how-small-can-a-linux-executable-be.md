---
title: "How Small Can A Linux Executable Be?"
source: "Hackaday"
url: "https://hackaday.com/2026/03/31/how-small-can-a-linux-executable-be/"
published: "2026-03-31"
fetched: "2026-04-01T07:02:37.397669"
---

With ever increasing sizes of various programs (video games being notorious for this), the question of size optimization comes up more and more often. [Nathan Otterness] shows us how it’s done by minifying a Linux “Hello, World!” program to the extreme.
A naive attempt at a minimal hello world in C might land you somewhere about 12-15Kb, but [Nathan] can do much better. He starts by writing everything in assembly, using Linux system calls. This initial version without optimization is 383 bytes. The first major thing to go is the section headers; they are not needed to actually run the program. Now he’s down to 173 bytes. And this is without any shenanigans!
The first shenanigans are extreme code size optimizations: by selecting instructions carefully (and in a way a C compiler never would), he shaves another 16 bytes off. But the real shenanigans begin when he starts looking for spaces in the ELF header that he can clobber while the program is still accepted by Linux: now he can move his already tiny x86_64 code into these “vacant” spaces in the ELF and program headers for a final tiny ELF file weighing in at just 120 bytes.
P.S.: We know it is possible to make this smaller, but leave this as an exercise to the viewer.
