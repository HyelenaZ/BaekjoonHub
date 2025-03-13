import sys
input = sys.stdin.readline

numbers = [int(input().strip()) for _ in range(9)]

max_value = max(numbers)
max_index = numbers.index(max_value) + 1

print(max_value)
print(max_index)