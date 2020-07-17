#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_plus = 0
    count_negative = 0
    count_zero = 0
    pos_ratio = 0.0
    neg_ratio = 0.0
    zero_ratio = 0.0
    for item in arr:
        if item > 0:
            count_plus +=   1
        elif item < 0:
            count_negative +=   1
        elif item == 0:
            count_zero +=   1
    
    pos_ratio = format(float(count_plus/len(arr)),'.6f')
    neg_ratio = format(float(count_negative/len(arr)),'.6f')
    zero_ratio = format(float(count_zero/len(arr)),'.6f')
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
