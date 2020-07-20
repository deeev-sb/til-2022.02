// 문자열 내림차순으로 배치하기

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    for (int i = 0; i < s.size(); i++){
        for (int j = i+1; j <= s.size(); j++){
            if (s[i] < s[j]){
                char temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    answer = s;
    return answer;
}
