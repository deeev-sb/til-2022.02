# 교육 과정 설계 (큐)

from collections import deque

def solution(need, num, plan):
    for i in range(num):
        dq = deque(need)
        for j in plan[i]:
            if j in dq:
                if j != dq.popleft():
                    print("#{}".format(i+1), "NO")
                    break
        else:
            if dq:
                print("#{}".format(i+1), "NO")
            else:
                print("#{}".format(i+1), "YES")


need = input()
num = int(input())
plan = []
for _ in range(num):
    plan.append(input())
solution(need, num, plan)