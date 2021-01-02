// 문자열 내 마음대로 정렬하기
// comparator를 통해 기본 정렬 기준과 다르게 정렬 가능 (주로 내림차순을 만들 때 많이 사용)
// comparable은 정렬 수행 시 기본적으로 적용되는 정렬 기준이 되는 메서드 (오름차순, 사전순)

import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        
        Arrays.sort(strings, new Comparator<String>(){
            public int compare(String s1, String s2){
                if (s1.charAt(n) > s2.charAt(n))
                    return 1;
                else if (s1.charAt(n) == s2.charAt(n))
                    return s1.compareTo(s2);
                else
                    return -1;
            }
        });
        
        
        return strings;
    }
}