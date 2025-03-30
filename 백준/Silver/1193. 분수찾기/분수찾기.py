import sys
input = sys.stdin.readline

X = int(input())

n = 1
while (n * (n + 1)) // 2 < X:
    n += 1

index_in_diagonal = X - (n * (n - 1)) // 2

if n % 2 == 1:
    numerator = n - (index_in_diagonal - 1)
    denominator = index_in_diagonal
else:
    numerator = index_in_diagonal
    denominator = n - (index_in_diagonal - 1)

print(f"{numerator}/{denominator}")
