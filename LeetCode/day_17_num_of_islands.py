"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""


class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        h = len(grid)
        w = len(grid[0])
        result = 0
        visited = {}
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        stack = []

        def is_valid(u, v):
            return 0 <= u < h and 0 <= v < w

        for i in range(h):
            for j in range(w):
                if (i, j) not in visited and grid[i][j] == "1":
                    result += 1

                    stack.append([i, j])
                    visited[(i, j)] = True
                    while stack:
                        r, c = stack.pop()

                        for x, y in direction:
                            row = r + x
                            col = c + y

                            if is_valid(row, col) and (row, col) not in visited and grid[row][col] == "1":
                                stack.append([row, col])
                                visited[(row, col)] = True
        return result


print(Solution().numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
