class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def length(self):
        if self.head == None:
            return
        curr = self.head
        total = 0
        while curr.next:
            total += 1
            curr = curr.next
        return total

    def get(self, index: int) -> int:
        if self.head == None:
            return - 1
        if index > self.length():
            return - 1
        count = 0
        curr = self.head
        while count != index:
            curr = curr.next
            count += 1
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
        if self.length() == None:
            return
        if index > self.length():
            self.addAtTail(val)
            return
        count = 0
        curr = self.head
        while (count+1) != index:
            curr = curr.next
            count += 1
        new_node = Node(val)
        next = curr.next
        curr.next = new_node
        new_node.next = next

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            return
        for i in range(index - 1):
            temp = temp.next
        if temp is None or temp.next is None:
            return
        next = temp.next.next
        temp.next = next


    def display(self):
        elems = []
        curr = self.head
        if curr == None:
            print(elems)
            return
        elems.append(curr.val)
        while curr.next:
            curr = curr.next
            elems.append(curr.val)
        print(elems)

