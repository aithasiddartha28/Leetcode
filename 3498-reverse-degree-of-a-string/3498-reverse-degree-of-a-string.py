class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for index, i in enumerate(s, 1):
            position = ord(i) - ord('a') + 1
            rev = 27 - position
            res += rev * index
        return res