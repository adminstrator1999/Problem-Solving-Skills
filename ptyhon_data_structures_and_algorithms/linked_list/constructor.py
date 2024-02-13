class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.make_empty()
        return temp

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.tail = node
        node.next = self.head
        self.head = node
        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if not self.length:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        # if index < 0 or index >= self.length:
        #     return
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
