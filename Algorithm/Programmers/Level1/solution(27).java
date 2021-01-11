// 콜라측 추측
// int로 받아오던 num을 long으로 변경하니 정상 수행됨
// 파라미터를 그대로 사용할 때 int라서 범위 오류로 인한 오버플로우가 발생한 것 같음

class Solution {
    public int solution(long num) {
        int answer = 0;
        
        for (int i = 0; i < 500; i++){
            if (num == 1)
                break;
            if (num%2 == 0)
                num /= 2;
            else
                num = num * 3 +1;
            answer += 1;
        }
        
        System.out.println(num);
        
        if (num != 1)
            answer = -1;
        
        return answer;
    }
}