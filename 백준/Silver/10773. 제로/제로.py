def cal_fin_sum():
    try: 
        K = int(input())
        if not (1<= K <= 100000):
            print("K는 1~100,000 사이의 정수")
            return 0

        stack = []
        for _ in range(K):
            num = int(input().strip())
            if num == 0 and stack:
                removed = stack.pop()
            elif num > 0:
                stack.append(num)
        return sum(stack)

    except ValueError:
        return 0

result= cal_fin_sum()
print(result)