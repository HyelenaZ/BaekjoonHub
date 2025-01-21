import sys
input = sys.stdin.readline

n = int(input())
in_office = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        in_office.add(name)
    else:
        in_office.remove(name)

for name in sorted(in_office, reverse=True):
    print(name)