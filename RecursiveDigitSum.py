#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    z = n
    s = 0
    for i in n:
        s = s + (int(i))
    s = s * k
    if s < 10:
        return s
    else:
        s = str(s)
        return superDigit(s, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
