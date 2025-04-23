import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
sys.stdout.write('\n'.join(map(str, numbers)))