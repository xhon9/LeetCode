class Solution:
    def checkValidString(self, s: str) -> bool:
        cont = check = 0
        for c in s:
            cont+=1 if c=='(' else -1
            check+=1 if c!=')' else -1
            if check<0: break
            cont = max(cont,0)
        return cont==0
