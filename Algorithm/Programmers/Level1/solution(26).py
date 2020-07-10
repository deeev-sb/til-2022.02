# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    nm_max = 0 # 최대공약수
    if n > m :
        n,m = m,n
    # 최대공약수 구하기
    for i in range(n, 0, -1):
        if n%i == 0 and m%i==0:
            nm_max = i
            break
    answer.append(nm_max)
    # 최소공배수 구하기
    if max == 1: # 최대공약수가 1이면 최소공배수는 두 수의 곱
        answer.append(n*m)
    else:
        answer.append(n*m/nm_max) # 최소공배수는 두 수의 곱/최대공약수
    return answer
