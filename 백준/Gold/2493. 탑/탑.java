import java.util.*;
import java.io.*;

public class Main {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        String[] towers = br.readLine().split(" ");
        // stack[i] = [value, idx]
        Stack<Integer[]> stack = new Stack<>();
        Integer[] answers = new Integer[n];

        for (int i = n-1; i >= 0; i--) {
            // 현재 숫자와 스택의 top 비교
            int curr = Integer.parseInt(towers[i]);

            // stack.top()이 현재 탑보다 작은 경우
            while (!stack.isEmpty() && stack.peek()[0] < curr) {
                Integer[] prevTower = stack.pop();
                int prevIdx = prevTower[1];
                answers[prevIdx] = i + 1;
            }

            stack.add(new Integer[]{curr, i});
        }

        for (Integer answer: answers) {
            if (answer == null) answer = 0;
            sb.append(answer);
            sb.append(" ");
        }

        System.out.println(sb);

    }
}
