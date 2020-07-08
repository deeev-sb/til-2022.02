# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    count = 0
    s = s.lower()
    for i in s:
        if i == "p":
            count += 1
        elif i== "y":
            count -= 1
    if count != 0:
        answer = False

    return answer
