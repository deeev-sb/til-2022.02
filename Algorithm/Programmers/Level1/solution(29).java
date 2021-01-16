// 2016년

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] day = {"THU", "FRI","SAT","SUN","MON","TUE","WED"};
        int[] month = {31,29,31,30,31,30,31,31,30,31,30,31};
        int sum = b;
        
        for (int i = 0; i < a-1; i++)
            sum += month[i];
        
        answer = day[sum%7];
        
        return answer;
    }
}