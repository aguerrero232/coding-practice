#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plus_minus(arr):
    '''gets ratio of positive, negative and zero values in array'''

    len_of_arr = len(arr)
    c_1 = len(list(filter(lambda x: x > 0, arr)))/len_of_arr
    c_2 = len(list(filter(lambda x: x < 0, arr)))/len_of_arr
    c_3 = len(list(filter(lambda x: x == 0, arr)))/len_of_arr
    print(c_1)
    print(c_2)
    print(c_3)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plus_minus(arr)

# Given an array of integers, calculate the ratios of its elements that are positive, negative,
# and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
# though answers with absolute error of up to  are acceptable.

# Example: arr [1,1,0.-1.-1]
