import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        new Main().solution();
    }

    public void solution() {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int m = Integer.parseInt(sc.nextLine());
        int[] lights = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int h = lights[0];
        int prev = 0;
        for (int next: lights) {
            if (prev + h < next - h) {
                // h가 부족하여 이전 가로등과 다음 가로등 사이에 여백이 존재함
                h = (next - prev) / 2 + ((next - prev) % 2 == 0 ? 0 : 1);
            }
            prev = next;
        }

        // 마지막 가로등과 굴다리 끝 사이에 여백이 존재하는지 확인
        if (prev + h < n) {
            h = n - prev;
        }

        System.out.println(h);
    }

}
