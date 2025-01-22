while True:
    a, b = map(int, input().strip().split())
    if 0<a<10 and 0<b<10:
        print(a*b)
        break    
    else:
        print("입력값 모두 0<입력값<10인 두 정수여야 함")
