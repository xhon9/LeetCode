class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if num**0.5==int(num**0.5) else False
