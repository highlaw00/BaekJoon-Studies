import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        new Main().solution();
    }

    /*
        - 첫번째 카드를 n번만큼 가장 뒤로 옮긴다.
        - 그 후 첫번째 카드가 n번 카드여야한다.

        - n을 덱의 앞쪽에 삽입
        - n번 만큼 가장 뒷쪽의 카드를 가장 앞쪽으로 옮긴다.
     */

    public void solution() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Deque<Integer> deque = new LinkedList<>();
        StringBuilder sb = new StringBuilder();

        for (int i = n; i >= 1; i--) {
            deque.addFirst(i);
            for (int j = 0; j < i; j++) {
                int last = deque.pollLast();
                deque.addFirst(last);
            }
        }

        for (int i = 0; i < n; i++) {
            sb.append(deque.pollFirst());
            sb.append(" ");
        }

        System.out.println(sb);

    }
}
