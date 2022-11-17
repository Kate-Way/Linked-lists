class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        count = 0
        curr = self.head
        while curr and count != index:
            curr = curr.next
            count += 1
            if curr == None:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if self.head == None:
            return
        count = 0
        curr = self.head
        while curr and (count+1) != index:
            curr = curr.next
            count += 1
            if curr == None:
                self.addAtTail(val)
                return
        new_node = Node(val)
        next = curr.next
        curr.next = new_node
        new_node.next = next

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        curr = self.head
        if index == 0:
            self.head = curr.next
            return
        count = 0
        while curr and (count + 1) != index:
            curr = curr.next
            count += 1
        if curr == None or curr.next == None:
            return
        next = curr.next.next
        curr.next = next

# helpful function for visualization of the algorithm

#     def display(self):
#         elems = []
#         curr = self.head
#         if curr == None:
#             print(elems)
#             return
#         elems.append(curr.val)
#         while curr.next:
#             curr = curr.next
#             elems.append(curr.val)
#         print(elems)



