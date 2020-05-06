class Solution:
    def firstUniqChar(self, s: str) -> int:
        cont = Counter(s)
        for i,c in enumerate(s):
            if cont[c]==1: return i
        return -1
