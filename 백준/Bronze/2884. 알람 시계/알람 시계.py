import sys
input = sys.stdin.readline 

H, M = map(int, input().split())

M -= 45

if M < 0:
    M += 60  # 60분을 더해서 양수로 만들고
    H -= 1     # 한 시간 줄여줌

if H < 0:
    H = 23 

print(H, M)
