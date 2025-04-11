import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if a + b <= c or b + c <= a or c + a <= b:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
