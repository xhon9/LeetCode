class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cont = 0
        m4x = 0
        seen = {0:-1}
        for i,n in enumerate(nums):
            if n: cont+=1
            else: cont-=1
            if cont in seen:
                m4x = max(m4x,(i-seen[cont]))
            else: seen[cont] = i
        return m4x
