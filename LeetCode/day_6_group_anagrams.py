"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):
        """
        use dict to form groups
        create key by sorting elements
        """
        anagrams = defaultdict(list)
        for word in strs:
            key = list(word)
            key.sort()
            anagrams[tuple(key)].append(word)

        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
