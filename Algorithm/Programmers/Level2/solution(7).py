# 기능개발

import queue
import math

def solution(progresses, speeds):
    answer = []
    finish = queue.Queue()
    
    for i in range(len(progresses)):
        temp = math.ceil((100-progresses[i])/speeds[i]) # math.ceil는 올림
        finish.put(temp)

    temp = finish.get()
    count = 1
    while(True):
        if finish.empty():
            break
        temp2 = finish.get()
        if temp >= temp2:
            count += 1
        else:
            temp = temp2
            answer.append(count)
            count = 1
    
    answer.append(count)
    
    return answer
