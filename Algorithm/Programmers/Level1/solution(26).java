// 최대공약수와 최소공배수

class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        if (n > m){
            int temp = n;
            n = m;
            m = temp;
        }
        
        // 최대공약수
        for (int i = n; i > 0; i--){
            if (n%i == 0 && m%i == 0){
                answer[0] = i;
                break;
            }
        }
        
        // 최소공배수 = 두 수의 곱/최대공약수
        answer[1] = n * m / answer[0];
        
        return answer;
    }
}