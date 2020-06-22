# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        min = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < min:
                min = arr[i]
        for i in range(len(arr)):
            if min != arr[i]:
                answer.append(arr[i])
    return answer