// 하샤드 수

class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String[] arr = (String.valueOf(x)).split("");
        int xsum = 0;
        for (int i = 0; i < arr.length; i++)
            xsum += Integer.valueOf(arr[i]);
        if (x%xsum != 0)
            answer = false;
        return answer;
    }
}