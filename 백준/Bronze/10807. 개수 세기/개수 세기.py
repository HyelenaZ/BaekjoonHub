import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
v = int(input())

print(len([num for num in nums if num == v]))