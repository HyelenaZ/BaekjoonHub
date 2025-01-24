n = int(input())

n_lst = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

result = ['1' if t in n_lst  else '0' for t in targets]
print(' '.join(result))