class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]

'''
Altre Soluzioni:

Sol. 1 =
return Counter(nums).most_common()[-1][0]

Sol. 2 =
return sum(set(nums))*2-sum(nums)

'''
