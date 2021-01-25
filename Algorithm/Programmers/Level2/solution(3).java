// 피보나치 수
// n번째 수를 1234567로 나눈 나머지

class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] fibonacci = new int[n+1];
        
        if (n == 0)
            return 0;
        else if (n == 1)
            return 1;
        else {
            fibonacci[0] = 0;
            fibonacci[1] = 1;
            for (int i = 2; i < n+1; i++){
                fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2])%1234567;
            }
            answer = fibonacci[n];
        }
        
        
        
        return answer;
    }
}