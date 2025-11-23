#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    res = arr
    ans = []
    for i in range(n - 1):
        while i > -1 and (res[i] > res[i + 1]):
            temp = res[i + 1]
            res[i + 1] = res[i]
            ans.append(' '.join(map(str, res)))
            res[i] = temp
            i -= 1
    ans.append(' '.join(map(str, res)))
    return ('\n'.join(map(str, ans)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(insertionSort1(n, arr))
