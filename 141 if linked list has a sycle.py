# 141. Linked list cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        if tortoise == None or tortoise.next == None:
            return False
        while tortoise.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == None or hare.next == None:
                return False
            if tortoise == hare:
                return True

