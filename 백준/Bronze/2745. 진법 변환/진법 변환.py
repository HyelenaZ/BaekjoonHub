import sys
input = sys.stdin.readline

def change_to_ten(num_str, base):
    answer = 0
    
    for char in num_str:
        if 'A' <= char <= 'Z':
            val = ord(char) - ord('A') + 10
        else:
            val = int(char)
            
        answer = answer * base + val
    
    return answer

n, b = input().split()
b = int(b)

result = change_to_ten(n, b)
print(result)