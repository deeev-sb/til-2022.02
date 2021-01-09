# 바둑이 승차 (DFS)

# total_sum은 붕붕이에 태울지 말지 고민한 멍멍이의 무게합
def DFS(index, weight_sum, total_sum):
    global result
    # 남은 멍멍이의 무게합이 최대합보다 작으면 return (이 조건 강의 참고)
    if weight_sum + (total-total_sum) < result: 
        return
    if weight_sum >= max_weight:
        return
    if index == n:
        if weight_sum > result:
            result = weight_sum
    else:
        DFS(index+1, weight_sum + dogs[index] , total_sum + dogs[index])
        DFS(index+1, weight_sum, total_sum + dogs[index])
    
    

if __name__=="__main__":
    max_weight, n = map(int, (input().split()))
    dogs = []
    result = 0
    for i in range(n) :
        dogs.append(int(input()))
    total = sum(dogs)
    DFS(0, 0, 0)
    print(result)