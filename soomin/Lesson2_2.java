package Codility;

import java.util.Arrays;
//OddOccurrencesInArray
//XOR연산으로 푸는 방법도 있으나 아직 이해하지 못했다. 
public class Lesson2_2 {
	public static int solution(int[]A) {
		//시간복잡도 O(N) or O(N*log(N))
		Arrays.sort(A); //A배열을 정렬해준다. 
		int answer=A[0];
		int count=1;
		for(int i=1;i<A.length;i++) {
			if(answer==A[i]) {
				count+=1;
			}else {
				if(count%2==0) {
					answer=A[i];
					count=1;
				}else {
					return answer;
				}
			}
		}
		
		return answer;
	}
	
	public static void main(String[]args) {
		int[]A=new int[] {9,3,9,3,9,7,9};
		System.out.println(solution(A));
	}
}
