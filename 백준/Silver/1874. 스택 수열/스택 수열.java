import java.util.*;
import java.io.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException{
        int n = Integer.parseInt(br.readLine());
        Integer[] numbers = new Integer[n];
        for (int i = 0; i < n; i ++) {
            numbers[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<>();
        int opsCnt = 0;
        int nextNumber = 1;
        boolean isAble = true;

        for (int number: numbers) {
            if (stack.isEmpty() || stack.peek() != number) {
                while (nextNumber <= number) {
                    stack.add(nextNumber);
                    sb.append("+\n");
                    opsCnt ++;
                    nextNumber ++;
                }
            }
            int top = stack.pop();
            if (top == number) {
                sb.append("-\n");
                opsCnt ++;
            } else {
                isAble = false;
                break;
            }
        }

        if (isAble) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }
    }
}
