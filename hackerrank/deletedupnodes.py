#!/bin/python3

from curses import noqiflush
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
# Complete the 'removeDuplicates' function below.
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


def removeDuplicates(llist):

    if llist is None:
        return None

    new_llist = SinglyLinkedList()
    current, prev = llist, 0

    while current is not None:

        if current.data != prev:
            new_llist.insert_node(current.data)
            prev = current.data

        current = current.next

    return new_llist.head


if __name__ == '__main__':

    t = 1
    n = 5

    v = [1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10]

    for t_itr in range(t):
        llist_count = len(v)
        llist = SinglyLinkedList()
        for i in range(llist_count):
            llist.insert_node(v[i])
        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', sys.stdout)
        print('\n')
