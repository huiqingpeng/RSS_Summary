---
title: "Play a .WAV Instead of Typing Line After Line Into Vintage Microcomputer"
source: "Hackaday"
url: "https://hackaday.com/2026/03/28/play-a-wav-instead-of-typing-line-after-line-into-vintage-microcomputer/"
published: "2026-03-29"
fetched: "2026-03-30T07:05:34.245822"
---

[Casey Bralla] got his hands on a Rockwell AIM 65 microcomputer, a fantastic example of vintage computing from the late 70s. It sports a full QWERTY keyboard, and a twenty character wide display complemented by a small thermal printer. The keyboard is remarkably comfortable, but doing software development on a one-line, twenty-character display is just not anyone’s idea of a good time. [Casey] made his own tools to let him write programs on his main PC, and transfer them easily to the AIM 65 instead.
Moving data wasn’t as straightforward in 1978 as it is today. While the Rockwell AIM 65 is a great machine, it has no disk drive and no filesystem. Programs can be written in assembler or BASIC (which had ROM support) but getting them into running memory where they could execute is not as simple as it is on modern machines. One can type a program in by hand, but no one wants to do that twice.
Fortunately the AIM 65 had a tape interface (two, actually) and could read and store data in an audio-encoded format. Rather than typing a program by hand, one could play an audio tape instead.
This is the angle [Casey]’s tools take, in the form of two Python programs: one for encoding into audio, and one for decoding. He can write a program on his main desktop, and encode it into a .wav
file. To load the program, he sets up the AIM 65 then hits play on that same .wav
file, sending the audio to the AIM 65 and essentially automating the process of typing it in. We’ve seen people emulate vintage tape drive hardware, but the approach of simply encoding text to and from .wav
files is much more fitting in this case.
The audio encoding format Rockwell used for the AIM is very well-documented but no tools existed that [Casey] could find, so he made his own with the help of Anthropic’s Claude AI. The results were great, as Claude was able to read the documentation and, with [Casey]’s direction, generate working encoding and decoding tools that implemented the spec perfectly. It went so swimmingly he even went on to also make a two-pass assembler and source code formatter for the AIM, as well. With them, development is far friendlier.
Watch a demonstration in the video [Casey] made (embedded under the page break) that shows the encoded data being transferred at a screaming 300 baud, before being run on the AIM 65.
