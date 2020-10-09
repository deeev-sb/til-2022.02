# 공주 구하기 (큐)

from collections import deque

def solution(n,k):
    q = list(range(1, n+1))
    dq = deque(q)
    while True:
        for _ in range(k-1):
            dq.append(dq.popleft())
        dq.popleft()
        if len(dq) == 1:
            return dq[0]

n, k = map(int, input().split())
print(solution(n,k))