# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2
        head, carry = l1, 0
        carry, l1.val = divmod(l1.val + l2.val + carry, 10)
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
        l1.next = self.addTwoNumbers(l1.next or l2.next, ListNode(carry) if carry else None)
        return head
