# 시저 암호

def solution(s, n):
    answer = ''
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i == ' ': # 공백일 때
            answer += ' '
        elif i in upper:# 대문자일 때
            for j in range(len(upper)):
                if i == upper[j]:
                    if j+n < len(upper):
                        answer += upper[j+n]
                    else :
                        answer += upper[j+n-len(upper)]
        else : # 소문자일 때
            for j in range(len(lower)):
                if i == lower[j]:
                    if j+n < len(lower):
                        answer += lower[j+n]
                    else:
                        answer += lower[j+n-len(lower)]
    return answer
