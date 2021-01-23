# 조합구하기 (DFS)

def DFS(L, num):
    global cnt
    if L == m:
        for i in range(m):
            print(temp[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(num, n+1):
            temp[L] = i
            DFS(L+1, i+1)


if __name__=="__main__":
    n, m = map(int, input().split())
    cnt = 0
    temp = [0]*(m)
    DFS(0, 1)
    print(cnt)