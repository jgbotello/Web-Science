# Homework 5 - Graph Partitioning

## Assignment 

This assignment will have you investigate the split of the Karate Club (Zachary, 1977), described starting on [slide 92 in the Social Networks lecture slides](https://docs.google.com/presentation/d/1G9bY32EslxRdIq7znDZoGJd3-_Ock1FeJcqN3QgQuy4/edit#slide=id.g7e0acafd7b_0_0).  You must use a Python or JavaScript library (as discussed in the [Graph Vis slides](https://docs.google.com/presentation/d/1M_c2CKSnVS9fe-1vAfV4sac6KoZ36KdknFiYBL575uw/edit?usp=sharing)) to generate the graphs required in this assignment.
 

### Q1. Color nodes based on final split

**Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A or Mr. Hi).  This should look similar to the graph on slide 92 - all edges should be present, just indicate the nodes in the eventual split by color.**

To visualize the split in the Karate Club graph, I used Zachary's Karate Club dataset from the NetworkX library. This graph represents the relationships (friendships) between members of a karate club that split into two factions after a conflict. Mr. Hi's faction and John A's faction are shown in grey and light coral, respectively.

<img src="Images/graph.jpg" height="400" alt="">


*Q: How many nodes eventually go with John and how many with Mr. Hi?*
Number of nodes in Mr. Hi: 17
Number of nodes in John A: 17

### Q2. Use the Girvan-Newman algorithm to illustrate the split

**We know the "real" result of the Karate Club split, which you've colored in Q1. Your task is to use the Girvan-Newman algorithm to show that this result of the split could have been predicted by the weighted graph of social interactions.  How well does the mathematical model represent reality?  Generously document your answer with all supporting equations, code, graphs, arguments, etc.**

**Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partioning algorithm (see [Social Networks, slides 90-99](https://docs.google.com/presentation/d/1G9bY32EslxRdIq7znDZoGJd3-_Ock1FeJcqN3QgQuy4/edit#slide=id.p98)) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph *after each iteration in your report.** 

**Note that you will have to implement the Girvan-Newman algorithm rather than relying on a built-in function, because a built-in function will automatically run the whole algorithm and you will not be able to view the intermediate graphs.  Make sure that you explain in your report what the Girvan-Newman algorithm is doing.**

In this task, I implemented the Girvan-Newman algorithm to predict the split in Zachary's Karate Club graph. 

As explained in the videos and showed in the slides, the Girvan-Newman algorithm is a graph partitioning method by progressively removing edges with the highest betweenness. Slide 90 shows the following steps:


1. Calculate betweenness of all edges

2. Remove the edge(s) with highest betweenness

3. Repeat steps 1 and 2 until graph is partitioned into as many regions as desired

Edges with high betweenness often act as "bridges" between clusters. 

I implemented the algorithm by creating a funtion in python to make the process easier. In each iteration I visualize the edges that were removed. The [code](https://github.com/jgbotello/Web-Science/blob/main/HW5-Graph%20Partitioning/code/Code.ipynb) follows these steps:

1. Load the Karate Club graph using NetworkX.

2. Compute the edge betweenness at each iteration.

3. Identify and remove edges with the highest betweenness.

4. Visualize the graph after each iteration using Matplotlib.

5. Stop the process when the graph splits into two connected components.

The images below show the graph after each iteration and the edges that were removed.

Iteration 1: Removed edge 0 - 31

<img src="Images/graph1.jpg" height="400" alt="">

Iteration 2: Removed edge 0 - 2

<img src="Images/graph2.jpg" height="400" alt="">

Iteration 3: Removed edge 0 - 8

<img src="Images/graph3.jpg" height="400" alt="">

Iteration 4: Removed edge 13 - 33

<img src="Images/graph4.jpg" height="400" alt="">

Iteration 5: Removed edge 19 - 33

<img src="Images/graph5.jpg" height="400" alt="">

Iteration 6: Removed edge 2 - 32

<img src="Images/graph6.jpg" height="400" alt="">

Iteration 7: Removed edge 1 - 30

<img src="Images/graph7.jpg" height="400" alt="">

Iteration 8: Removed edge 1 - 2

<img src="Images/graph8.jpg" height="400" alt="">

Iteration 9: Removed edge 2 - 3

<img src="Images/graph9.jpg" height="400" alt="">

Iteration 10: Removed edge 2 - 7 and edge 2 - 13. (Two because they had the same betweenness)

<img src="Images/graph10.jpg" height="400" alt="">

**Q: How many iterations did it take to split the graph?**
The Girvan-Newman algorithm split the Karate Club graph into two connected components after 10 iterations.


### Q3. Compare the actual split to the mathematical split

**Compare the connected components of the Girvan-Newman split graph (Q2) with the connected components of the actual split Karate club graph (Q1).Q: Did all of the same colored nodes end up in the same group?  If not, what is different?**


Here is the corrected version with improved grammar, consistency, and clarity:

Note that I kept the same colors as in Q1 so we can see 17 nodes for Mr. Hi and 17 nodes for John A, respectively. We can compare this with the results of the mathematical implementation shown below:

Number of nodes in Mr. Hi: 15 {0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21}

Number of nodes in John A: 19 {2, 8, 9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33}

Notice that nodes 2 and 8 originally belonged to Mr. Hi, but in the mathematical implementation, they are assigned to John A.

Overall, the algorithm demonstrates the real result of the split could have been predicted by the weighted graph of social interactions. However, there may be a minimal discrepancy.

