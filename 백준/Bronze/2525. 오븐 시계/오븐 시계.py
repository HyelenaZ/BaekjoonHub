import sys
input = sys.stdin.readline

A, B = map(int, input().split()) #현재 시각
C = int(input()) # 요리 시각

total_minutes = A * 60 + B + C #총 분으로 환산

end_hour = (total_minutes // 60) % 24  # 시간 환산
end_minute = total_minutes % 60  # 분으로 환산

print(end_hour, end_minute)
