import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

products = [tuple(map(int, input().split())) for _ in range(N)]

total = sum(price * quantity for price, quantity in products)

if total == X:
    print("Yes")
else:
    print("No")