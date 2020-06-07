import sys
sys.stdout = open('fctrl/output.txt', 'w')
sys.stdin = open('fctrl/input.txt', 'r')
     
def fact(x):
    count = 0
    div = 5
    
    while (x / div >= 1):
        
        count += int(x / div)
        div *= 5
    return count


t = int(input())

for x in range(t):
    number = int(input())
    print(fact(number))
    



    
    
    




