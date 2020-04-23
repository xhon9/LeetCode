class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        seen[0] = 1
        sub_arrays, tot_num = 0, 0
        for n in nums:
            tot_num += n
            sub_arrays += seen[tot_num-k]
            seen[tot_num] += 1
        return sub_arrays
