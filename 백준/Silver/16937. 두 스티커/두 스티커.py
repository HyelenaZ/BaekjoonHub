import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = []

for _ in range(N):
    R, C = map(int, input().split())
    stickers.append((R, C))

max_area = 0

for i in range(N):
    for j in range(i + 1, N):  # 같은 스티커를 두 번 쓰면 안됨
        for (r1, c1) in [(stickers[i][0], stickers[i][1]), (stickers[i][1], stickers[i][0])]:  # 회전 고려
            for (r2, c2) in [(stickers[j][0], stickers[j][1]), (stickers[j][1], stickers[j][0])]:  # 회전 고려
                
                # 첫 번째 스티커 왼쪽 위 배치, 두 번째 스티커 오른쪽에 배치
                if r1 <= H and c1 + c2 <= W and r2 <= H:
                    max_area = max(max_area, r1 * c1 + r2 * c2)
                
                # 첫 번째 스티커 왼쪽 위 배치, 두 번째 스티커 아래쪽에 배치
                if r1 + r2 <= H and max(c1, c2) <= W:
                    max_area = max(max_area, r1 * c1 + r2 * c2)

print(max_area)
