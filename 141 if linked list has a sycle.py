# 141. Linked list cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr2 = head
        if curr == None or curr.next == None:
            return False
        while curr.next:
            curr = curr.next
            curr2 = curr2.next
            if curr2 == None or curr2.next == None:
                return False
            else:
                curr2 = curr2.next
            if curr == curr2:
                return True

