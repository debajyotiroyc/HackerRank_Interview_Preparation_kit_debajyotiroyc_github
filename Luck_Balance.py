#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    lst = list()
    luck = 0
    contests.sort(reverse=True, key=lambda x: x[0])
    for x, y in contests:
        if y == 0:
            luck = luck + x
        elif y == 1 and k != 0:
            luck = luck + x
            k = k - 1
        else:
            luck = luck - x
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
