import sys
input = sys.stdin.readline

def convert_to_base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   
    result = []
    while N > 0:
        result.append(digits[N % B])  
        N //= B  
    return ''.join(result[::-1])

N, B = map(int, input().split())

print(convert_to_base(N, B))
