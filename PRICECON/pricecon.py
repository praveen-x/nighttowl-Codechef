import sys
sys.stdout = open('PRICECON/output.txt', 'w')
sys.stdin = open('PRICECON/input.txt', 'r')

def lost_revenue():
    
    def original_sum(list):
        original_total = 0
        for num in range(0, len(list)):
            original_total += list[num]
        return original_total
    
    def limited_price_sum(num, orig):
        less_or_equal = []
        more = []
        limited_price = 0
        for items in range(len(orig)):
            
            if orig[items] <= num:
                less_or_equal.append(orig[items])
            else:
                more.append(orig[items])
        
        more = [num if x > num else x for x in more]
    
        final_limited_price_list = less_or_equal + more
        
        for num in range(0, len(final_limited_price_list)):
            limited_price += final_limited_price_list[num]
    
        return limited_price
    
    a = original_sum(original_price) - limited_price_sum(number, original_price)
    return a





#driver program

for i in range(int(input())):        
    for x in range(1):
        no_of_items, number = map(int, input().split())
        #print(m,n)
        for y in range(1):
            original_price = list(map(int,input().split()))
            print(lost_revenue())

'''
def original_sum(original_price):
    original_total = 0
    for num in range(0, len(original_price)):
        total += original_price[num]
    return original_total


def limited_price_sum(limit_on_price):
    less_or_equal = []
    more = []
    limited_price = 0
    for items in original_price:
        if original_price[items] <= limit_on_price:
            less_or_equal.append(original_price[items])
        else:
            more.append(original_price[items])
    more[:] = [(mor - limit_on_price) for mor in more]

    final_limited_price_list = less_or_equal + more

    for num in range(0, len(final_limited_price_list)):
        limited_price += final_limited_price_list[num]

    return limited_price


def lost_revenue():
    return original_sum() - limited_price_sum()

/////
   
t = int(input())
print(t)


for test_cases in range(1):
    n,p, *other = map(int,input().split())

    p = []
    
    for i in range(n):
        pr = int(input(' '))
        p.append(pr)
    print(p)

'''
'''
num = []
for i in range(int(input())):
    x,y = map(int, input().split())  

    for _ in range(x):
        numbers = list(map(int, input().split()))
        num.append(numbers)

 '''
 

    





    
    