// 소수 찾기
// 에라토스테네스 체 활용

class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] check = new int[n+1]; // 0으로 초기화
        
        for (int i = 2; i < n+1; i++){
            if (check[i] == 0){
                answer += 1;
                for (int j = i; j < n+1;){
                    check[j] = 1;
                    j += i;
                }
            }
        }
        
        return answer;
    }
}