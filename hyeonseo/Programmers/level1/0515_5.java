// 가운데 글자 가져오기
// https://programmers.co.kr/learn/courses/30/lessons/12903

class Solution {
    public String solution(String s) {
        String answer = "";
        if(s.length()%2==0) {
			 answer+=s.charAt(s.length()/2-1);;
		 }
		 answer+=s.charAt(s.length()/2);
        return answer;
    }
}