class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for dr,n in shift:
            if not dr:
                for i in range(n):
                    s = s[1:] + s[0]
            else:
                for i in range(n):
                    s = s[-1] + s[:-1]
        return s
