# %%
import numpy as np


# %%
arr = [np.random.randint(0, 9) for _ in range(6)]
arr2 = [np.random.randint(0, 9) for _ in range(6)]
arr.sort()
arr2.sort()
# %%


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# %%


def merge_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    merge_ll = SinglyLinkedList()

    while head1.next is not None and head2.next is not None:
        if head1.data < head2.data:
            merge_ll.insert_node(head1.data)
            head1 = head1.next
        else:
            merge_ll.insert_node(head2.data)
            head2 = head2.next
    if head1.next is None:
        while head2.next is not None:
            merge_ll.insert_node(head2.data)
            head2 = head2.next

    if head2.next is None:
        while head1.next is not None:
            merge_ll.insert_node(head1.data)
            head1 = head1.next

    return merge_ll.head


def better_merge_list(head1, head2):
    """
        description: merge two sorted linked lists
        @param head1: first linked list
        @param head2: second linked list
        @return: merged linked list
    """
    list1, list2 = [], []
    while head1 is not None:
        list1.append(head1.data)
        head1 = head1.next
    while head2 is not None:
        list2.append(head2.data)
        head2 = head2.next
    mergelist = list1 + list2
    mergelist.sort()
    merge_ll = SinglyLinkedList()
    [merge_ll.insert_node(i) for i in mergelist]
    return merge_ll.head


# %%

def driver():

    list1 = SinglyLinkedList()

    for _, item in enumerate(arr):
        list1.insert_node(item)

    list2 = SinglyLinkedList()

    for _, item in enumerate(arr2):
        list2.insert_node(item)

    list3 = better_merge_list(list1.head, list2.head)

    while list3.next is not None:
        print(list3.data)
        list3 = list3.next


# %%
driver()

# %%
