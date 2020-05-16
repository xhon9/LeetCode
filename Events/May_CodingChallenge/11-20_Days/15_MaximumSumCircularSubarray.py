class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A: return 0
        cur_max = cur_min = maX = miN = suM = A[0]
        for i in range(1, len(A)):
            cur_max = max(A[i], cur_max + A[i]); maX = max(maX, cur_max)
            cur_min = min(A[i], cur_min + A[i]); miN = min(miN, cur_min)
            suM += A[i]
        if(suM == cur_min):
            return maX
        return max(suM - miN, maX);
