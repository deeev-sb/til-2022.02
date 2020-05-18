# 구슬 수집가 (Level 2)

def solve(box,n,k):
	result = 0
	for i in range(k-1,-1, -1):
		result += (n//box[i])
		n %= box[i]
	return result

n, k = map(int, input().split())
box = [0]*k
input_box = map(int, input().split())
input_box = list(input_box)
for i in range(k):
	box[i] = input_box[i]

print(solve(box,n,k))
