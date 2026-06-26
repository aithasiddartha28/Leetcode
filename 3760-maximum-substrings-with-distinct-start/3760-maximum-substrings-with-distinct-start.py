class Solution:
    def maxDistinct(self, s: str) -> int:
        a=set(str(s))
        return len(a)