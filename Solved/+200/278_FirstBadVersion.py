# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        lim = 0
        while n-1 != lim:
            if isBadVersion((n+lim)//2): n = (n+lim)//2
            else: lim = (n+lim)//2
        return n
