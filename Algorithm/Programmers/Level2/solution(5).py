# N개의 최소공배수

def solution(arr):
    answer = 0
    
    def gcd (a,b): # 최대공약수 구하기
        if a > b:
            a, b = b, a
        while b:
            a, b = b, a%b
        return a
    
    def lcm (a,b): # 최소공배수 구하기
        return a*b//gcd(a,b)
    
    while True:
        if len(arr) == 1: # 길이가 1이 되면 비교할 수가 없으므로 return
            return arr[0]
        arr.append(lcm(arr.pop(), arr.pop())) # pop 시켜서 최소공배수 계속 update
        
    return answer
