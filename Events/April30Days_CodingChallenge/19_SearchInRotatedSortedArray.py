class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0, len(nums)-1
        while  start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                if nums[start] <= nums[mid] < target or nums[mid] < target <= nums[end]:
                    start = mid + 1
                else: end = mid -1
            elif nums[mid] > target:
                if target < nums[mid] <=nums[end] or nums[start] <= target < nums[mid]:
                    end = mid -1
                else: start = mid +1
        return -1
