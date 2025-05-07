An array, , is defined as follows:
Ao=0
for , where (+)is the symbol for XOR
You will be given a left and right index l r . You must determine the XOR sum of the segment of A as .
A[l]+A[l+1]+...+A[r-1]+A[r]

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def xorSequence(l, r):
    def xor(num):
        n=num%8
        if n==0 or n==1:
            return num
        elif n==2 or n==3:
            return 2
        elif n==4 or n==5: 
            return num+2
        else:
            return 0
    return xor(l-1)^xor(r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
