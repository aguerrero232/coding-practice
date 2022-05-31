#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
import collections

#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort()

    # mid = len(arr) // 2

    stepper = len(arr) - 1
    a_sum = sum(arr[stepper:])
    b_sum = sum(arr[:stepper])

    print(a_sum, b_sum)

    return 0


if __name__ == '__main__':

    arr = [5, 3, 2, 4, 1, 2]
    result = minimalHeaviestSetA(arr)
    print(result)
