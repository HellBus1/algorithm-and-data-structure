# Knapsack problem

Website : https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

We are given N items where each item has some weight and profit (or price) associated with it. We are also given a bag (knapsack) with capacity W, [i.e., the bag can hold at most W weight in it]. The target is to put the items into the bag such that the sum of profits associated with them is the maximum possible.

<b> Note: </b> The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].

Examples :
```
Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0
```

Knapsack using recursion :
```
A simple solution is to consider all subsets of items and calculate the total weight and profit of all subsets. Consider the only subsets whoste total weight is smaller or same as W. From all such subsets, pick the subset with maximum profit.

Optimal Substructure :
To consider all subsets of items, there can be two cases for every item.
- case 1: The item is included in the optimal subset.
- case 2: The item is not included in the optimal set.
```

