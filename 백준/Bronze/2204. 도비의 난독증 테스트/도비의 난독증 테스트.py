import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
        
    min_word = None
        
    for _ in range(n):
        word = input().rstrip()
        
        if min_word is None or word.lower() < min_word.lower():
            min_word = word
               
    print(min_word)