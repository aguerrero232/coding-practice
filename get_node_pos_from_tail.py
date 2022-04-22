# %%
import os
import numpy as np


# %%
arrs = [[np.random.randint(0, 9) for _ in range(8)] for _ in range(5)]

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


def getNode(llist, positionFromTail):
    cur_position = 0
    length = 0

    cur_node = llist
    while cur_node is not None:
        length += 1
        cur_node = cur_node.next

    while llist is not None:
        if (length - cur_position) == positionFromTail:
            return llist.data
        llist = llist.next
        cur_position += 1

# %%


def driver():
    for i, arr in enumerate(arrs):
        linked_list = SinglyLinkedList()
        for _, item in enumerate(arr):
            linked_list.insert_node(item)
        position = np.random.randint(0, len(arr))
        print(f'index: {i}')
        print(f"position: {position}")
        print(f"arr: {arr}")
        result = getNode(linked_list.head, position)
        print(result)

# %%


driver()
# %%
