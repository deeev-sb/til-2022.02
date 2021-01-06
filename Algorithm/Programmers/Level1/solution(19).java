// 핸드폰 번호 가리기

class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int len = phone_number.length();
        for (int i = 0; i < len; i++){
            if (i < (len-4))
                answer += "*";
            else
                answer += String.valueOf(phone_number.charAt(i));
        }
        return answer;
    }
}