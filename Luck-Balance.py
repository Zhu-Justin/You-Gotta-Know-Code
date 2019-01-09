Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers,  and :
 is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ; if she loses it, her luck balance will increase by .
 denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to  if it's unimportant.
If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.
For example,  and:
Contest		L[i]	T[i]
1		5	1
2		1	1
3		4	0
If Lena loses all of the contests, her will be . Since she is allowed to lose  important contests, and there are only  important contests. She can lose all three contests to maximize her luck at . If , she has to win at least  of the important contests. She would choose to win the lowest value important contest worth . Her final luck will be .
Function Description
Complete the luckBalance function in the editor below. It should return an integer that represents the maximum luck balance achievable.
luckBalance has the following parameter(s):
k: the number of important contests Lena can lose
contests: a 2D array of integers where each  contains two integers that represent the luck balance and importance of the  contest.
Input Format
The first line contains two space-separated integers  and , the number of preliminary contests and the maximum number of important contests Lena can lose. 
Each of the next  lines contains two space-separated integers,  and , the contest's luck balance and its importance rating.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    ans = 0
    contests.sort(reverse=True)
    for i in range(len(contests)):
        if contests[i][1] == 1 and k <= 0:
            ans += -contests[i][0]
        else:
            if contests[i][1] == 1 and k > 0:
                print(contests)
                k += -1
            ans += contests[i][0]
    return ans
         

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

