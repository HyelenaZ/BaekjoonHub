import sys

input = sys.stdin.readline

T = int(input().strip())

result = []

for i in range(1, T + 1):
    A, B = map(int, sys.stdin.readline().split())
    result.append(f"Case #{i}: {A} + {B} = {A + B}")

sys.stdout.write("\n".join(result) + "\n") 