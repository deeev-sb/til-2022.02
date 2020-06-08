# 평균 구하기

def solution(arr):
    answer = 0
    for i in arr:
        answer += int(i)
    answer = answer/len(arr)
    return answer