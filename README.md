<p align="center"> 
  <img src="gif/checkers.jpeg" alt="checkers logo" width="80px" height="80px">
</p>
<h1 align="center"> American Checkers </h1>
<h3 align="center"> CSCI 561 -  Artificial Intelligence </h3>
<h5 align="center"> Assignment 2 - <a href="https://web-app.usc.edu/soc/syllabus/20213/30079.pdf">University of Southern California</a> (Spring 2021)</h5>

<p align="center"> 
  <img src="gif/AI-checkers.gif" alt="Animated checkers game" height="535px" width="637">
</p>

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#overview"> ➤ Overview</a></li>
    <li><a href="#project-files-description"> ➤ Project Files Description</a></li>
    <li><a href="#getting-started"> ➤ Getting Started</a></li>
    <li><a href="#scenario1"> ➤ Scenario 1: Using input output files</a></li>
    <li><a href="#scenario2"> ➤ Scenario 2: Watching the game play</a></li>
    <li><a href="#references"> ➤ References</a></li>
    <li><a href="#credits"> ➤ Credits</a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  English draughts (British English) also called American checkers or straight checkers, is a form of the strategy board game checkers. It is played on an 8×8 checkerboard with 12 pieces per side.</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>

<p align="justify"> 
  In this project, the checkers AI agent needs to find the most optimal move to make given an input.txt file of the below format. 'b' and 'w' represent regular black and white coins respectively. 'B' and 'W' represent black and white coins that have become kings coins and can move front and back.
  <pre><code>GAME
BLACK
100.0
........
....W...
.....w..
....W.w.
........
w.w.W.w.
...B....
......w.</code></pre>
The AI agent needs to produce the most viable move output in the following format. If multiple jumps are possible the sequence of jumps needs to be written into the output folder. For the above example input below is one suggested move output which results in most points.
  <pre><code>J d2 f4
J f4 d6
J d6 f8</code></pre>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

<ul>
  <li><b>checkers_agent.py</b> - Reads the input.txt file and writes the best move in output.txt</li>
  <li><b>orchestration.py</b> -  Competes two programs checker_agent_smart.py against checkers_agent_dumb.py alerternatively calling the two programs and making them write and read from their respective input and output files</li>
  algorithms.</li>
</ul>

<h3>Some other supporting files</h3>
<ul>

  <li><b>input.txt</b> - Example input file</li>
  <li><b>output.txt</b> - Example output file</li>
  <li><b>board_move1.png</b> - Parses autograder test and solution files.</li>
  <li><b>input_basic.txt</b> - Full board input configuration</li>
  <li><b>input_smart.txt</b> - Input file read by the smart agent</li>
  <li><b>input_dumb.txt</b> - Input file read by the dumb agent</li>
  
  
  <li><b>output_smart.txt</b> - Output file the smart agent writes into</li>
  <li><b>output_dumb.txt</b> - Output file the dumb agent writes into</li>
  
  <li><b>testClasses.py</b> - General autograding test classes.</li>
  <li><b>test_cases/</b> - Directory containing the test cases for each scenario.</li>
  <li><b>searchTestClasses.py</b> - Project specific autograding test classes.</li>
</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GETTING STARTED -->
<h2 id="getting-started"> :book: Getting Started</h2>

<p>You are able to start the game by typing the following commands in the command line:</p>
<pre><code>$ python orchestration.py</code></pre>

<p>You can watch the gameplay by opening </p>
<pre><code>$ python pacman.py -h</code></pre>
<i>Note that all of the commands that appear in this project also appear in <code>commands.txt</code>, for easy copying and pasting.</i>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- SCENARIO1 -->
<h2 id="scenario1"> :small_orange_diamond: Scenario 1: Finding a Fixed Food Dot using Depth First Search</h2>

<p>I have implemented the depth-first search (DFS) algorithm in the depthFirstSearch function in <code>search.py</code>.</p>
<p>The Pacman will quickly find a solution via running the following commands:</p>

<pre><code>$ python pacman.py -l tinyMaze -p SearchAgent</code></pre>
<pre><code>$ python pacman.py -l mediumMaze -p SearchAgent</code></pre>
<pre><code>$ python pacman.py -l bigMaze -z .5 -p SearchAgent</code></pre>

<p align="center"> 
<img src="gif/DFS.gif" alt="Animated gif DFS Algorithm" height="282px" width="637px">
<!--height="382px" width="737px"-->
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- SCENARIO2 -->
<h2 id="scenario2"> :small_orange_diamond: Scenario 2: Finding a Fixed Food Dot using Breadth First Search</h2>

<p>I have implemented the breadth-first search (BFS) algorithm in the breadthFirstSearch function in <code>search.py</code>.</p>
<p>I wrote a graph search algorithm that avoids expanding any already visited states.</p>
<p>The Pacman will quickly find a solution via running the following commands:</p>

<pre><code>$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs</code></pre>
<pre><code>$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5</code></pre>

<p align="center"> 
<img src="gif/BFS.gif" alt="Animated gif BFS Algorithm" height="282px" width="637">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

Mohammad Amin Shamshiri

[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ma-shamshiri)
[![Twitter Badge](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ma_shamshiri)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ma-shamshiri)

Acknowledgements: Based on UC Berkeley's Pacman AI project, <a href="http://ai.berkeley.edu">http://ai.berkeley.edu</a>

