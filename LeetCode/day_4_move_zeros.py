"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        count zeros and copy numbers back, fill 0 based on total 0 count
        OR
        pop(n-i-1) when you find 0 and append at last
        """
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i - c] = nums[i]
            if nums[i] == 0:
                c = c + 1

        for i in range(c):
            nums[n - i - 1] = 0


print(Solution().moveZeroes([1, 2, 0, 0, 3, 4, 5]))
