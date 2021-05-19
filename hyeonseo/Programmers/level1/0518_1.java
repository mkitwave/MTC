// https://programmers.co.kr/learn/courses/30/lessons/1845
// ÆùÄÏ¸ó

import java.util.ArrayList;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int max = nums.length/2;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++){
            if(!arr.contains(nums[i])){
                arr.add(nums[i]);
                if(arr.size()>=max){
                    break;
                }
            }
        }
        answer = arr.size();
        return answer;
    }
}