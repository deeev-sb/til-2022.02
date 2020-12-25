# 부분집합 구하기

def DFS(x):
    if x == n + 1:
        for i in range(1, n+1):
            if state[i] == 1:
                print(i, end = ' ')
        print()
    else:
        state[x] = 1
        DFS(x+1)
        state[x] = 0
        DFS(x+1)

if __name__=="__main__":
    n = int(input())
    state = [0]*(n+1)
    DFS(1)