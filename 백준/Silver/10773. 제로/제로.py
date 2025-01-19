import sys
input = sys.stdin.readline

def cal_final_sum():
    K = int(input())
    if not (1 <= K <= 100000): 
        return 0
        
    stack = []  
    
    for _ in range(K):
        num = int(input())
        if num == 0:  
            stack.pop()
        else:
            stack.append(num)
    
    return sum(stack)

print(cal_final_sum())