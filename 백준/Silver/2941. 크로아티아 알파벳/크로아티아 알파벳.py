import sys
input = sys.stdin.readline

def count_cro_alphabets(word):
    cro_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    count = 0
    i = 0
    while i < len(word):
        if word[i:i+3] == "dz=":
            count += 1
            i += 3 
        elif word[i:i+2] in cro_alphabets:
            count += 1
            i += 2 
        else:
            count += 1
            i += 1
    return count

word = input().strip()
print(count_cro_alphabets(word))
