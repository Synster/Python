"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        def msb(n):
            res = -1
            while n > 0:
                n = n >> 1
                res += 1

            return res

        result = 0
        while m > 0 and n > 0:
            msb_m = msb(m)
            msb_n = msb(n)
            if msb_m != msb_n:
                break

            x = 1 << msb_n
            result += x

            m = m - x
            n = n - x

        return result


class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= n - 1
        return n & m


print(Solution().rangeBitwiseAnd(5, 7))
