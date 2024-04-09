import java.util.*;
import java.io.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer strTokenizer = new StringTokenizer(br.readLine());
        Queue<Integer> queue = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();

        while (strTokenizer.hasMoreTokens()) {
            queue.add(Integer.parseInt(strTokenizer.nextToken()));
        }

        int cnt = 1;
        boolean flag = true;

        while (cnt <= n && flag) {
            // queue의 top을 확인. 다르다면 stack에 저장
            // queue의 top을 확인. 같다면 그대로 cnt 증가
            // queue가 비어있다면 stack만 바라보기
            if (queue.isEmpty()) {
                // 스택의 top과 cnt를 비교
                while (!stack.isEmpty()) {
                    if (stack.pop() == cnt) {
                        cnt ++;
                    } else {
                        flag = false;
                        break;
                    }
                }
            } else if (queue.peek() == cnt) {
                queue.poll();
                cnt ++;
            } else if (!stack.isEmpty() && stack.peek() == cnt) {
                stack.pop();
                cnt ++;
            } else {
                stack.add(queue.poll());
            }
        }

        if (flag) System.out.println("Nice");
        else System.out.println("Sad");
    }
}
