class Solution:
    def removeCoveredIntervals(self, a: List[List[int]]) -> int:
        return sum(sum(L<=l<r<=R for L,R in a)==1 for l,r in a)