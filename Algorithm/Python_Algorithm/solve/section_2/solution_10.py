# 점수계산

def solution(N, num):
    count = 0
    answer = 0
    for i in range(N):
        if num[i]==1:
            count += 1
            answer += count
        else:
            count = 0
    return answer

N = int(input())
num = list(map(int, input().split()))
print(solution(N, num))