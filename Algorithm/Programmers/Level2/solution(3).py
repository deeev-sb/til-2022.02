# 피보나치 수
### 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

def solution(n):
    answer = 0
    F = [0,1]
    
    if n < 2 :
        answer = F[n]
    else:
        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        answer = F[n]%1234567

    return answer
