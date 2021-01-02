// 올바른 괄호

import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = false;
        Stack<Character> st = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(')
                st.push('(');
            else {
                if (st.isEmpty())
                    return false;
                st.pop();
            }
        }
        
        if (st.isEmpty())
            answer = true;

        return answer;
    }
}