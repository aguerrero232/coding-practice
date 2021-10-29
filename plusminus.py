#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
    l = len(arr)
    c1 = len(list(filter( lambda x: x > 0, arr)))/l
    c2 = len(list(filter( lambda x: x < 0, arr)))/l
    c3 = len(list(filter( lambda x: x == 0, arr)))/l
    print(c1)
    print(c2)
    print(c3)
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

# Given an array of integers, calculate the ratios of its elements that are positive, negative, 
# and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
# though answers with absolute error of up to  are acceptable.

# Example: arr [1,1,0.-1.-1]

