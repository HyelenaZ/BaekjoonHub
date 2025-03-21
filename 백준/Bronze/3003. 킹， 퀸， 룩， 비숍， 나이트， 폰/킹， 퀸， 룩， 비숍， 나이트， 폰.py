import sys
input = sys.stdin.readline

correct_set = [1, 1, 2, 2, 2, 8]

current_pieces = list(map(int, input().split()))

result = [correct_set[i] - current_pieces[i] for i in range(6)]
print(" ".join(map(str, result)))
