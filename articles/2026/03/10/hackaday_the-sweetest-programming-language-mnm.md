---
title: "The Sweetest Programming Language: MNM"
source: "Hackaday"
url: "https://hackaday.com/2026/03/09/the-sweetest-programming-language-mnm/"
published: "2026-03-10"
fetched: "2026-03-10T11:20:27.742331"
---

Admit it. If you haven’t created your own little programming language, you’ve probably at least thought about it. [Muffed] decided to create a unique — and sweet — programming language that uses M&M (or, at least, M&M-like) candies as the building block of programs.
If this sounds strange, it is because, honestly, it is. It all started when a packet of GEMS (the Cadbury’s version of M&Ms) spilled and randomly fell in the shape of an arrow. There are only six symbols corresponding to the colors in a package. You create your program by arranging the candies and creating a digital image of the result. In practice, you’ll probably use ASCII text to represent your candy layout and let the compiler render the image for you.
The main way of encoding things is by the number of colored candy pixels in a row. So three blue morsels in an opcode, while four is a different opcode. Red candies encode integer literals with one candy being zero, two being one, and so on. Blue indicates control flow, green candy handles variables and stack operations, yellow is for math, and so on.
Since building things like strings. So, sadly, the M&M program isn’t complete without a run-time data file in JSON format. The title graphic shows a Hello World program that you can run in the web page, but it doesn’t show the JSON file. That’s here:
{ "strings": ["Hello, world!"], "variables": [], "inputs": { "int": [], "str": [] } }
We don’t know of any other language where you can literally eat your mistakes. There’s something to be said for that. If you want to try it, you can just write over one of the examples on the web page. Or download from GitHub.
We have seen graphic input languages before. Plus many other weird languages.
