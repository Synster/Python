class Solution:
    def canJump(self, nums) -> bool:
        index = len(nums) - 1
        max_jump = 0
        for i, n in enumerate(nums[:index]):
            max_jump = max(max_jump, i + n)
            if max_jump >= index:
                return True
        return False


print(Solution().canJump([3, 2, 1, 0, 4]))
