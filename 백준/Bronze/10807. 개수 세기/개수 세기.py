import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
v = int(input())

print(num.count(v))