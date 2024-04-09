import java.util.*;
import java.io.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        String[] lines = br.readLine().split(" ");
        Stack<Integer> stack = new Stack<>();

        int cnt = 1;

        for (int i = 0; i < n; i++) {
            int temp = Integer.parseInt(lines[i]);
            stack.push(temp);
            // 다음 사람을 받을 수 있다면 받는다.
            while (!stack.isEmpty() && stack.peek() == cnt) {
                stack.pop();
                cnt ++;
            }
        }

        if (stack.isEmpty()) System.out.println("Nice");
        else System.out.println("Sad");

    }
}
