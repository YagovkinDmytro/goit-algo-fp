# goit-algo-fp

1. Data structures. Sorting. Working with a singly linked list

2. Recursion. Creating a Pythagorean tree fractal using recursion

3. Trees, Dijkstra's algorithm

4. Pyramid visualization

5. Visualization of binary tree traversal

6. Greedy algorithms and dynamic programming

7. Using the Monte Carlo method

# Conclusion on the task "Monte Carlo method for calculating the probabilities of sums when rolling dice"

We performed a Monte Carlo simulation to simulate 1000 rolls of two dice. For each roll, we calculated the sum of the numbers on the dice, counted the number of occurrences of each sum, and calculated the experimental probability.

### Simulation results:

| Sum | Number of cases | Probability (%) |
| :-: | :-------------: | :-------------: |
|  2  |       26        |      2.6%       |
|  3  |       47        |      4.7%       |
|  4  |       82        |      8.2%       |
|  5  |       119       |      11.9%      |
|  6  |       130       |      13.0%      |
|  7  |       174       |      17.4%      |
|  8  |       136       |      13.6%      |
|  9  |       113       |      11.3%      |
| 10  |       82        |      8.2%       |
| 11  |       58        |      5.8%       |
| 12  |       33        |      3.3%       |

### Comparison with analytical probabilities:

Analytical probabilities are calculated as the ratio of the number of combinations that give the corresponding sum to the total number of combinations (36):

| Sum | Analytical probability (%) |
| :-: | :------------------------: |
|  2  |           2.78%            |
|  3  |           5.56%            |
|  4  |           8.33%            |
|  5  |           11.11%           |
|  6  |           13.89%           |
|  7  |           16.67%           |
|  8  |           13.89%           |
|  9  |           11.11%           |
| 10  |           8.33%            |
| 11  |           5.56%            |
| 12  |           2.78%            |

### Conclusion:

The results of the Monte Carlo method are very close to the analytical values, especially with a large number of throws (1000 attempts). The difference between the obtained and theoretical probabilities does not exceed a few percent, which indicates the correctness of the simulation implementation. With an even larger number of attempts, the discrepancy decreases even more.

Thus, the Monte Carlo method confirms its effectiveness for approximating the probabilities of events in problems with a finite space of possible outcomes.
