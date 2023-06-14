# CupWaterAllocationProblem

使用BFS/IDDFS来解决简单的杯子均分水的问题。
输入为杯子数N，N个整数的数组V表示杯子容积，N个整数的数组S表示杯子中现含有的水量，D需要均分的份数。（IDDFS：搜索层数限制max_depth）
输出为需要的最小步数和操作。（IDDFS无法保证操作次数为最小）
以下为一些简单的例子

e.g.1
输入：3
     12 7 6
     12 0 0
     2
输出：
    1 歩が必要：
    (12, 0, 0)
    (6, 0, 6)

e.g.2
输入：5
     12 6 4 9 7
     12 5 3 0 0
     4
输出：
     5 歩が必要：
    (12, 5, 3, 0, 0)
    (5, 5, 3, 0, 7)
    (5, 0, 3, 5, 7)
    (5, 6, 3, 5, 1)
    (5, 5, 4, 5, 1)
    (5, 5, 0, 5, 5)
    
请注意，这个程序并没有包含太多的剪枝，如果遇到数量庞大的问题会出现内存不够的情况。

Using BFS/IDDFS to solve the problem of equally distributing water in cups. The input consists of the number of cups N, an array V of N integers representing the cup capacities, an array S of N integers representing the current water levels in the cups, and the number of divisions D. (IDDFS: maximum depth is limited by max_depth)
The output includes the minimum number of steps required and the operations performed. (IDDFS cannot guarantee the minimum number of operations)
Here are some simple examples:

e.g.1
Input: 3
       12 7 6
       12 0 0
       2
Output:
       1 歩が必要：
       (12, 0, 0)
       (6, 0, 6)

e.g.2
Input: 5
       12 6 4 9 7
       12 5 3 0 0
       4
Output:
        5 歩が必要：
       (12, 5, 3, 0, 0)
       (5, 5, 3, 0, 7)
       (5, 0, 3, 5, 7)
       (5, 6, 3, 5, 1)
       (5, 5, 4, 5, 1)
       (5, 5, 0, 5, 5)

Please note that this program does not include extensive pruning, so it may encounter memory issues for large-scale problems.

