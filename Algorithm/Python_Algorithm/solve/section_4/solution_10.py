# 역수열(그리디)

def solution(n, nums):
    answer = ''
    temp = [0]*n
    for i in range(n):
        for j in range(n):
            if nums[i]==0 and temp[j]==0:
                temp[j]=i+1
                break
            elif nums[i]!=0 and temp[j]==0:
                nums[i]-=1
    for i in temp:
        answer += str(i) + ' '
    return answer

n = int(input())
nums = list(map(int, input().split()))
print(solution(n, nums))