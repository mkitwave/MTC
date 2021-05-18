// https://programmers.co.kr/learn/courses/30/lessons/12947
// ÇÏ»þµå ¼ö

class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String num = Integer.toString(x);
        int sum = 0;
        for(int i=0; i<num.length(); i++){
            sum += Integer.parseInt(num.substring(i,i+1));
        }
        if(x%sum != 0){
            answer = false;
        }
        return answer;
    }
}