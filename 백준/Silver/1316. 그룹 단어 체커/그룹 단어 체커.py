import sys
input = sys.stdin.readline

def is_group_word(word):
    seen = set() 
    previous_char = None 
    
    for char in word:
        if char != previous_char:
            if char in seen: 
                return False 
            seen.add(char)  
        previous_char = char
        
    return True

def main():
    N = int(input())  
    group_word_count = 0 
    
    for _ in range(N):
        word = input().strip()
        if is_group_word(word):
            group_word_count += 1
    
    print(group_word_count)

if __name__ == "__main__":
    main()