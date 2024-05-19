import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] numbers = new int[n+1];
            String[] line = br.readLine().split(" ");
            for (int j = 1; j <= n; j++) {
                numbers[j] = Integer.parseInt(line[j-1]);
            }

            // 0부터 n-1까지 최대 부분 수열을 구한다!
            int answer = getMaximumSubArray(numbers);

            System.out.println(answer);
        }
    }

    public int getMaximumSubArray(int[] numbers) {
        int maximum = -Integer.MAX_VALUE;
        int[] prefix = new int[numbers.length]; // prefix[i] = numbers[0] + numbers[1] + ... + numbers[n-1];
        for (int i = 1; i < numbers.length; i++) {
            prefix[i] = prefix[i-1] + numbers[i];
        }

        for (int i = 0; i < numbers.length-1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                maximum = Integer.max(maximum, prefix[j] - prefix[i]);
            }
        }

        return maximum;
    }
}
