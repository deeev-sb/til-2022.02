# 랜선자르기 (결정알고리즘)

def solution(N, lines):
    lt, rt = 0, max(lines)
    answer = 0
    while lt<=rt:
        m = (lt+rt)//2
        cnt = 0
        for i in lines:
            cnt += i//m
        if cnt >= N:
            answer = m
            lt = m + 1
        else:
            rt = m - 1

    return answer

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
print(solution(N, lines))