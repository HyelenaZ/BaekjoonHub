import sys
from collections import Counter
input = sys.stdin.readline

word = input().strip()

word = word.lower()
counter = Counter(word)

max_count = max(counter.values())

most_common = [char for char, count in counter.items() if count == max_count]

if len(most_common) > 1:
    print('?')
else:
    print(most_common[0].upper())
