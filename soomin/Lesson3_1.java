package Codility;

public class Lesson3_1 {
//1번째 시도 : 44% - runtime Error 발생
	static int solution(int X,int Y,int D) {
		int count=0;
		while(Y>X) {
			X+=D;
			count++;
		}
		return count;
	}
	public static void main(String[] args) {
		System.out.println(solution(10,85,30));
	}

}
