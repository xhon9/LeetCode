class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        return self.isHappyAux(n,seen)
    def isHappyAux(self, n: int, seen: set) -> bool:
        if n in seen:
            return False
        seen[n]=n
        sum=0
        while n>0:
            sum+= (n%10)**2
            n //= 10
        if sum==1:
            return True
        return self.isHappyAux(sum,seen)
