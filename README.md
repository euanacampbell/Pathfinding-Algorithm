# A Pathfinding Investigation

Investigating various pathfinding algorithms against a new approach.

## Installation

Use with Python 2.7 only.

## Usage

Run the `main.py` file. Optional paramters can be added as shown below.

- 10 = grid start size
- 12 = grid finish size
- 400 = iterations of each grid size



```bash
>> python main.py 10 12 400

Tests completed: 1500/1500 | Current map size: 12/12


Algorithms: New, Dijkstra, DFS, A*
Maps sizes: 10 -> 12
Iterations: 500
Time taken: 2.92 seconds
```

## Results
The output data can be found in the `algorithm_results.csv` file, with all the auto-generated maps on in the `maps.csv` file.

## Abstract
With software always growing in its capabilities and sophistication, we are seeing programs tackle evermore complex problems, replacing many roles that humans have been performing for decades. One such task is driving, where progression in areas including machine learning and Artificial Intelligence have seen vehicles taking to the roads under the control of only a computer. With pathfinding regarded as a crucial asset in Automatically Guided Vehicles (AVG), it is important that the mechanisms driving the vehicles are considered safe and effective for improved predictability in driving situations. Recent road incidents involving self- driving vehicles have stressed the significance of having safe and reliable computer systems where public trust needs to be gained through high performing pathfinding algorithms and vigorous tests carried out on them.


This project carried out a review on current pathfinding algorithms from literature. A new pathfinding method was designed and implemented, using self-generated weights and a wall- hugging approach. The new pathfinding algorithm has gone through a number of tests to evaluate how well it performs compared against existing algorithms. With random maps generated for test variety, simulations were run over large map sizes ranging from 10x10 to 100x100 to understand how the different approaches handled different situations.


The test results show that the new pathfinding algorithm is faster than existing methods such as A* to find a solution. A slightly longer path length is produced however.


Future works include continuing the development of the new algorithm to deal with scalability of the driving environment. 3D simulations with integrated sensors can be used to test the algorithm in a simulated autonomous vehicle driving environment.

## Project Objectives
The project aim was to implement a new pathfinding method, with the potential to be used within autonomous vehicles.

Main Objectives:
1. Implement an assortment of existing pathfinding algorithms for comparison.
2. Design and implement a new pathfinding algorithm.
3. Compare the performance of existing pathfinding methods and the newly proposed
algorithm.
4. Investigate the similarities and differences between the pathfinding algorithms. 5. Explore the impact the new algorithm could make to autonomous vehicles.
