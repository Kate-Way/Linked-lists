# Linked-lists
Common linked list challenges

File by file problem description:

#19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

#83. Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example: 
Input: head = [1,1,2,3,3]
Output: [1,2,3]


#141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.


#876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

#1669. Merge In Between Linked Lists
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result: Build the result list and return its head.
Example: 
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

