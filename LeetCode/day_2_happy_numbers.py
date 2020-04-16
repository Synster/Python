"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Keep track of the resulting number break if you reach 1 or you revisit a resulting number
        """
        visited = []
        while n > 1 and n not in visited:
            visited.append(n)
            num = n
            total = 0
            while num > 0:
                total += pow(num % 10, 2)
                num = int(num / 10)
            n = total
        return n == 1


print(Solution().isHappy(19))
