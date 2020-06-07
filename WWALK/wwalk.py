import sys
sys.stdout = open('WWALK/output.txt', 'w')
sys.stdin = open('WWALK/input.txt', 'r')


for i in range(int(input())):
    t = int(input())
    Alice = list(map(int, input().split()))
    Bob = list(map(int, input().split()))

    sum = 0; distance_Alice = 0; distance_bob = 0

    for i in range(t):
        distance_Alice += Alice[i]
        distance_bob += Bob[i]

        if Alice[i] == Bob[i] and distance_Alice == distance_bob:
            sum += Alice[i] # sum += Alice[i] == sum += Bob[i] ... Same result
    print(sum)


''' *** Goes on top ***
import atexit
import io
import sys
import math
from collections import defaultdict,Counter

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
'''

    