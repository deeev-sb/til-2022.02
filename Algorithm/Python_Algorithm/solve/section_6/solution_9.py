# 수열 추측하기 (순열, 파스칼 삼각형 응용)
import copy

def DFS(length):
    global temp
    if length == n:
        temp2 = copy.deepcopy(temp)
        for i in range(n-1):
            for j in range(len(temp2)-1):
                temp2[j] = temp2[j] + temp2[j+1]
                if temp2[0] > f:
                    break
            temp2 = temp2[:-1]
        if temp2[0] == f:
            for k in range(n):
                print(temp[k], end=' ')
            exit(0)
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                temp[length] = i
                DFS(length+1)
                check[i] = 0

if __name__=="__main__":
    n, f = map(int, input().split())
    check = [0]*(n+1)
    temp = [0]*n
    DFS(0)