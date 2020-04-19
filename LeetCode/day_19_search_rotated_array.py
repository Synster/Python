"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        result = -1
        while start <= end:
            mid = int((end + start)/2)

            if nums[mid] == target:
                result = mid
                break
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid - 1
        return result


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
