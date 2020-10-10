# 응급실 (큐)

from collections import deque

def solution(n,m,danger):
    # enumerate를 활용해 인덱스 번호를 가져와 튜플로 관리
    danger = [(a, b) for a, b in enumerate(danger)]
    dq = deque(danger)
    cnt = 0
    while True:
        temp = dq.popleft()
        if any(temp[1] < i[1] for i in dq):
            dq.append(temp)
        else:
            cnt += 1
            if temp[0] == m:
                break
    return cnt

n, m = map(int, input().split())
danger = list(map(int, input().split()))
print(solution(n,m,danger))