"""
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
"""
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m = binaryMatrix.dimensions()
        i,j = n-1,m-1
        while (i>=0 and j>=0):
            if not binaryMatrix.get(i,j): i-=1
            else: j-=1
        return -1 if j == m-1 else j+1
