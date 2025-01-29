import sys
input = sys.stdin.readline

try:
    x = int(input())
    y = int(input())
    
   # 조건 검사 간소화
    if -1000<=x<=1000 and x!=0 and -1000<=y<=1000 and y!=0:
        print(1 if x>0 and y>0 else 2 if x<0 and y>0 else 4 if x>0 else 3)
    else:
        raise ValueError
except ValueError:
    print("Invalid input")