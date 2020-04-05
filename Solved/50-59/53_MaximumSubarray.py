class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur = max_sum
        for n in nums[1:]:
        	if cur <=0:
	            cur = max(n, cur)
	        else:
		        cur += n
        	if cur > max_sum:
	            max_sum = cur
        return max_sum
