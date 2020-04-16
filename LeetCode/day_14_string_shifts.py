"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
"""


class Solution:
    def shift_left(self, s: str, n: int):
        s_arr = list(s)
        for i in range(n):
            x = s_arr.pop(0)
            s_arr.append(x)
        return "".join(s_arr)

    def shift_right(self, s: str, n: int):
        s_arr = list(s)
        for i in range(n):
            x = s_arr.pop()
            s_arr.insert(0, x)
        return "".join(s_arr)

    def stringShift(self, s: str, shift) -> str:

        for i, j in shift:
            if i:
                s = self.shift_right(s, j)
            else:
                s = self.shift_left(s, j)

        return s


print(Solution().stringShift([[0, 1], [1, 2]]))
