# 프린터

import queue

def solution(priorities, location):
    answer = 0
    p_que = queue.Queue()
    
    for i in range(len(priorities)):
        p_que.put(priorities[i])
    
    priorities = sorted(priorities, reverse=True)
    tmep = 0
    
    while(True):
        temp = p_que.get()
        if location == -1:
            location = len(priorities) -1
        if temp == priorities[0]:
            answer += 1
            location -= 1
            priorities = priorities[1:]
            if location == -1:
                break
        else :
            location -= 1
            p_que.put(temp)
        
    
    return answer