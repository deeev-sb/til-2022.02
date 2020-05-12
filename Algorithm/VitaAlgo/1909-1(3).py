# 환상의 조합 (Level 2)

import sys

def solve(current,sum):
	global N, S, A, count
	if (current == N-1):
		if (sum == S):
			count += 1
			return 
	if (current+1 >= N):
		return
	solve(current+1, sum)
	solve(current+1, sum + A[current+1])
	return count


N, S = map(int, input().split()) # N는 사람 수, S는 부분합
A = list(map(int, input().split())) # 수치화된 사람들의 능력치
count = 0
print(solve(0, A[0]))
