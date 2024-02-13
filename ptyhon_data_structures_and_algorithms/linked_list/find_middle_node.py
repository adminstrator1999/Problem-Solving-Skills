from constructor import LinkedList as LL


class LinkedList(LL):

    def find_middle_node(self):
        middle = self.head
        last = self.head
        while last and last.next:
            middle = middle.next
            last = last.next.next
        return middle


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


print(my_linked_list.find_middle_node().value)
