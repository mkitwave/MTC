// 2016³â
// https://programmers.co.kr/learn/courses/30/lessons/12901

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        //SUN, MON, TUE, WED, THU, FRI, SAT
        int[] month = {31,29,31,30,31,30,31,31,30,31,30,31};
        int day = 0;
        for(int i=1; i<a; i++){
            day+=month[i-1];
        }
        day+=b;
        day%=7;
        switch(day){
            case 0: answer = "THU"; break;
            case 1: answer = "FRI"; break;
            case 2: answer = "SAT"; break;
            case 3: answer = "SUN"; break;
            case 4: answer = "MON"; break;
            case 5: answer = "TUE"; break;
            case 6: answer = "WED"; break;
        }
        
        return answer;
    }
}