from constructor import LinkedList, Node


def find_kth_from_end(linked_list: LinkedList, k: int) -> Node or None:
    fast = linked_list.head
    slow = linked_list.head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 5
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4
