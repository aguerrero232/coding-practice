#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n, step):
    s = ''
    if n == 0:
        return
    s += ' ' * step
    s += '#' * n
    staircase( n-1, step+1 )  
    print(s)    
    

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n, 0)

# Staircase detail

# This is a staircase of size : n = 4

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# * int n: an integer