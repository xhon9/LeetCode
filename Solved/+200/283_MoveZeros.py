class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
'''
Another solution is
class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]: #from len(nums)-1 to 0 to not miss any number
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
'''
