import sys

N = int(sys.stdin.readline())
string = set()
for i in range(N):
    str =sys.stdin.readline().strip()
    string.add(str)
    
words = []
for word in string:
    words.append([len(word), word])
    
words.sort()

for word in words:
    print(word[1])