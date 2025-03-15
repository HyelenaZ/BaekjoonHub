import sys
input = sys.stdin.readline

remains= set()

for _ in range(10):
    num = int(input())
    remains.add(num % 42)  # 42로 나눈 나머지 값을 집합에 추가

print(len(remains))
