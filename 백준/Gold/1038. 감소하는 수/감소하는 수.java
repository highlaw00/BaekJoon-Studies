import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        new Main().solution();
    }

    public void solution() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Long> decreaseNumbers = new LinkedList<>();
        long[] sortedDecreaseNumbers = new long[1_000_001];

        Queue<Long> queue = new LinkedList<>();
        Set<Long> visited = new HashSet<>();

        for (long i = 0; i < 10; i++) {
            decreaseNumbers.add(i);
            visited.add(i);
            queue.add(i);
        }

        while (!queue.isEmpty()) {
            long number = queue.poll();
            long rightDigit = number % 10;
            for (long i = rightDigit - 1; i >= 0; i--) {
                long temp = number * 10 + i;
                if (temp > 9876543210L || temp < 0) continue;
                if (!visited.contains(temp)) {
                    decreaseNumbers.add(temp);
                    visited.add(temp);
                    queue.add(temp);
                }
            }
        }

        Collections.sort(decreaseNumbers);
        for (int i = 0; i <= 1_000_000; i++) sortedDecreaseNumbers[i] = -1;
        for (int i = 0; i < decreaseNumbers.size(); i++) sortedDecreaseNumbers[i] = decreaseNumbers.get(i);
        System.out.println(sortedDecreaseNumbers[n]);
    }
}
