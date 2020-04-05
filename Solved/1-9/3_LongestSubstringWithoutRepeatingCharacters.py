class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cont = 0
        res = 0
        a = {}
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=i+1
                cont+=1
            elif a[s[i]]>=i-cont:
                if cont>res:
                    res = cont
                cont = 1 + i - a[s[i]]
                a[s[i]]=i+1
            else:
                cont+=1
                a[s[i]]=i+1
        return cont if cont>res else res

