import sys
input = sys.stdin.readline
score = int(input())
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >=70 else 'D' if score >= 60 else 'F'
print(grade)