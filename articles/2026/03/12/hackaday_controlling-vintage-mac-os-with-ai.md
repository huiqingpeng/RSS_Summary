---
title: "Controlling Vintage Mac OS With AI"
source: "Hackaday"
url: "https://hackaday.com/2026/03/12/controlling-vintage-mac-os-with-ai/"
published: "2026-03-12"
fetched: "2026-03-13T07:02:47.954290"
---

Classic Mac OS was prized for its clean, accessible GUI when it first hit the scene in the 1980s. Back then, developers hadn’t even conceived of all the weird gewgaws that would eventually be shoehorned into modern operating systems, least of all AI agents that seem to be permeating everything these days. And yet! [SeanFDZ] found a way to cram Claude or other AI agents into the vintage Mac world.
The result of [Sean]’s work is AgentBridge, a tool for interfacing modern AI agents with vintage Mac OS (7-9). AgentBridge itself runs as an application within Mac OS. It works by reading and writing text files in a shared folder which can also be accessed by Claude or whichever AI agent is in use. AgentBridge takes commands from its “inbox”, executes them via the Mac Toolbox, and then writes outputs to its “outbox” where they can be picked up and processed by the AI agent. The specifics of how the shared folder work are up to you—you can use a network share, a shared folder in an emulation environment, or just about any other setup that lets the AI agent and AgentBridge access the same folder.
It’s hard to imagine any mainstream use cases for having a fleet of AI-controlled Macintosh SE/30s. Still, that doesn’t mean we don’t find the concept hilarious. Meanwhile, have you considered the prospect of artificial intelligence running on the Commodore 64?
