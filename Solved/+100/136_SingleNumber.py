class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)
        for n in seen:
            return n

'''
Another solution!
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        fun = lambda x,y: y.remove(x) if x in y else y.add(x)
        [fun(e,s) for e in nums]
        return s.pop()
'''
