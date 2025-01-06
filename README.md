# Fanorona with MCTS

Welcome to **Fanorona with MCTS**, a project that implements the Monte Carlo Tree Search (MCTS) algorithm for the traditional board game of [Fanorona](https://en.wikipedia.org/wiki/Fanorona).
---
![[Fanorona Board](https://fr.wikipedia.org/wiki/Fanorona#/media/Fichier:Fanorona-1.svg)
## 📖 About Fanorona
Fanorona is a centuries-old strategy board game originating from Madagascar. It is played on a 9x5 grid (fanorona 9) or a 5x5 grid (fanorona 5)  and challenges players to capture their opponent's pieces using a variety of strategic moves. The game is renowned for its depth and complexity, making it an excellent candidate for AI research.

---
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" version="1.0" width="900" height="485" id="svg1901">
  <defs id="defs1903"/>
  <g style="opacity: 1;" id="layer1">
    <path d="M 42.857143,35.219325 L 42.857143,446.6479 M 40,446.6479 L 855.71429,446.6479 M 40,40.933613 L 855.71429,40.933613 M 40,345.21933 L 855.71429,345.21933 M 40,243.79076 L 855.71429,243.79076 M 40,142.36218 L 855.71429,142.36218 M 448.57143,35.219325 L 448.57143,446.6479 M 550,35.219325 L 550,446.6479 M 347.14286,35.219325 L 347.14286,446.6479 M 245.71429,35.219325 L 245.71429,446.6479 M 651.42858,35.219325 L 651.42858,446.6479 M 752.85715,35.219325 L 752.85715,446.6479 M 854.28572,35.219325 L 854.28572,446.6479 M 42.872011,446.49006 L 448.53445,40.928195 M 448.61516,446.6479 L 854.29338,40.928195 M 42.81916,243.71053 L 245.58802,40.928195 M 651.56916,446.56767 L 854.33802,243.78534 M 245.71337,446.6479 L 651.39159,40.928195 M 144.28571,35.219325 L 144.28571,446.6479 M 854.39023,446.6479 L 448.71201,40.928195 M 448.6313,446.6479 L 42.95308,40.928195 M 854.4273,243.71053 L 651.65844,40.928195 M 245.6773,446.56767 L 42.90844,243.78534 M 651.53309,446.6479 L 245.85487,40.928195" style="overflow: visible; marker: none; color: rgb(0, 0, 0); fill: none; fill-opacity: 1; fill-rule: nonzero; stroke: rgb(0, 0, 0); stroke-width: 3; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1; visibility: visible; display: inline;" id="path6583"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(507.143)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6531"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(608.571)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6541"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(710)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6551"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(811.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6561"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(811.429, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6563"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(811.429, 202.857)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6565"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(811.429, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6567"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(811.429, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6569"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(0, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6489"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(101.429, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6499"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(202.857, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6509"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(304.286, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6519"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(405.714, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6529"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(507.143, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6539"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(608.571, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6549"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(710, 405.714)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6559"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6491"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(202.857)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6501"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(304.286)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6511"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(405.714)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6521"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(0, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6483"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(0, 202.857)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6485"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(0, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6487"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(101.429, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6493"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(202.857, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6503"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(304.286, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6513"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(304.286, 202.857)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6515"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(202.857, 202.857)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6505"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(101.429, 202.857)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6495"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(101.429, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6497"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(202.857, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6507"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(304.286, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6517"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(405.714, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6527"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(507.143, 202.857)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6535"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(507.143, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6533"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(405.714, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6523"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(507.143, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6537"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(608.571, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6547"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(608.571, 202.857)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6545"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(608.571, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6543"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(710, 101.429)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6553"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(710, 202.857)" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6555"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" transform="translate(710, 304.286)" style="fill: rgb(255, 255, 255); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="use6557"/>
    <path d="M 65.714287 40.933613 A 22.857143 22.857143 0 1 1  20,40.933613 A 22.857143 22.857143 0 1 1  65.714287 40.933613 z" style="opacity: 1; fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 5; stroke-linecap: round; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="path6209"/>
  </g>
</svg>


## 🎯 Project
- Implement a simple interface for 
- Implement the **Monte Carlo Tree Search (MCTS)** algorithm to play Fanorona.
- Develop an AI capable of making intelligent, adaptive decisions.

---

## 🚀 Features
- **Fanorona Game Logic**: The game board is represented programmatically, supporting all valid moves and captures.
- **MCTS Algorithm**: To calculate optimal moves.

- **Interactive Gameplay**: Play against the AI (simulate AI vs. AI matches)

---

## 🛠️ Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Fanorona-MCTS.git
   cd Fanorona-MCTS
   ```
2. Run the game
```bash
python main.py
```

---

## 🛠️ To do

---

## 📂 Repository Structure
```
Fanorona-MCTS/
├── docs/                 # Documentation files
├── src/                  # Source code
│   ├── board.py          # Fanorona board and rules
│   ├── mcts.py           # MCTS implementation
│   └── main.py           # Entry point for the game
├── tests/                # Unit tests
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🌟 Acknowledgments
- Inspired by the board game [Fanorona](https://en.wikipedia.org/wiki/Fanorona))  
- Thanks to [maksimKorzh](https://github.com/maksimKorzh/) for the help on the MCTS part.

Enjoy playing and exploring the strategies of Fanorona with AI!

