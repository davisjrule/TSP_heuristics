# TSP Heuristics

After completing Data Structures and Algorithms (EECS 281) at the University of Michigan, I was inspired to experiment with visualizing several heuristics that seek to approximate a solution to the traveling salesperson problem (TSP). In this project, I used two heuristics: arbitrary insertion and 2-OPT.

## Arbitrary insertion

This method starts with an existing tour between the first three vertices in the graph. Naively, we can use 0->1->2->0. Then, for each remaining vertex in the graph (from vertex 3 and onwards), the algorithm evaluates each edge in the existing tour and chooses the best edge that adds the least distance to the current tour. 

## 2-OPT: crossing elimination

The arbitrary insertion heuristic results in a decent approximation, but often leaves a large number of crossings in the tour, which indicates that there is a better route possible. To eliminate as many of these crossings as possible using the starting tour that results from arbitrary insertion, we can use the 2-OPT algorithm. 2-OPT compares each edge with every other edge, and it evaluates whether swapping the edges results in an improvement. For example, in the scenario below, the algorithm determines that A-B and C-D is a lower cost set of edges than A-D and B-C:

<img width="330" alt="Screen Shot 2022-05-03 at 4 40 57 PM" src="https://user-images.githubusercontent.com/59371711/166562381-278e17a0-a345-4dde-abc3-3278ee9ecb5e.png">

## Example

Below is an example of the two algorithms at work. First, the arbitrary insertion heuristic runs and constructs a complete tour. Then, 2-OPT is employed to remove crossings. In this example, 2-OPT only runs once, but multiple passes through 2-OPT has the potential to rearrange more pairs of edges. In fact, one way to reach a locally optimal solution to TSP is to continue running 2-OPT until it is determined that no further optimizations can be made. However, it is not guaranteed that such an approach will result in a globally optimal solution.  

![TSP-example](https://user-images.githubusercontent.com/59371711/166559968-7f1538ec-4bc1-4ef6-b598-299261988e3d.gif)
