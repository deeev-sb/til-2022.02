// 평균 구하기
// 문자의 길이는 length(), 배열의 길이는 length!!!

class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++){
            answer += arr[i];
        }
        answer /= n;
        return answer;
    }
}