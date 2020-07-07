# 같은 숫자는 싫어
# 정확성, 효율성 모두 통과!

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer