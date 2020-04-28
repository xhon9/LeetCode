class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        cont = 0
        aux = 1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                aux+=1
                continue
            if arr[i]+1 == arr[i+1]:
                cont+=aux
            aux = 1
        return cont
