### 240111 : SUM_OF_2MATRIX
N, M = map(int, input().split())

matrix_A = []
for _ in range(N):
    matrix_A.append(list(map(int, input().split())))
for i in range(N):
    row_B = list(map(int, input().split()))
    
    result_row = []
    for j in range(M):
        sum_value = matrix_A[i][j] + row_B[j]
        result_row.append(sum_value)
    
    print(f'{" ".join(map(str, result_row))}')