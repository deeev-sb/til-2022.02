# 봉우리

def solution(N, matrix):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] > matrix[i+1][j] and matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i][j+1] and matrix[i][j] > matrix[i][j-1]:
                count += 1
    return count

N = int(input())
matrix = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1, N+1):
    matrix[i][1:N+1] = list(map(int, input().split()))

print(solution(N, matrix))