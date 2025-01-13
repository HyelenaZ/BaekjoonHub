### 240114 : Soriting_Ascending
N = int(input())
number_lst = [int(input()) for _ in range(N)]
number_lst.sort()
for number in number_lst:
    print(number)
    