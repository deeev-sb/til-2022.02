# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    nstr = str(n)
    nlist = sorted(nstr, reverse=True)
    nstr = ''
    for i in nlist:
        nstr += i
    answer = int(nstr)
    return answer
