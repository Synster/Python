"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        total = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == ')':
                total -= 1
            else:
                total += 1

            if total < 0:
                return False

        if total == 0:
            return True
        total = 0
        for i in range(n):
            if s[n - i - 1] == '(':
                total -= 1
            else:
                total += 1

            if total < 0:
                return False
        return True


print(Solution().checkValidString('(*)'))

print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
