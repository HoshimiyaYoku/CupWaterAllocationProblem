# CupWaterAllocationProblem

## Description

The CupWaterAllocationProblem is a program that uses BFS/IDDFS algorithms to solve the problem of equally distributing water in cups. Given the number of cups, their capacities, the current water levels in the cups, and the desired number of divisions, the program calculates the minimum number of steps required to achieve equal distribution.

Please note that the IDDFS algorithm does not guarantee the minimum number of operations, but it provides a depth-limited search for finding solutions within a specified maximum depth.

## Input Format

The input for the program is formatted as follows:

```
N
V
S
D
```

- N: The number of cups (an integer)
- V: An array of N integers representing the cup capacities
- S: An array of N integers representing the current water levels in the cups
- D: The desired number of divisions (an integer)

## Output Format

The program provides the following output:

```
Minimum number of steps required: X
State 1
State 2
...
```

- X: The minimum number of steps required to achieve equal distribution
- Each step includes the sequence of states (cup water levels) achieved during that step

## Examples

### Example 1

Input:

```
3
12 7 6
12 0 0
2
```

Output:

```
 1 歩が必要：
(12, 0, 0)
(6, 0, 6)
```

### Example 2

Input:

```
5
12 6 4 9 7
12 5 3 0 0
4
```

Output:

```
 5 歩が必要：
(12, 5, 3, 0, 0)
(5, 5, 3, 0, 7)
(5, 0, 3, 5, 7)
(5, 6, 3, 5, 1)
(5, 5, 4, 5, 1)
(5, 5, 0, 5, 5)
```

Please note that the program may encounter memory limitations for large-scale problems, as it does not include advanced pruning techniques.

