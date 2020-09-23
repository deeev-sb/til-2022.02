# 회의실 배정(그리디)

def solution(n, c):
    c = sorted(c, key = lambda x : x[1]) # 특정 자리를 기준으로 sort
    cnt = 1
    temp = c[0][1]
    for i in range(1, n):
        if temp <= c[i][0]:
            cnt += 1
            temp = c[i][1]
    return cnt

n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, c))