# 뒤집은 소수

def reverse(x): # 숫자를 뒤집는 함수
    x = str(x)
    len_X = len(x)
    result = ''
    for i in range(len_X-1, -1, -1):
        if x != '0':
            result += x[i]
    return int(result)

def isPrime(x): # 소수인지 확인하는 함수
    if x < 2: # 2보다 작은 수 제외하는 거 잊지말기!!
        return False
    if x == 2 or x==3:
        return True
    else:
        for i in range(2, x):
            if x%i == 0:
                return False
        else:
            return True

def solution(N, num):
    answer = ''
    for i in range(N):
        reverse_num = reverse(num[i])
        if isPrime(reverse_num):
            answer += str(reverse_num) + ' '
    return answer

N = int(input())
num = list(map(int, input().split()))
print(solution(N, num))