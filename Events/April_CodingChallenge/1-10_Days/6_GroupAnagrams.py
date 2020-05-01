class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st not in dic:
                dic[sorted_st] = [st]
            else:
                dic[sorted_st].append(st)
        res = [v for v in dic.values()]
        return res
