# 최대힙

import heapq

def solution(num):
    heap = []
    for n in num:
        if n == 0:
            if heap:
                print(-heapq.heappop(heap))
            else:
                print(-1)
        elif n == -1:
            break
        else:
            heapq.heappush(heap, -n)

num = []
while True:
    num.append(int(input()))
    if num[-1] == -1:
        break
solution(num)