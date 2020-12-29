// 문자열 내림차순으로 배치하기
// 자바도 split, join, sort, reverse 기능 존재

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] sp = s.split("");
        Arrays.sort(sp);
        Collections.reverse(Arrays.asList(sp));
        answer = String.join("", sp);
        return answer;
    }
}