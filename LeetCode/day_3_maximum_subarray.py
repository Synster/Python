"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        """
        Keep two integer tracking curr_max = sum of curr_max and num[i] and max_so_far = max of curr traversed array
        max so far should give you your result on complete traversal
        """
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
