#!/bin/python3

import math
import os
import random
import re
import sys


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

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
#    # Function to reverse the linked list
#     def reverse(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev


def reverse(llist):
    # Write your code here
    if llist is None:
        return None

    # example -> 1 - 2 - 3 - None

    prev = None
    # prev = None

    cur = llist
    # cur = 1

    while cur:
        next = cur.next
        # next = 2, 3, None

        cur.next = prev
        # cur.next = None, 1, None

        prev = cur
        # prev = 1, 2, 3

        cur = next
        #  cur = 2, 3, None

    # ittr 0: prev = None, cur = 1, next = 2
    # ittr 1: prev = 1, cur = 2, next = 3
    # ittr 2: prev = 2, cur = 3, next = None
    # ittr 3: prev = 3, cur = None, next = None

    return prev


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
