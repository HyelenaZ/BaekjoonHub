import sys
input = sys.stdin.readline

N = int(input().strip())

#print("long " * (N // 4) + "int")
print(" ".join(["long"] * (N // 4) + ["int"]))
