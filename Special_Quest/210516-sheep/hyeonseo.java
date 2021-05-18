//테스트케이스는나오는데통과가안됨
//그만할라고.....
import java.util.Scanner;
public class Main{

	public static void main(String args[]){
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int testNum = scan.nextInt();
		int[] answerArr = new int[testNum];
		for(int i=0; i<testNum; i++) {
			int height = scan.nextInt();
			int width = scan.nextInt();
			int[][] greed = new int[height][width];
			for(int j=0; j<height; j++) {
				String str = scan.next();
				String[] arr = str.split("",-1);
				for(int k = 0; k<arr.length; k++) {
					if(arr[k].equals("#")) {
						greed[j][k] = 1;
					}
				}
			}
			int answer = 0;
			for(int j=0; j<height; j++) {
				for(int k=0; k<width; k++) {
					if(greed[j][k]==1||greed[j][k]==3) {
						greed[j][k]=2;
						if((j-1<0?1>2:greed[j-1][k]==2)
								||(j+1>=height?1>2:greed[j+1][k]==2)
								||(k-1<0?1>2:greed[j][k-1]==2)
								||(k+1>=width?1>2:greed[j][k+1]==2)) {
						}else {
							if(j+1<height?greed[j+1][k]==1:1<2) {
								try {
									greed[j+1][k]=3;
								}catch(Exception e) {
									
								}
							}	
							boolean check = true;
							// k가 1일때 오른쪽이 1이면 
							for(int l = k+1; l<width; l++) {
								if(greed[j][l]==0) {
									break;
								}
								if(greed[j][l]==3) {
									check = false;
									break;
								}
							}
							if(check) {
								answer++;
							}
							
						}
					}
				}
			}
			answerArr[i] = answer;		
		}
		for(int i=0; i<testNum; i++) {
			System.out.println(answerArr[i]);
		}
	}
}
