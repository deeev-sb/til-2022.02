# K번째 약수

def solution(N, K):
    result = []
    for i in range(1, N+1):
        if N%i == 0:
            result.append(i)
    if len(result) < K:
        return -1
    return result[K-1]

N, K = map(int, input().split())
print(solution(N, K))