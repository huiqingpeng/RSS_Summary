---
title: "KiCad 10 release – Dark mode, graphical DRC rule editor, new file importers, and more"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/22/kicad-10-release-dark-mode-graphical-drc-rule-editor-new-file-importers-and-more/"
published: "2026-03-22"
fetched: "2026-03-23T07:02:25.609519"
---

KiCad 10 open-source EDA software has just been released with support for dark mode, importers for Allegro, PADS, and gEDA/Lepton PCB, and various changes to the Schematic Editor (e.g., hop-over display) and the PCB Editor, notably adding a graphical DRC rule editor.
KiCad 10 was built by hundreds of developers, translators, library contributors, and documentation submitters, who submitted 7,609 unique commits after KiCad 9 was released in February 2025. The new version also gains 952 new symbols, 1216 new footprints, and 386 new 3D models.
Some UI and usability improvements include dark mode support (Windows only), customizable toolbars, undo/redo support in dialogs, lasso/freeform selection instead of only rectangular selection, and new importers for Allegro, PADS, and gEDA/Lepton PCB.
Schematic editing gains support for variants (e.g., single project with different BoM), hop-over display, jumper support, grouping support, and pin table CSV export/import.
PCB Design adds time-domain tuning beyond just length constraints (along with Tuning Profiles), PCB Design Blocks have been added to the PCB editor (Blocks were added to the schematic editor in Kicad 9), and support for inner-layer objects in footprints allows users to add graphical shapes, keepouts, and more on inner layers. An unconstrained pin/pad and gate/unit swap feature was added to support forward and back annotation of changes between the schematic and PCB, and finally, KiCad 10 now offers a graphical DRC rule editor.
Other small changes include support for barcodes, hatched fills in graphic shapes, precise point editing for polygons, suggested fix actions for DRC errors, 3D PDF export, native rounded rectangles, and more. You’ll find more details and screenshots in the official announcement.
You can head to the Download page to install KiCad 10 on your operating system. I installed it on Ubuntu 24.04 in a similar way to what I did for KiCad 9:
|
1 2 |
sudo add-apt-repository ppa:kicad/kicad-10.0-releases sudo apt install kicad |
I quickly tried it using Olimex’ ESP32-C3-DevKit-LiPo hardware design files. I had the usual “this file was created by an older version of Kicad” warning, but apart from that, I could not see any obvious issue with the schematics…
… and the PCB layout, both of which opened normally.
As usual, there may be some breaking changes between major versions, at least until the dot versions with bug fixes are released. For instance, one user on X complain about KiCad 10 messing up with his custom symbols and footprint libraries, but I’m sure rough edges will be fixed soon enough.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
