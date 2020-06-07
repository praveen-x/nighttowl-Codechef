import sys
sys.stdout = open('LOSTWKND/output.txt', 'w')
sys.stdin = open('LOSTWKND/input.txt', 'r')

t = int(input()) 

for x in range(t):
    mon, tue, wed, thu, fri, num = map(int, input().split())    
    max_hours = 120

    if((num * mon + num * tue + num * wed + num * thu + num * fri) <= max_hours):
        print('No')
    else:
        print('Yes')


'''   *** 1 ***
t = int(input())
while(t):
    a = input().split(' ')
    a = [int(x) for x in a]
    if sum(a[:-1])*a[5] > 120:
        print('Yes')
    else:
        print('No')
    t -= 1


    *** 2 ***
    for t in range(int(input())):
    l=list(map(int,input().split()))
    y=sum(l[:-1])*l[-1]
    if y<=120:
        print("No")
    else:
        print("Yes")
'''





