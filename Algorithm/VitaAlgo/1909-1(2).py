# 수의 비밀 (Level 1)

def CheckThePowerOfTwo(num):
	while (num%2==0):
		num = num/2
	if (num==1):
		return "Yes"
	else:
		return "No"

num = int(input())
print(CheckThePowerOfTwo(num))
