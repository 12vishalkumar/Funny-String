import math
import os
import random
import re
import sys
import sys
# Complete the 'funnyString' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def funnyString(s):
    # Write your code here
    S = ''
    for i in reversed(s):
        S += i
    ar_s = []
    ar_S = []
    for i, j in zip(s, S):
        ar_s.append(ord(i))
        ar_S.append(ord(j))
    for i in range(1, len(ar_s)):
        if(abs(ar_s[i-1] - ar_s[i]) == abs(ar_S[i-1] - ar_S[i])):
            T = True
        else:
            T = False
            break
    if T:
        return 'Funny'
    else:
        return 'Not Funny'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()