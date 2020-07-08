# 이상한 문자 만들기

def solution(s):
    answer = ''
    slist = s.split(' ')
    for word in slist:
        for i in range(len(word)):
            if i%2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    answer = answer[:-1]
    return answer
