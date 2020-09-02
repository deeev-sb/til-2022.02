# 격자판 최대합

def solution(N, matrix):
    max_sum = -2147000000

    # row
    for i in range(N):
        temp = sum(matrix[i])
        if max_sum < temp:
            max_sum = temp
    
    # column
    for i in range(N):
        temp = 0
        for j in range(N):
            temp += matrix[j][i]
        if max_sum < temp:
            max_sum = temp
    
    # diagonal
    temp = 0
    for i in range(N):
        temp += matrix[i][i]
    if max_sum < temp:
        max_sum = temp
     
    # diagonal 2
    temp = 0
    for i in range(N):
        temp += matrix[i][N-i-1]
    if max_sum < temp:
        max_sum = temp

    return max_sum


N = int(input())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))
print(solution(N, matrix))