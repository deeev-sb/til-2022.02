# 씨름선수(그리디)

def solution(n, p):
    p = sorted(p, key=lambda x:x[1], reverse=True)
    cnt = 1
    temp = p[0][0]
    for i in range(1, n):
        if temp < p[i][0]:
            cnt += 1
            temp = p[i][0]
    return cnt

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, p))