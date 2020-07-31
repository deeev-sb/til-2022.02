# 올바른 괄호

def solution(s):
    answer = True
    rcount = 0
    lcount = 0
    
    for i in range(len(s)):
        if s[0] == ')':
            lcount = 0
        if s[i] == '(' and lcount <= rcount:
            rcount += 1
        elif s[i] == ')' and lcount <= rcount:
            lcount += 1
            
    if rcount != lcount:
        answer = False

    return answer
