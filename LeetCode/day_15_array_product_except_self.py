"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""
import functools


class Solution:
    def productExceptSelf(self, nums):
        def product(nums):
            if not nums:
                return 1
            return functools.reduce(lambda a, b: a * b, nums)

        result = []
        l = len(nums)
        for i, n in enumerate(nums):
            if i < l - 1:
                result.append(product(nums[:i] + nums[i + 1:]))
            else:
                result.append(product(nums[:i]))

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))

print(Solution().productExceptSelf([1, 2, 3, 4]))
