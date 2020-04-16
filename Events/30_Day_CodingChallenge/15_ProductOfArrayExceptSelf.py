class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o = [1] * len(nums)
        prod, prodwithoutzeros, contzeros = 1, 1, 0
        for i,n in enumerate(nums):
            prod *= n
            if n: prodwithoutzeros *= n
            if not n :
                o[i] = 0
                contzeros+=1
        if contzeros>1: return [0]*len(nums)
        for i in range(len(o)):
            if not o[i]: o[i] = prodwithoutzeros
            else: o[i] = prod//nums[i]
        return o
