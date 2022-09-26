
# 876 Middle node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head:ListNode):
        if head == None:
            return None
        if head.next == None:
            return head
        hare = tort = head
        while hare.next:
            tort = tort.next
            if hare.next.next == None:
                return tort
            else:
                hare = hare.next.next
        return tort


