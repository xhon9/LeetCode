class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judges = set([i+1 for i in range(N) ])
        trusted_person = [0] * N
        for x,y in trust:
            if x in judges: judges.remove(x)
            trusted_person[y-1] += 1
        if len(judges)==1:
            judge = judges.pop()
            if trusted_person[judge-1]==N-1: return judge
        return -1
