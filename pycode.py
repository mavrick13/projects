#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(list1):
    # Write your code here
    # creating a variable to store sum
    summ = 0
    # iterating over ar to add all items
    for ele in list1:
        summ += ele
    # returning the fnal sum to print
    print(summ)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # get count of number of inputs
    ar_count = int(input().strip())
# using rstrip() and split , split() get multiple values and store as a list
    list1 = list(map(int, input().rstrip().split()))
    # ar=np.array(list1)
# calling solution method
    result = simpleArraySum(list1)

    #fptr.write(str(result) + '\n')

    # fptr.close()
