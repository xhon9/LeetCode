# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode(0); oddHead = odds
        evens = ListNode(0); evenHead = evens
        cont = 1
        while head:
            if cont % 2 == 0:
                evens.next = head
                evens = evens.next
            else:
                odds.next = head
                odds = odds.next
            cont += 1
            head = head.next
        odds.next = None
        evens.next = None
        if odds:
            odds.next = evenHead.next
            return oddHead.next
        else:
            return evenHead.next
