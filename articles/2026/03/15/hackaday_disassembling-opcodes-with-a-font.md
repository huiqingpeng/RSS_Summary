---
title: "Disassembling Opcodes with a Font"
source: "Hackaday"
url: "https://hackaday.com/2026/03/15/disassembling-opcodes-with-a-font/"
published: "2026-03-15"
fetched: "2026-03-16T07:01:18.611538"
---

Those who stay into the forbidden realm of font rendering quickly learn how convoluted and arcane it can be – LaTeX is a fully Turing-complete programming language, Unicode has over eighty invisible characters, and there are libraries that let you execute WebAssembly in a font. A great example of a font’s hidden capabilities is Z80 Sans, a font that disassembles Z80 opcodes to assembly mnemonics.
If one pastes Z80 opcodes into a word processor and changes their font to Z80 Sans, the codes are rendered as their assembly mnemonics. The font manages this by abusing the Glyph Substitution Table and Glyph Positioning Table, two components of the OpenType standard. Fonts define relations between characters (internal representations used by the computer, such as ASCII and Unicode) and glyphs (the graphics actually displayed).
In some cases, though, the way a character is displayed depends on where it appears in a word, or what appears around it (Arabic characters are a common example, but an example from English is the ligature “æ”). Z80 Sans defines all the possible glyphs for each nibble of the opcodes, then used a recursive descent parser to generate substitution rules which display the correct glyphs in context.
For a deeper dive into the pitfalls of text graphics, check out this font rendering engine written for a hobby OS. You can also use fonts to play games or talk to an LLM.
