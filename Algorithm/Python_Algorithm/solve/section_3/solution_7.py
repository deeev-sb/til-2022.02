# 사과나무

def solution(N, matrix):
    mid = N//2
    sum_matrix = 0
    for i in range(N):
        if i <= mid:
            temp = 2*i + 1
        else:
            temp = 2*(N-i) -1
        temp_mid = temp//2
        for j in range(temp):
            if j <= temp_mid:
                sum_matrix += matrix[i][mid-j]
            else:
                sum_matrix += matrix[i][mid+(temp-j)]

    return sum_matrix

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, matrix))