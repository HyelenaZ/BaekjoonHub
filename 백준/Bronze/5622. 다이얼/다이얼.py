import sys
input = sys.stdin.readline

word = input().strip()

total_time = 0

for char in word:
    dial_number = (ord(char) - ord('A')) // 3 + 2
    
    if char in 'PQRS':
        dial_number = 7
    elif char in 'TUV':
        dial_number = 8
    elif char in 'WXYZ':
        dial_number = 9
    
    total_time += dial_number + 1

print(total_time)
