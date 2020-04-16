"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


class Solution:
    def singleNumber(self, nums) -> int:
        """
        subtract sum of number from 2* sum of unique numbers
        """
        total = sum(nums)
        unique_total = sum(set(nums))
        return unique_total * 2 - total


print(Solution().singleNumber([1, 1, 2, 2, 3]))
