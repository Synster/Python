"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums) -> int:
        """

        """
        occ = {0: 0}
        total = 0
        n = len(nums)
        answer = 0
        for i in range(n):
            total += -1 if nums[i] == 0 else 1

            if total in occ:
                answer = max(answer, i + 1 - occ[total])
            else:
                occ[total] = i + 1

        return answer


print(Solution().findMaxLength([1, 0, 0]))
