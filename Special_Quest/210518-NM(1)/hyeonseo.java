import java.util.Scanner;
// 너무 어려워서,.... 구글링했음.........양심선언
public class Main {
	public static int[] arr;
	public static boolean[] visit;
	
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();
		
		arr = new int[m];
		visit = new boolean[n];
		
		func(n,m,0);
	}
	public static void func(int n, int m, int depth) {
		if(depth == m) {
			for(int a:arr) {
				System.out.print(a+" ");
			}
			System.out.println("");
			return;
		}
		for(int i=0; i<n; i++) {
			if(!visit[i]) {
				visit[i] = true;
				arr[depth]=i+1;
				func(n,m,depth+1);
				visit[i] = false;
			}
		}
		
	}
}
  