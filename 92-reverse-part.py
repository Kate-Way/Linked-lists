# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        curr = head
        pointer = 1
        before_flip = head

        while pointer < left:
            before_flip = curr
            curr = curr.next
            pointer += 1

        tail = curr
        new_head = None

        while pointer >= left and pointer <= right:
            next = curr.next
            curr.next = new_head
            new_head = curr
            curr = next
            pointer += 1

        before_flip.next = new_head
        tail.next = curr

        if left > 1:
            return head
        else:
            return new_head
