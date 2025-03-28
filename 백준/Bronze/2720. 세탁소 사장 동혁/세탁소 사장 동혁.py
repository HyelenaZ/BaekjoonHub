import sys
input = sys.stdin.readline 

def money(change):
    quarter = change // 25
    change %= 25
    dime = change // 10
    change %= 10
    nickel = change // 5
    change %= 5
    penny = change // 1 
    return quarter, dime, nickel, penny

T = int(input()) 
for _ in range(T):
    change = int(input()) 
    q, d, n, p = money(change)
    print(q, d, n, p)
