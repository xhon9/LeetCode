class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            m1 = stones[len(stones)-1]
            m2 = stones[len(stones)-2]
            if m1==m2:
                stones.pop()
                stones.pop()
            else:
                stones.pop()
                stones.pop()
                stones.append(m1-m2)
                stones.sort()
        if stones:
            return stones[0]
        return 0
