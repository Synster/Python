"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S = []
        stack_T = []
        for i in list(S):
            if i != '#':
                stack_S.append(i)
            elif stack_S:
                stack_S.pop()

        for i in list(T):
            if i != '#':
                stack_T.append(i)
            elif stack_T:
                stack_T.pop()

        return "".join(stack_S) == "".join(stack_T)


print(Solution().backspaceCompare("a#d", "b"))
