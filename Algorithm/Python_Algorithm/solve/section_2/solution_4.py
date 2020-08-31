# 대표값
import math # 반올림을 위해 사용

def solution(N, num):
    result = round(sum(num)/N) # round()는 반올림
    student = 0
    min = abs(result-num[0]) # abs()는 절댓값
    for i in range(1, N):
        if min > abs(result-num[i]):
            min = abs(result-num[i])
            student = i+1
        elif min == abs(result-num[i]):
            if num[student-1] < num[i]:
                min = abs(result-num[i])
                student = i+1
    return str(result)+' '+str(student)

N = int(input())
num = list(map(int, input().split()))
print(solution(N, num))