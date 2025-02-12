import sys
input = sys.stdin.readline

def check_strike_ball(target_num, asked_num): 
    target_digits = [target_num//100, (target_num//10)%10, target_num%10]
    asked_digits = [asked_num//100, (asked_num//10)%10, asked_num%10]
    
    strike_count = 0 
    ball_count = 0
    
    for i in range(3):
        if target_digits[i] == asked_digits[i]:
            strike_count += 1
        elif target_digits[i] in asked_digits:
            ball_count += 1
            
    return strike_count, ball_count


possible_nums = [] 
for num in range(123, 988):

    digits = [num//100, (num//10)%10, num%10]
    if 0 in digits: 
        continue
    if len(set(digits)) != 3:  
        continue
    possible_nums.append(num)


N = int(input())
questions = []
for _ in range(N):
    question, strike, ball = map(int, input().split())
    questions.append((question, strike, ball))

answer_count = 0
for target_num in possible_nums:
    is_matched = True
    for q, real_strike, real_ball in questions:
        strike_count, ball_count = check_strike_ball(target_num, q)
        if strike_count != real_strike or ball_count != real_ball:
            is_matched = False
            break
    if is_matched:
        answer_count += 1

print(answer_count)