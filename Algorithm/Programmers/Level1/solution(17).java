// 이상한 문자 만들기
// 공백까지 신경써서 만들어야 함

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == ' '){
                cnt = 0;
                answer += " ";
            }
            else {
                if (cnt%2 == 0){
                    cnt++;
                    answer += String.valueOf(s.charAt(i)).toUpperCase();
                }
                else{
                    cnt++;
                    answer += String.valueOf(s.charAt(i)).toLowerCase();
                }
            }
        }
        return answer;
    }
}