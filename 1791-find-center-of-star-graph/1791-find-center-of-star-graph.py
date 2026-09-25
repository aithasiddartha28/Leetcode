class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a=set(edges[0])
        b=set(edges[1])
        common=a&b
        return list(common)[0]