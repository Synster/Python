"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return 0

        h = len(grid)
        w = len(grid[0])

        def get_min_cost(i, j):
            if i - 1 < 0 and j - 1 < 0:
                return grid[i][j]
            if i - 1 < 0:
                return grid[i][j - 1] + grid[i][j]
            if j - 1 < 0:
                return grid[i - 1][j] + grid[i][j]

            return min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        for i in range(h):
            for j in range(w):
                grid[i][j] = get_min_cost(i, j)
        return grid[h - 1][w - 1]
