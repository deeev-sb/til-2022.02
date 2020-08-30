# K번째 큰 수

def solution(N, K, num):
    result = []
    for a in range(N):
        for b in range(a+1, N):
            for c in range(b+1, N):
                result.append(num[a] + num[b] + num[c])
    result = list(set(result))
    result.sort(reverse=True)
    return result[K-1]

N, K = map(int, input().split())
num = list(map(int, input().split()))

print(solution(N, K, num))