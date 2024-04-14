import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();
        int[] answers = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = n-1; i >= 0; i --) {
            int currentElem = numbers[i];
            // 비어있지 않고, 현재 원소가 top보다 크면 pop
            while (!stack.isEmpty() && currentElem >= stack.peek()) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                answers[i] = -1;
            } else {
                answers[i] = stack.peek();
            }
            // stack.add(currentElem); // add를 써서 그런가?!!!!
            stack.push(currentElem);
        }

        for (int answer: answers) {
            sb.append(answer);
            sb.append(" ");
        }
        System.out.println(sb);
    }
}
