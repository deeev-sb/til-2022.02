# 격자판 회문수

def solution(matrix):
    count = 0
    for i in range(7):
        start = 0
        end = 4
        for _ in range(3):
            if matrix[i][start] == matrix[i][end] and matrix[i][start+1] == matrix[i][end-1]:
                count += 1
            if matrix[start][i] == matrix[end][i] and matrix[start+1][i] == matrix[end-1][i]:
                count += 1
            start += 1
            end += 1
    return count

matrix = [list(map(int, input().split())) for _ in range(7)]
print(solution(matrix))