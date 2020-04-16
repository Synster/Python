"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
"""


class Solution:
    def countElements(self, arr) -> int:
        """
        traverse list count++ if num+1 in list
        """
        count = 0
        for num in arr:
            if num + 1 in arr:
                count = count + 1

        return count


print(Solution().countElements([1, 2, 3]))
