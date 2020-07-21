#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_ = sum(arr)
    max_ = max(arr)
    for x in arr:
        if (sum(arr)-x) > max_:
            #print(max_)
            max_ = sum(arr)-x
        if (sum(arr)-x) < min_:
            #print(min_)
            min_ = sum(arr)-x
    print(min_, max_)
    #print("max: ", max_)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
