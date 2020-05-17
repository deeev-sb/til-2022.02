# 택배왕 안홍자 (Level 3)

def go(i, sum):
	global start, result, a, check, N
	if ((i == start) and sum):
		result = max(result, sum)
		return
	for j in range(N):
		if (check[j]): continue
		if (a[i][j]):
			check[j]=1
			go(j, sum+a[i][j])
			check[j]=0

def main(N):
	global start, result
	for i in range(N):
		start = i
		go(i,0)
	return result

N = int(input())
a = [0]*N
check = [0]*N
start = 0
result = 0

for i in range(N):
	a[i] = list(map(int, input().split()))

print(main(N))
