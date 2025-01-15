while True:
    try:
        a, b = map(int, input().strip().split())
        if 0 < a < 10 and 0 < b < 10:
            print(a + b)
            break
        else:
            print("입력값 모두 0 초과 10미만의 두 정수")
    except ValueError:
        print("정수를 정확히 두 개 입력하세요.")
