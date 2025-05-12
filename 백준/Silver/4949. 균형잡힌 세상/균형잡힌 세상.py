def is_balanced(sentence):
    stack = []
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

# 입력 처리
while True:
    line = input()
    if line == ".":
        break
    print(is_balanced(line))
