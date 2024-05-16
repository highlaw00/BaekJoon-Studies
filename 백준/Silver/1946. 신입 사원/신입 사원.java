import java.util.*;
import java.io.*;

public class Main {
    class Pair {
        int paper;
        int interview;
        Pair(int paper, int interview) {
            this.paper = paper;
            this.interview = interview;
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(solutionOne(n));
        }
    }

    public int solutionOne(int n) throws IOException {
        Pair[] pairs = new Pair[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int paper = Integer.parseInt(st.nextToken());
            int interview = Integer.parseInt(st.nextToken());
            pairs[i] = new Pair(paper, interview);
        }
        // 서류 점수를 기준으로 오름차순 정렬
        Arrays.sort(pairs, (p1, p2) -> Integer.compare(p1.paper, p2.paper));
        // 누적 배열 선언
        int[] prefix = new int[n];
        for (int i = 0; i < n; i++) {
            prefix[i] = Integer.MAX_VALUE;
        }
        // 누적 배열 초기화
        for (int i = 1; i < n; i++) {
            prefix[i] = Integer.min(prefix[i-1], pairs[i-1].interview);
        }

        int failCnt = 0;
        // 불합격자 결정
        for (int i = 0; i < n; i++) {
            Pair curr = pairs[i];
            int currInterview = curr.interview;
            if (currInterview > prefix[i]) failCnt++;
        }

        return n - failCnt;
    }
}
