# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    answer = sorted(strings)
    answer = sorted(answer, key = lambda x : x[n])
    return answer
