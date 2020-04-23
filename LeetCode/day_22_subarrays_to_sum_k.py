"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays
whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""
import collections


class Solution:

    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)
        sums = {}

        def get_sum(i, j):
            if (i, j) in sums:
                return sums[(i, j)]
            else:
                return sum(nums[0:j + 1]) - sum(nums[0:i])

        count = 0
        for i in range(n):
            for j in range(i, n):

                sums[(i, j)] = get_sum(i, j)
                if sums[(i, j)] == k:
                    count += 1
        return count


class Solution2:

    def subarraySum(self, nums, k: int) -> int:
        if not nums:
            return 0

        d = collections.Counter()

        d[0] = 1
        cnt = 0
        res = 0
        for n in nums:
            cnt += n
            if (cnt - k) in d:
                res += d[cnt - k]
            d[cnt] += 1

        return res


print(Solution().subarraySum([1, 2, 3], 3))
