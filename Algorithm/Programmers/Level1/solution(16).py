# 문자열 다루기 기본

def solution(s):
    answer = True
    num = "0123456789"
    if len(s) != 4 and len(s) != 6:
        answer = False
    else :
        for i in s:
            if i not in num:
                answer = False
    return answer
