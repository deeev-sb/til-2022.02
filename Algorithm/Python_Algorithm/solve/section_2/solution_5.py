# 정다면체

def solution(N, M):
    answer = ''
    result = [0]*(N+M+1)
    for i in range(1,N+1):
        for j in range(1,M+1):
            result[i+j] += 1
    max_num = max(result)
    for i in range(N+M+1):
        if max_num == result[i]:
            answer += str(i) + ' '

    return answer

N, M = map(int, input().split())
print(solution(N, M))