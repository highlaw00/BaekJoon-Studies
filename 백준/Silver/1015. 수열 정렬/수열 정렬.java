import java.util.*;
import java.util.stream.Collectors;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        List<Integer> arrA = Arrays.stream(sc.nextLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        
        int cnt = 0;
        int[] answer = new int[n];
        for (int i=1; i<=1000; i++) {
            for (int j=0; j<n; j++) {
                if (arrA.get(j) == i) {
                    answer[j] = cnt++;
                }
            }
            if (cnt >= n) {
                break;
            }
        }
        
        for (int num: answer) {
            System.out.print(num + " ");
        }
	}
}