class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cont = 0
        for c in S:
            if c in J: cont+=1
        return cont
