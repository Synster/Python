"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution:
    def maximalSquare(self, matrix) -> int:
        h = len(matrix)

        if h == 0 or len(matrix[0]) == 0:
            return 0
        w = len(matrix[0])

        result = 0
        dp = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    dp[i][j] = 1

                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                    result = max(result, dp[i][j])
        return result * result
