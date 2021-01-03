// 문자열 내 p와 y의 개수

import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int ycount = 0;
        int pcount = 0;

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'y' || s.charAt(i) == 'Y')
                ycount++;
            else if (s.charAt(i) == 'p' || s.charAt(i) == 'P')
                pcount++;
        }
        
        if (ycount != pcount)
            answer = false;

        return answer;
    }
}