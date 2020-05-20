# 학생회실에는 프린터가 한 대뿐입니다. (Level 2)

def solve(a):
	a.sort()
	result, wait = 0, 0
	for i in range(len(a)):
		result += (wait+a[i])
		wait += a[i]
	return result

n = int(input())
a = map(int, input().split())
a = list(a)

print(solve(a))
