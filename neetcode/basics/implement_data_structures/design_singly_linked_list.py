"""
Design Singly Linked List
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
"""
from typing import List


class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next = node


class LinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        node = self.head
        for i in range(index):
            node = node.next
        return node.value

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        head = self.head
        while head.next:
            head = head.next
        head.next = node

    def remove(self, index: int) -> bool:
        if index == 0 and self.head.next:
            self.head = self.head.next
            return True
        curr = self.head
        prev = None
        for i in range(index):
            if curr.next:
                pass

    def getValues(self) -> List[int]:
        res = []
        node = self.head
        while node:
            res.append(node.value)
            node = node.next
