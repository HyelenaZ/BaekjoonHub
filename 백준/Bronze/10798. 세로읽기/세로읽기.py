words = []
for _ in range(5):
    words.append(input())

max_len = max(len(word) for word in words)

result = ''

for col in range(max_len):
    for row in range(5):
        if col < len(words[row]):
            result += words[row][col]

print(result)