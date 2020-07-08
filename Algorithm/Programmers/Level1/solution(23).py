# 하샤드 수

def solution(x):
    answer = True
    xstr = str(x)
    xsum = 0
    for i in xstr:
        xsum += int(i)
    if x%xsum!=0:
        answer = False
        
    return answer
