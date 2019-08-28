#!/bin/python3

import math
import os
import random
import re
import sys

# This is also just testing my vim abilities
# Complete the function below.
def function(X, N):

    poss_nums = []
    
    for num in xrange(1, X):
        new = num**N
        if new > X:
            break
        poss_nums.append(new)
        
    def total_subsets_matching_sum(numbers, sum):
        array = [1] + [0] * (sum)
        for current_number in numbers:
            for num in xrange(sum - current_number, -1, -1):
                if array[num]:
                    array[num + current_number] += array[num]
        return array[sum]
    
    ans = total_subsets_matching_sum(poss_nums,X)
	return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    param1 = int(input())

    param2 = int(input())

    result = function(param1, param2)

    fptr.write(str(result) + '\n')

    fptr.close()
