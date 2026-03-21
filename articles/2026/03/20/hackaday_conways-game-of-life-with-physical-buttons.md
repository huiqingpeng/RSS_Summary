---
title: "Conway’s Game of Life With Physical Buttons"
source: "Hackaday"
url: "https://hackaday.com/2026/03/20/conways-game-of-life-with-physical-buttons/"
published: "2026-03-20"
fetched: "2026-03-21T08:04:59.025808"
---

Conway’s Game of Life excels in its simplicity, creating a cellular automaton on a 2D grid where each cell obeys a set of very simple rules that determine whether a cell is ‘alive’ or ‘dead’. After setting an initial condition the ‘game’ then evolves naturally from there, creating an endless series of patterns as a simplified form of bacterial evolution. Of course, setting an initial state and then watching cells light up or fade away seems like a natural fit for light-up buttons. After struggling with intrusive thoughts related to such a project for a while, [Michal Zalewski] finally gave in, creating a pretty amazing looking result.
Although there is no set size for the game board, [Michal] was constrained by his budget for the selected NKK JB15LPF-JF tactile buttons, resulting in a 17×17 matrix. That’s 289 buttons, for those keeping score, which comes down to over $1,000 over at e.g. Digikey even with quantity-based pricing. Add to this the custom PCB and a Microchip AVR128DA64 squeezed in a corner of said PCB to run the whole show and it’s quite the investment.
Finishing up the PCB, driving the lights is done with a duty cycle as the matrix is scanned along with detecting inputs in a similar manner. This required the addition of MOSFETs and transistors, the details of which can be found in the downloadable project files, along with the firmware source code. In the article a video of the board in action can be watched, allowing one to admire the very pretty wooden enclosure as well.
