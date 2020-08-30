# K번째 수

def solution(s,e,k,num):
    num = num[s-1:e]
    num.sort()
    return num[k-1]

case = int(input())
for i in range(case):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    print('#', i+1, ' ', solution(s,e,k,num), sep='')