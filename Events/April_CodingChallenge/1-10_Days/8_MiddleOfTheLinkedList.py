# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def middleNode(self, head):
        cont = 0
        mid = head
        while head:
            if cont%2:
                mid = mid.next
            count+=1
            head = head.next
        return mid

'''
Altra soluzione:

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cont = 0
        aux = head
        while aux:
            cont+=1
            aux = aux.next
        mid = cont//2
        aux = head
        for i in range(mid):
            aux= aux.next
        return aux
'''
