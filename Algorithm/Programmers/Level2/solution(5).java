// N개의 최소공배수
// 순서대로 값의 최소공배수를 구해가면 됨
// 최소공배수 공식 = 두 수의 곱 // 최대공약수

class Solution {
    
    // 최대공약수 구하기
    public int gcd(int a, int b){
        while (a != 0 && b != 0){
            if (a > b)
                a = a % b;
            else
                b = b % a;
        }
        return a + b;
    }
    
    // 최소공배수 구하기
    public int lcm(int a, int b){
        return a * b / gcd(a, b);
    }
    
    public int solution(int[] arr) {
        int answer = arr[0];
        for (int i = 1; i < arr.length; i++)
            answer = lcm(answer, arr[i]);
        return answer;
    }
}