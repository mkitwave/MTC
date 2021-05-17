import java.util.Scanner;

public class Main{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		int cownum = scan.nextInt();
		int width = scan.nextInt();
		int height = scan.nextInt();
		int space = scan.nextInt();
		
		System.out.println(((width/space)*(height/space)>cownum?cownum:(width/space)*(height/space)));
	}
}
