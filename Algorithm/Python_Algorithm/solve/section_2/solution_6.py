# 자릿수의 합

def digit_sum(x):
    x = str(x)
    answer = 0
    for i in x:
        answer += int(i)
    return answer


def solution(N, num):
    max_num = digit_sum(num[0])
    answer = num[0]
    for i in range(1, N):
        temp = digit_sum(num[i])
        if max_num < temp :
            max_num = temp
            answer = num[i]
    return answer

N = int(input())
num = list(map(int, input().split()))
print(solution(N, num))