# 마구간 정하기 (결정알고리즘)

def solution(N, C, M):
    M.sort()
    lt, rt = M[0], M[-1]
    answer = 0
    cnt = 1
    horse = M[0]
    while lt<=rt:
        m = (lt+rt)//2
        for i in range(1,N):
            if (M[i] - horse) >= m:
                cnt += 1
                horse = M[i]
        if cnt < C:
            rt = m - 1
        else:
            answer = m
            lt = m + 1
        horse = M[0]
        cnt = 1

    return answer

N, C = map(int, input().split())
M = [int(input()) for _ in range(N)]
print(solution(N, C, M))