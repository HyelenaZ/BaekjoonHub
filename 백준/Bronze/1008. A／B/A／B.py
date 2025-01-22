while True:
    a, b = map(int, input().split())
    if 0 < a < 10 and 0 < b < 10:
        print(a/b)
        break
    else:
        print("정수를 입력하시오")