# 곳감 (모래시계)

def solution(N, matrix, M, change):
    # 곳감 이동
    for i in range(M):
        row = change[i][0] - 1
        direction = change[i][1]
        move = change[i][2]
        while True:
            if move < N:
                break
            move -= N
        temp = [0]*N
        if direction: # 1, 오른쪽
            for j in range(N):
                if j < move:
                    temp[j] = matrix[row][j+N-move]
                else:
                    temp[j] = matrix[row][j-move]
        else: # 0, 왼쪽
            for j in range(N):
                if j < (N-move):
                    temp[j] = matrix[row][j+move]
                else:
                    temp[j] = matrix[row][j+move-N]
        matrix[row] = temp

    # 모래시계 모양으로 출력
    start, end, sum_matrix = 0, N, 0
    for i in range(N):
        for j in range(start, end):
            sum_matrix += matrix[i][j]
        if i < N//2:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1
    
    return sum_matrix


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
change = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, matrix, M, change))