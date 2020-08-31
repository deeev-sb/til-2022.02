# 소수 (에라토스테네스 체)
# 배수를 False면서 소수가 아닌 수를 지워나가는 형식

def solution(N):
    count = 0
    num = [True]*(N+1)
    for i in range(2, N+1):
        if num[i] == True:
            count += 1
            for j in range(i, N+1, i):
                num[j] = False
    return count

N = int(input())
print(solution(N))