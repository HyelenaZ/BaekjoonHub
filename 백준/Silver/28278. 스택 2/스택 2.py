import sys

input = sys.stdin.read

data = input().splitlines()

N = int(data[0])
orders = data[1:]

stack = []
output = []

for order in orders:
    cmd = order.split()
    
    if cmd[0] == "1":
        stack.append(int(cmd[1]))

    elif cmd[0] == "2":
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append("-1")
    
    elif cmd[0] == "3":
        output.append(str(len(stack)))
    
    elif cmd[0] == "4":
        output.append("1" if not stack else "0")
    
    elif cmd[0] == "5":
        output.append(str(stack[-1] if stack else -1))

sys.stdout.write("\n".join(output) + "\n")
